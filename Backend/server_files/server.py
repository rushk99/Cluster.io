from ariadne import (
    QueryType,
    MutationType,
    ObjectType,
    make_executable_schema,
    load_schema_from_path,
    InterfaceType,
    convert_kwargs_to_snake_case,
)
from ariadne.asgi import GraphQL
from ariadne.contrib.tracing.apollotracing import ApolloTracingExtension
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.applications import Starlette
import pandas as pd
import json
import sys
import boto3
import os
from urllib.parse import urlparse
s3 = boto3.client("s3",
                  aws_access_key_id="AKIA52QUT77PGKPYKG5H",
                  aws_secret_access_key="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")
sys.path.append("../")

from helpers import StringDefinitionsHelper
from helpers.ComparisonHelper import compare_cluster
from server_helpers import cluster_helper
from subscriptions import subscription
from json_data import data

query = QueryType()
mutation = MutationType()
type_defs = load_schema_from_path("schema.graphql")



def upload_to_s3(file, object_name):
    bucket="materialdatasets"
    s3.upload_fileobj(file, bucket, object_name)
    return f"https://{bucket}.s3.amazonaws.com/{object_name}"

def download_from_s3(url,folder):
    parsed_url = urlparse(url)
    bucket = "materialdatasets"
    object_key = parsed_url.path.strip('/')
    file_name = os.path.basename(object_key)
    local_path = os.path.join(folder, file_name)
    clear_temp()
    s3.download_file(bucket, object_key, local_path)
    return local_path
     

with open('datasets.json', 'r') as file:
    datasets = json.load(file)

def clear_temp():
    bucket_name = 'materialdatasets'
    directory_name = 'temp_image/'

    objects = s3.list_objects_v2(Bucket=bucket_name, Prefix=directory_name)
    if 'Contents' in objects:
        delete_keys = {'Objects': [{'Key': obj['Key']} for obj in objects['Contents']]}
        s3.delete_objects(Bucket=bucket_name, Delete=delete_keys)
    folder_paths = ["../temp_image","../temp_dataset","../temp_clustered_data"]
    for folder_path in folder_paths:
        file_list = os.listdir(folder_path)
        if file_list:
            for file_name in file_list:
                file_path = os.path.join(folder_path, file_name)
                os.remove(file_path)

def populate_response_with_image_url(response):
    with open("../temp_image/raw_data.png", "rb") as f:
            response["rawData"]=upload_to_s3(f,"temp_image/raw_data.png")
    with open("../temp_image/clustered_data.png", "rb") as f:
            response["clusteredData"]=upload_to_s3(f,"temp_image/clustered_data.png")
    with open("../temp_image/clusters_fractions.png", "rb") as f:
            response["clustersFractions"]=upload_to_s3(f,"temp_image/clusters_fractions.png")
    return response
@query.field("datasets")
def resolve_Datasets(_,info):
    """
    Returns the name of all datasets
    """
    for file in datasets["datasets"]:
        yield file

@query.field("configs")
def resolve_configs(_,info):
    """
    Returns the name of all datasets
    """
    for file in datasets["configData"]:
        yield file

@query.field("clusteredDataset")
def resolve_clusteredDataset(_,info,name):
    """
    Returns the name of all datasets
    """
    for file in datasets["configData"]:
        if (file["name"]==name):
            ClusteredDataset=download_from_s3(file["clusteredDataset"],"../temp_clustered_data/")
            df = pd.read_excel(ClusteredDataset)
            data = [{"x": row["x"], "y": row["y"],"labeldata":row["label"], "cluster": row["cluster"]} for _, row in df.iterrows()]
            return data
        
@query.field("config")
def resolve_config(_,info,name):
    for file in datasets["configData"]:
        if (file["name"]==name):
            return file

