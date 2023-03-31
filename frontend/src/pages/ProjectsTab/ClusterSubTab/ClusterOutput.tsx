import { useState , memo } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { gql, useQuery,useMutation  } from "@apollo/client";
import { Box } from '@material-ui/core';
//////////////////////////////////////////////
const useStyles = makeStyles(theme => ({
	//Title, the top of the side bar where the project name is
	window: {
		marginLeft: 250,
		marginTop: 100,
		backgroundColor: '#C9D9D2' 
	},
	createButton: {
		marginTop: 25,
		marginBottom:10
		
		
	},
	text: {
		paddingTop: 15
	},
	config:{
		textAlign: "left",
		marginLeft:10
	},
	clusterButton:{
		textAlign: "center",
		marginBottom:20
	}
}));

const GET_KMEANS_OUTPUT = gql`
  query getKMeansOutput( $numClusters: String!, $randomState: String!, $datasetName:String!, $clusterDataOn:String!) {
    clusteringMethod(name:"KMeans"){
  ...on KMeans{
    cluster(numClusters:$numClusters randomState:$randomState datasetName:$datasetName clusterDataOn:$clusterDataOn){
      error
      rawData
      clusteredData
      clustersFractions
    }
  }
}
  }
`;

const GET_FUZZYCMEANS_OUTPUT = gql`
  query getFuzzycmeansOutput( $numClusters: String!, $fuzzifier: String!, $datasetName:String!, $clusterDataOn:String!) {
    clusteringMethod(name:"Fuzzycmeans"){
  ...on Fuzzycmeans{
    cluster(numClusters:$numClusters fuzzifier:$fuzzifier datasetName:$datasetName clusterDataOn:$clusterDataOn){
      error
      rawData
      clusteredData
      clustersFractions
    }
  }
}
  }
`;

const GET_Birch_OUTPUT = gql`
  query getBirchOutput( $numClusters: String!,$threshold: String! ,$branchingFactor: String!,$datasetName:String!, $clusterDataOn:String!) {
    clusteringMethod(name:"Birch"){
  ...on Birch{
    cluster(numClusters:$numClusters threshold:$threshold branching_factor:$branchingFactor datasetName:$datasetName clusterDataOn:$clusterDataOn){
      error
      rawData
      clusteredData
      clustersFractions
    }
  }
}
  }
`;
const GET_Agglomerative_OUTPUT = gql`
  query getAgglomerativeOutput( $numClusters: String!,$linkage:String! $datasetName:String!, $clusterDataOn:String!) {
    clusteringMethod(name:"Agglomerative"){
  ...on Agglomerative{
    cluster(numClusters:$numClusters linkage:$linkage datasetName:$datasetName clusterDataOn:$clusterDataOn){
      error
      rawData
      clusteredData
      clustersFractions
    }
  }
}
  }
`;

const GET_DBSCAN_OUTPUT = gql`
  query getDBSCANOutput( $eps: String!,$minSamples:String! $algorithm: String! $datasetName:String!, $clusterDataOn:String!) {
    clusteringMethod(name:"DBSCAN"){
  ...on DBSCAN{
    cluster(eps:$eps minSamples:$minSamples algorithm:$algorithm datasetName:$datasetName clusterDataOn:$clusterDataOn){
      error
      rawData
      clusteredData
      clustersFractions
    }
  }
}
  }
`;

const GET_Deconvolution_OUTPUT = gql`
  query getDeconvolutionOutput( $mVal: String!,$maxIter:String! $limit: String!  $datasetName:String!, $clusterDataOn:String!) {
    clusteringMethod(name:"Deconvolution"){
  ...on Deconvolution{
    cluster(mVal:$mVal maxIter:$maxIter limit:$limit  datasetName:$datasetName clusterDataOn:$clusterDataOn){
      error
      rawData
      clusteredData
      clustersFractions
    }
  }
}
  }
`;

const GET_KMedoids_OUTPUT = gql`
  query getKMedoidsOutput( $numClusters: String!, $init:String! $randomState: String!, $datasetName:String!, $clusterDataOn:String!) {
    clusteringMethod(name:"KMedoids"){
  ...on KMedoids{
    cluster(numClusters:$numClusters init:$init randomState:$randomState datasetName:$datasetName clusterDataOn:$clusterDataOn){
      error
      rawData
      clusteredData
      clustersFractions
    }
  }
}
  }
`;

const GET_OPTICS_OUTPUT = gql`
  query getOPTICSOutput( $max_eps: String!,$minSamples:String! $algorithm: String! $datasetName:String!, $clusterDataOn:String!) {
    clusteringMethod(name:"OPTICS"){
  ...on OPTICS{
    cluster(maxEps:$max_eps minSamples:$minSamples algorithm:$algorithm datasetName:$datasetName clusterDataOn:$clusterDataOn){
      error
      rawData
      clusteredData
      clustersFractions
    }
  }
}
  }
`;

const GET_Spectral_OUTPUT = gql`
  query getSpectralOutput( $numClusters: String!,$assignLabels: String!, $affinity:String! $randomState: String!, $datasetName:String!, $clusterDataOn:String!) {
    clusteringMethod(name:"Spectral"){
  ...on Spectral{
    cluster(numClusters:$numClusters assignLabels:$assignLabels affinity:$affinity randomState:$randomState datasetName:$datasetName clusterDataOn:$clusterDataOn){
      error
      rawData
      clusteredData
      clustersFractions
    }
  }
}
  }
`;
const ADD_CONFIG = gql`
  mutation AddConfig ($name:String!, $parameters:String!, $datasetName:String!,$label:String!){
    uploadConfig(name:$name, parameters:$parameters, datasetName:$datasetName,label:$label)
	{
		name
    parameters{name value}
    datasetName 
    rawData
    clusteredData
    clustersFractions
	}
  }
`;
function RenderOutput(props: any) {
  let { clustering,configData,clusterDataOn } = props.data;
  const datasetName=configData.datasetName
  let configDataString = JSON.stringify(configData);
  const [configName, setConfigName] = useState('');
  const rawDataUrl = clustering.clusteringMethod.cluster.rawData;
  const clusteredDataUrl = clustering.clusteringMethod.cluster.clusteredData;
  const clustersFractionsUrl = clustering.clusteringMethod.cluster.clustersFractions;
  const [addConfig, { data, loading, error }] = useMutation(ADD_CONFIG);
  const downloadImage = (url: string, imageName: string) => {
    const link = document.createElement("a");
    link.download = imageName;
    link.href = url;
    link.click();
  };

  const ImageWithDownloadButton = ({
    imageUrl,
    imageName,
  }: {
    imageUrl: string;
    imageName: string;
  }) => {
    return (
      <div style={{  alignItems: "center" }}>
        <img src={imageUrl} alt={imageName} />
        <button onClick={() => downloadImage(imageUrl, imageName)}>
          Download {imageName}
        </button>
      </div>
    );
  };
  

  return (
    <div>
      <br />
      <ImageWithDownloadButton
        imageUrl={rawDataUrl}
        imageName="raw-data.png"
      />
      <br />
      <ImageWithDownloadButton
        imageUrl={clusteredDataUrl}
        imageName="clustered-data.png"
      />
      <br />
      <ImageWithDownloadButton
        imageUrl={clustersFractionsUrl}
        imageName="clusters-fractions.png"
      />
      <br />
      <label htmlFor="config-name">Enter configuration name: </label>
      <input type="text" id="config-name" name="config-name" onChange={(e) => setConfigName(e.target.value)}/><br /><br />
      <button onClick={(e:any) => {
					e.preventDefault();
					addConfig({variables:{name:configName,  parameters:configDataString, datasetName:datasetName,label:clusterDataOn}});
				}}>Save configuration</button>
    </div>
  );
}
function RenderLoading(){
  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
        <div style={{ backgroundColor: "lightgray", width: "300px", height: "100px", marginBottom: "10px" }}>Raw Data Image<br />Loading...</div>
        <div style={{ backgroundColor: "lightgray", width: "300px", height: "100px", marginBottom: "10px" }}>Clustered Data<br />Loading...</div>
        <div style={{ backgroundColor: "lightgray", width: "300px", height: "100px" }}>Cluster Fractions<br />Loading...</div>
    </div>
) 
}


function RenderKMeans(props:any){

    let configData= props.data;
    const numClusters=configData.numClusters;
    const randomState=configData.randomState;
    const datasetName=configData.datasetName;
    const clusterDataOn=configData.clusterDataOn;
    console.log("testing renderkmeans");
    console.log(props.data);
    const { loading, error, data } = useQuery(GET_KMEANS_OUTPUT, {
        variables: { numClusters,randomState ,datasetName ,clusterDataOn },
      });
    let clustering =data;
    if (loading) {
      return <RenderLoading/>
    
    }
    if (error) {
        return <div>Error</div>
    }
    
    return <RenderOutput  data={{ clustering, configData,clusterDataOn}} />

}