@query.field("clusterComparisons")
def resolve_clusterComparisons(_,info,list,metric):
    clusterNames = list.split(",")
    scores=[]
    for cluster in clusterNames:
        for file in datasets["configData"]:
            if (file["name"]==cluster):
                ClusteredDataset=download_from_s3(file["clusteredDataset"],"../temp_clustered_data/")
                df = pd.read_excel(ClusteredDataset)
                datapoints = [[row['label']] for index, row in df.iterrows()]
                labels = [[row['cluster']] for index, row in df.iterrows()]
                score=str(compare_cluster(datapoints,labels,metric))
                scores.append({"clustername":cluster,"metric":metric,"score":score})
    print("done")
    return scores

@query.field("dataset")
def resolve_dataset(_,info,name):
    """
    Returns the dataset given a name
    """
    for file in datasets["datasets"]:
        if (file["name"]==name):
            return file

@mutation.field("uploadDataset")
async def resolve_uploadDataset(_,info,name, file, description):
    """
    Returns the dataset given a name
    """
    url= str(upload_to_s3(file.file,file.filename))
    temp={
        "name":name,
        "fileName": file.filename,
        "description":description,
        "url":url
    }
    datasets["datasets"].append(temp)
    with open('datasets.json', 'w') as file:
        json.dump(datasets, file, indent=4)
    for file in datasets["datasets"]:
        if (file["name"]==name):
            return file
@mutation.field("uploadConfig")
async def resolve_uploadConfig(_,info, name,  parameters, datasetName,label ):
    parameterobj = json.loads(parameters)
    del parameterobj['datasetName']
    temp=[]
    for i in parameterobj:
        temp.append({"name":i,"value":parameterobj[i]})
    with open("../temp_image/raw_data.png", "rb") as f:
        rawData=upload_to_s3(f,"clusterConfig/"+datasetName+"/"+name+"/raw_data.png")
    with open("../temp_image/clustered_data.png", "rb") as f:
        clusteredData=upload_to_s3(f,"clusterConfig/"+datasetName+"/"+name+"/clustered_data.png")
    with open("../temp_image/clusters_fractions.png", "rb") as f:
        clustersFractions=upload_to_s3(f,"clusterConfig/"+datasetName+"/"+name+"/clusters_fractions.png")
    with open("../temp_clustered_data/ClusteredData.xlsx", "rb") as f:
        clusteredDataset=upload_to_s3(f,"clusterConfig/"+datasetName+"/"+name+"/ClusteredData.xlsx")
    temp={
            "name":name, 
            "parameters":temp, 
            "datasetName":datasetName, 
            "rawData":rawData, 
            "clusteredData":clusteredData, 
            "clustersFractions":clustersFractions,
            "clusteredDataset":clusteredDataset,
            "label":label,
    }
    datasets["configData"].append(temp)
    with open('datasets.json', 'w') as file:
        json.dump(datasets, file, indent=4)
    for file in datasets["configData"]:
        if (file["name"]==name):
            return file

@mutation.field("deleteDataset")
async def resolve_deleteDataset(_,info,name):
    """
    Returns the dataset of the recently uploaded dataset
    """
    for ind,file in enumerate(datasets["datasets"]):
        if (file["name"]==name):
            url=file["url"]
            bucket_name = url.split("//")[1].split(".")[0]
            file_key = url.split("//")[1].split("/", 1)[1]
            s3.delete_object(Bucket=bucket_name, Key=file_key)
            del datasets["datasets"][ind]
            with open('datasets.json', 'w') as file:
                json.dump(datasets, file, indent=4)
            return True
    return False

@mutation.field("deleteConfig")
async def resolve_deleteConfig(_,info,name):
    for ind,file in enumerate(datasets["configData"]):
        if (file["name"]==name):
            url=file["rawData"]
            bucket_name = url.split("//")[1].split(".")[0]
            file_key = url.split("//")[1].split("/", 1)[1]
            s3.delete_object(Bucket=bucket_name, Key=file_key)
            url=file["clusteredData"]
            bucket_name = url.split("//")[1].split(".")[0]
            file_key = url.split("//")[1].split("/", 1)[1]
            s3.delete_object(Bucket=bucket_name, Key=file_key)
            url=file["clustersFractions"]
            bucket_name = url.split("//")[1].split(".")[0]
            file_key = url.split("//")[1].split("/", 1)[1]
            s3.delete_object(Bucket=bucket_name, Key=file_key)
            url=file["clusteredDataset"]
            bucket_name = url.split("//")[1].split(".")[0]
            file_key = url.split("//")[1].split("/", 1)[1]
            s3.delete_object(Bucket=bucket_name, Key=file_key)
            del datasets["configData"][ind]
            with open('datasets.json', 'w') as file:
                json.dump(datasets, file, indent=4)
            return True
    return False