function RenderFuzzycmeans(props:any){

  let configData= props.data;
  const numClusters=configData.numClusters;
  const fuzzifier=configData.fuzzifier;
  const datasetName=configData.datasetName;
  const clusterDataOn=configData.clusterDataOn;
  const { loading, error, data } = useQuery(GET_FUZZYCMEANS_OUTPUT, {
      variables: { numClusters,fuzzifier ,datasetName ,clusterDataOn },
    });
  let clustering =data;
  if (loading) {
    return <RenderLoading/>
  
  }
  if (error) {
      return <div>Error</div>
  }
  
  return <RenderOutput  data={{ clustering, configData,clusterDataOn}} />

}


function RenderBirch(props:any){

  let configData= props.data;
    const numClusters=configData.numClusters;
    const datasetName=configData.datasetName;
    const clusterDataOn=configData.clusterDataOn;
    const threshold=configData.threshold;
    const branchingFactor=configData.branchingFactor
    const { loading, error, data } = useQuery(GET_Birch_OUTPUT, {
      variables: { numClusters,threshold ,branchingFactor,datasetName,clusterDataOn },
    });
    let clustering =data;
  if (loading) {
    return <RenderLoading/>
  }
  if (error) {
      return <div>Error</div>
  }
  return <RenderOutput  data={{ clustering, configData,clusterDataOn}} />
}

function RenderAgglomerative(props:any){


  let configData= props.data;
    const numClusters=configData.numClusters;
    const datasetName=configData.datasetName;
    const linkage=configData.linkage;
    const clusterDataOn=configData.clusterDataOn;
    const { loading, error, data } = useQuery(GET_Agglomerative_OUTPUT, {
        variables: { numClusters, linkage ,datasetName,clusterDataOn },
      });
      let clustering =data;
    if (loading) {
      return <RenderLoading/>
    }
    if (error) {
        return <div>Error</div>
    }
    return <RenderOutput  data={{ clustering, configData,clusterDataOn}} />

}

function RenderDBSCAN(props:any){

  let configData= props.data;
  const eps=configData.eps;
  const datasetName=configData.datasetName;
  const minSamples=configData.minSamples;
  const algorithm=configData.algorithm;
  const clusterDataOn=configData.clusterDataOn;
  const { loading, error, data } = useQuery(GET_DBSCAN_OUTPUT, {
      variables: { eps,minSamples,algorithm ,datasetName,clusterDataOn },
    });
    let clustering =data;
  if (loading) {
    return <RenderLoading/>
  }
  if (error) {
      return <div>Error</div>
  }
  return <RenderOutput  data={{ clustering, configData,clusterDataOn}} />

}

function RenderDeconvolution(props:any){

  let configData= props.data;
  const mVal=configData.mVal;
  const datasetName=configData.datasetName;
  const maxIter=configData.maxIter;
  const limit=configData.limit;
  const label=configData.label;
  const clusterDataOn=configData.clusterDataOn;
  console.log("yes working");
  console.log(mVal);
  
  const { loading, error, data } = useQuery(GET_Deconvolution_OUTPUT, {
      variables: { mVal,maxIter,limit,label ,datasetName,clusterDataOn },
    });
    let clustering =data;
  if (loading) {
    return <RenderLoading/>
  }
  if (error) {
      return <div>Error</div>
  }
  return <RenderOutput  data={{ clustering, configData,clusterDataOn}} />

}

function RenderKMedoids(props:any){

  let configData= props.data;
  const numClusters=configData.numClusters;
  const datasetName=configData.datasetName;
  const init=configData.init;
  const randomState=configData.randomState;
  const clusterDataOn=configData.clusterDataOn;
  const { loading, error, data } = useQuery(GET_KMedoids_OUTPUT, {
      variables: { numClusters,init,randomState ,datasetName,clusterDataOn },
    });

    let clustering =data;
  if (loading) {
    return <RenderLoading/>
  }
  if (error) {
      return <div>Error</div>
  }
  return <RenderOutput  data={{ clustering, configData,clusterDataOn}} />

}
function RenderOPTICS(props:any){

  let configData= props.data;
  const max_eps=configData.max_eps;
  const datasetName=configData.datasetName;
  const minSamples=configData.minSamples;
  const algorithm=configData.algorithm;
  const clusterDataOn=configData.clusterDataOn;
  const { loading, error, data } = useQuery(GET_OPTICS_OUTPUT, {
      variables: { max_eps,minSamples,algorithm ,datasetName,clusterDataOn },
    });
    let clustering =data;
  if (loading) {
    return <RenderLoading/>
  }
  if (error) {
      return <div>Error</div>
  }
  return <RenderOutput  data={{ clustering, configData,clusterDataOn}} />

}
function RenderSpectral(props:any){

  let configData= props.data;
  const numClusters=configData.numClusters;
  const datasetName=configData.datasetName;
  const assignLabels=configData.assignLabels;
  const affinity=configData.affinity;
  const randomState=configData.randomState;
  const clusterDataOn=configData.clusterDataOn;
  const { loading, error, data } = useQuery(GET_Spectral_OUTPUT, {
      variables: { numClusters,assignLabels,affinity,randomState ,datasetName,clusterDataOn },
    });
    let clustering =data;
  if (loading) {
    return <RenderLoading/>
  }
  if (error) {
      return <div>Error</div>
  }
  return <RenderOutput  data={{ clustering, configData,clusterDataOn}} />

}

function ClusterOutput(props:any){
    let url = window.location.href;
	let start = url.lastIndexOf(':-');
    let snippedUrl = url.substring(start+2);
    let end = snippedUrl.indexOf('/');
	let datasetName =snippedUrl.substring(0, end)
    let formData=props.fdata;
    let clusterName=props.cname;
    let clusterDataOn = formData.selectedClusterDataOn;
    
    
    const classes = useStyles();
    if (clusterName==="KMeans") {
        let numClusters=formData.num_clusters;
        let randomState=formData.random_state;
        console.log("testing clusteroutput");
        console.log(formData);
        return <RenderKMeans  data={{ numClusters,randomState,datasetName,clusterDataOn}} />
    }
    else if (clusterName==="Fuzzycmeans") {
      let numClusters=formData.num_clusters;
      let fuzzifier=formData.fuzzifier;
      return <RenderFuzzycmeans  data={{ numClusters,fuzzifier,datasetName,clusterDataOn}} />
  }
    else if (clusterName==="Birch") {
        let numClusters=formData.num_clusters;
        let threshold=formData.threshold;
        let branchingFactor=formData.branching_factor;
        return <RenderBirch  data={{ numClusters,threshold,branchingFactor,datasetName,clusterDataOn}} />
    }
    else if (clusterName==="Agglomerative") {
      let numClusters=formData.num_clusters;
      let linkage=formData.linkage;
      return <RenderAgglomerative  data={{ numClusters,linkage,datasetName,clusterDataOn}} />
  }
  
  else if (clusterName==="DBSCAN") {
    let eps=formData.eps;
    let minSamples=formData.min_samples;
    let algorithm=formData.algorithm;
    return <RenderDBSCAN  data={{ eps,minSamples,algorithm ,datasetName,clusterDataOn}} />
}
else if (clusterName==="Deconvolution") {
  
  
  let mVal=formData.m_val;
  let maxIter=formData.max_iter;
  let limit=formData.limit;
  return <RenderDeconvolution  data={{ mVal,maxIter,limit ,datasetName,clusterDataOn}} />
}
  else if (clusterName==="KMedoids") {
    let numClusters=formData.num_clusters;
    let randomState=formData.random_state;
    let init=formData.init;
    return <RenderKMedoids  data={{ numClusters,init,randomState,datasetName,clusterDataOn}} />
}
else if (clusterName==="OPTICS") {
  let max_eps=formData.max_eps;
    let minSamples=formData.min_samples;
    let algorithm=formData.algorithm;
    return <RenderOPTICS  data={{ max_eps,minSamples,algorithm ,datasetName,clusterDataOn}} />
}
else if (clusterName==="Spectral") {
  let numClusters=formData.num_clusters;
  let randomState=formData.random_state;
  let affinity=formData.affinity;
  let assignLabels=formData.assign_labels;
  return <RenderSpectral  data={{ numClusters, assignLabels, affinity,randomState,datasetName,clusterDataOn}} />
}
    else{
        return(
            <div>
                yet to be added
            </div>
        )
    }
    

}

ClusterOutput.defaultProps = {
	data: {num_clusters: '0', random_state: '0'}
  };

export default memo(ClusterOutput);