@query.field("clusteringMethods")
def resolve_clusteringMethods(_, info):
    """
    Returns no or yes if the dataset is deleted or uploaded
    """
    for method in data["clusteringMethods"]:
        yield method["name"]


@query.field("clusteringMethod")
def resolve_clusteringMethod(_, info, name):
    return name


clusteringMethod = InterfaceType("ClusteringMethod")


@clusteringMethod.type_resolver
def resolve_type(obj, *_):
    return obj


@clusteringMethod.field("label")
def resolve_name(_, info):
    """
    Gets the display name for a clustering method
    :param _: Unused parameter
    :param info: used to ge the type of the clustering method
    :return: the display name of the clustering method
    """
    for method in data["clusteringMethods"]:
        if method["name"] == str(info.parent_type):
            return method["label"]


@clusteringMethod.field("name")
def resolve_name(_, info):
    """
    Gets the name for a clustering method
    :param _: Unused parameter
    :param info: used to ge the type of the clustering method
    :return: the display name of the clustering method
    """
    for method in data["clusteringMethods"]:
        if method["name"] == str(info.parent_type):
            return method["name"]


@clusteringMethod.field("options")
def resolve_name(_, info):
    """
    Gets the options associated with a clustering method
    :param _: unused parameter
    :param info: used to get the type of the clustering method
    :return: list of options for the clustering method
    """
    for method in data["clusteringMethods"]:
        if method["name"] == str(info.parent_type):
            return method["options"]


kMeans = ObjectType("KMeans")


@kMeans.field("cluster")
@convert_kwargs_to_snake_case
async def resolve_kMeans_cluster(_, info, num_clusters, random_state, dataset_name, cluster_data_on):
    """
    Resolves the cluster query for KMeans clustering
    :param _: unused parameter
    :param info: unused parameter
    :param num_clusters: A parameter taken by the clustering method
    :param random_state: A parameter taken by the clustering method
    :return: A response with the results and/or errors
    """
    print("testing")
    print(num_clusters,random_state)
    clustering_details = {"num_clusters": int(num_clusters), "random_state": int(random_state)}
    for file in datasets["datasets"]:
        if (file["name"]==dataset_name):
            url=file["url"]
    file_name=download_from_s3(url,'../temp_dataset/')
    response = await cluster_helper(
        StringDefinitionsHelper.K_MEANS_LABEL, clustering_details, file_name,cluster_data_on
    )
    return populate_response_with_image_url(response)


birch = ObjectType(StringDefinitionsHelper.BIRCH_LABEL)


@birch.field("cluster")
@convert_kwargs_to_snake_case
async def resolve_birch_cluster(_, info, num_clusters,threshold,branching_factor, dataset_name, cluster_data_on):
    """
    Resolves the cluster query for Birch clustering
    :param _: unused parameter
    :param info: unused parameter
    :param num_clusters: A parameter taken by the clustering method
    :return: A response with the results and/or errors
    """
    clustering_details = {"num_clusters": int(num_clusters), "threshold":float(threshold),"branching_factor":int(branching_factor)}
    for file in datasets["datasets"]:
        if (file["name"]==dataset_name):
            url=file["url"]
    file_name=download_from_s3(url,'../temp_dataset/')
    response = await cluster_helper(
        StringDefinitionsHelper.BIRCH_LABEL, clustering_details, file_name, cluster_data_on
    )
    return populate_response_with_image_url(response)


agglomerative = ObjectType(StringDefinitionsHelper.AGGLOMERATIVE_LABEL)


@agglomerative.field("cluster")
@convert_kwargs_to_snake_case
async def resolve_agglomerative_cluster(_, info, num_clusters, linkage, dataset_name, cluster_data_on):
    """
    Resolves the cluster query for Agglomerative Clustering
    :param _: unused parameter
    :param info: unused parameter
    :param num_clusters: A parameter taken by the clustering method
    :param linkage: A parameter taken by the clustering method
    :return: A response with the results and/or errors
    """
    clustering_details = {"num_clusters": int(num_clusters), "linkage": linkage}
    for file in datasets["datasets"]:
        if (file["name"]==dataset_name):
            url=file["url"]
    file_name=download_from_s3(url,'../temp_dataset/')
    response = await cluster_helper(
        StringDefinitionsHelper.AGGLOMERATIVE_LABEL, clustering_details, file_name, cluster_data_on
    )
    return populate_response_with_image_url(response)


dbscan = ObjectType(StringDefinitionsHelper.DBSCAN_LABEL)


@dbscan.field("cluster")
@convert_kwargs_to_snake_case
async def resolve_dbscan_cluster(_, info, eps, min_samples, algorithm, dataset_name, cluster_data_on):
    """
    Resolves the cluster query for DBSCAN Clustering
    :param _: unused parameter
    :param info: unused parameter
    :param eps: A parameter taken by the clustering method
    :param min_samples: A parameter taken by the clustering method
    :param algorithm: A parameter taken by the clustering method
    :return: A response with the results and/or errors
    """
    clustering_details = {
        "eps": float(eps),
        "min_samples": int(min_samples),
        "algorithm": algorithm,
    }
    for file in datasets["datasets"]:
        if (file["name"]==dataset_name):
            url=file["url"]
    file_name=download_from_s3(url,'../temp_dataset/')
    response = await cluster_helper(
        StringDefinitionsHelper.DBSCAN_LABEL, clustering_details, file_name, cluster_data_on
    )
    return populate_response_with_image_url(response)


deconvolution = ObjectType(StringDefinitionsHelper.DECONVOLUTION_LABEL)


@deconvolution.field("cluster")
@convert_kwargs_to_snake_case
async def resolve_deconvolution_cluster(_, info, m_val, max_iter, limit, dataset_name, cluster_data_on):
    """
    Resolves the cluster query for Deconvolution
    :param _: unused parameter
    :param info: unused parameter
    :param m_val: A parameter taken by the clustering method
    :param max_iter: A parameter taken by the clustering method
    :param limit: A parameter taken by the clustering method
    :param label: A parameter taken by the clustering method
    :return: A response with the results and/or errors
    """
    clustering_details = {
        "m_val": int(m_val),
        "max_iter": int(max_iter),
        "limit": float(limit),
    }
    for file in datasets["datasets"]:
        if (file["name"]==dataset_name):
            url=file["url"]
    file_name=download_from_s3(url,'../temp_dataset/')
    response = await cluster_helper(
        StringDefinitionsHelper.DECONVOLUTION_LABEL, clustering_details, file_name, cluster_data_on
    )
    return populate_response_with_image_url(response)



kmedoids = ObjectType("KMedoids")


@kmedoids.field("cluster")
@convert_kwargs_to_snake_case
async def resolve_kmedoids_cluster(_, info, num_clusters, init, random_state, dataset_name, cluster_data_on):
    """
    Resolves the cluster query for KMedoids Clustering
    :param _: unused parameter
    :param info: unused parameter
    :param num_clusters: A parameter taken by the clustering method
    :param init: A parameter taken by the clustering method
    :param random_state: A parameter taken by the clustering method
    :return: A response with the results and/or errors
    """
    clustering_details = {
        "num_clusters": int(num_clusters),
        "init": init,
        "random_state": int(random_state),
    }
    for file in datasets["datasets"]:
        if (file["name"]==dataset_name):
            url=file["url"]
    file_name=download_from_s3(url,'../temp_dataset/')
    response = await cluster_helper(
        StringDefinitionsHelper.K_MEDOIDS_LABEL, clustering_details, file_name, cluster_data_on
    )
    return populate_response_with_image_url(response)


optics = ObjectType(StringDefinitionsHelper.OPTICS_LABEL)


@optics.field("cluster")
@convert_kwargs_to_snake_case
async def resolve_optics_cluster(_, info, max_eps, min_samples, algorithm, dataset_name, cluster_data_on):
    """
    Resolves the cluster query for optics clustering
    :param _: unused parameter
    :param info: unused parameter
    :param eps: A parameter taken by the clustering method
    :param min_samples: A parameter taken by the clustering method
    :param algorithm: A parameter taken by the clustering method
    :return: A response with the results and/or errors
    """
    clustering_details = {
        "max_eps": float(max_eps),
        "min_samples": int(min_samples),
        "algorithm": algorithm,
    }
    for file in datasets["datasets"]:
        if (file["name"]==dataset_name):
            url=file["url"]
    file_name=download_from_s3(url,'../temp_dataset/')
    response = await cluster_helper(
        StringDefinitionsHelper.OPTICS_LABEL, clustering_details, file_name, cluster_data_on
    )
    return populate_response_with_image_url(response)



fuzzycmeans = ObjectType("Fuzzycmeans")


@fuzzycmeans.field("cluster")
@convert_kwargs_to_snake_case
async def resolve_fuzzycmeans_cluster(_, info, num_clusters, fuzzifier, dataset_name, cluster_data_on):
    """
    Resolves the cluster query for optics clustering
    :param _: unused parameter
    :param info: unused parameter
    :param eps: A parameter taken by the clustering method
    :param min_samples: A parameter taken by the clustering method
    :param algorithm: A parameter taken by the clustering method
    :return: A response with the results and/or errors
    """
    clustering_details = {
        "num_clusters": int(num_clusters),
        "fuzzifier": int(fuzzifier),
    }
    for file in datasets["datasets"]:
        if (file["name"]==dataset_name):
            url=file["url"]
    file_name=download_from_s3(url,'../temp_dataset/')
    response = await cluster_helper(
        "fuzzycmeans", clustering_details, file_name, cluster_data_on
    )
    return populate_response_with_image_url(response)



spectral = ObjectType(StringDefinitionsHelper.SPECTRAL_LABEL)


@spectral.field("cluster")
@convert_kwargs_to_snake_case
async def resolve_spectral_cluster(
    _, info, num_clusters, assign_labels, affinity, random_state, dataset_name, cluster_data_on
):
    """
    Resolves the cluster query for spectral clustering
    :param _: unused parameter
    :param info: unused parameter
    :param num_clusters: A parameter taken by the clustering method
    :param assign_labels: A parameter taken by the clustering method
    :param affinity: A parameter taken by the clustering method
    :param random_state: A parameter taken by the clustering method
    :return: A response with the results and/or errors
    """
    clustering_details = {
        "num_clusters": int(num_clusters),
        "assign_labels": assign_labels,
        "affinity": affinity,
        "random_state": int(random_state),
    }
    for file in datasets["datasets"]:
        if (file["name"]==dataset_name):
            url=file["url"]
    file_name=download_from_s3(url,'../temp_dataset/')
    response = await cluster_helper(
        StringDefinitionsHelper.SPECTRAL_LABEL, clustering_details, file_name, cluster_data_on
    )
    return populate_response_with_image_url(response)


schema = make_executable_schema(
    type_defs,
    [
        query,
        clusteringMethod,
        kMeans,
        birch,
        agglomerative,
        dbscan,
        deconvolution,
        kmedoids,
        optics,
        fuzzycmeans,
        spectral,
        subscription,
        mutation
    ],
)


app = Starlette(debug=True)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
)
app.mount("/graphql", GraphQL(schema, debug=True))

# app = GraphQL(
#     schema, debug=True, extensions=[ApolloTracingExtension], middleware=middleware
# )
