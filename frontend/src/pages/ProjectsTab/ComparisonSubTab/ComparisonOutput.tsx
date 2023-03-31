import React, { Children, useContext, useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Box, Button, ListItem, ListItemText,FormControl, InputLabel, MenuItem, Select } from '@material-ui/core';
import { Add } from '@material-ui/icons';
import { gql, useQuery } from "@apollo/client";



const useStyles = makeStyles(theme => ({
	//Title, the top of the side bar where the project name is
	table: {
		width: 600,
		marginRight: 1050,
		float: 'right',
		marginTop: 50,
        marginBottom: 50
	},
	title: {
		backgroundColor: '#C9D9D2',
		outlineColor: 'black',
		outlineWidth: '2px',
		outlineStyle: 'solid'
	},
	clusterName: {
		backgroundColor: "white",
		outlineColor: 'black',
		outlineWidth: '2px',
		outlineStyle: 'solid'
	},
	compareButton: {
		float: 'right',
		marginTop: 30,
		marginRight: 100
	},
    hr:{
        margin: "16px 0",
        padding: 0,
        border: 0,
        borderTop: "3px solid #ccc"
    }
}));

const GET_CLUSTER_COMPARISON = gql`
  query getClustercOMPARISON($fileNamesString: String!,$method:String ) {
    clusterComparisons(list: $fileNamesString,metric:$method) {
		clustername metric score 
    }
  }
`;
const GET_CLUSTERED_DATA_URL = gql`
  query getClusteredDataURL( $clustername: String!) {
    config(name:$clustername){
      clusteredData
    
}
  }
`;
function ImageFromConfigName(props: any) {
    const classes = useStyles();
    let  clustername  = props.name;
        
    
    
    const { loading, error, data } = useQuery(GET_CLUSTERED_DATA_URL, {
        variables: { clustername },
    });
    
    
    
    if (loading) {
        return <div>loading...</div>
    }
    if (error){
        return <div>error...</div>
    
    }
    const imageUrl=data.config.clusteredData;
    return <div><img src={imageUrl} alt="clustered-data.png" /></div>}


function ComparisonOutput(props: any) {
    const classes = useStyles();
    let { fileNamesString,method } = props.data;
        
    
    const { loading, error, data } = useQuery(GET_CLUSTER_COMPARISON, {
        variables: { fileNamesString,method },
    });
      
    if (loading) {
        return <div>loading...</div>
    }
    if (error){
        return <div>error...</div>
    }
    
    return <div><Box className={classes.table}>
        <ListItem key="title" className={classes.title}>
            <ListItemText disableTypography primary={"Comparison Results"} />
        </ListItem>
            {data.clusterComparisons.map((clusterComparison:any, index:any) => (
                <div>
                    
                    <ListItem  
                    key={clusterComparison.clustername} className={classes.clusterName} >
                        <ListItemText primary={`${index + 1}) ${clusterComparison.clustername}`} />
                        
                    </ListItem>
                    <ListItem  
                    key={clusterComparison.clustername} className={classes.clusterName} >
                        <ImageFromConfigName
                        name={clusterComparison.clustername}
                    />
                        
                    </ListItem>
                    <ListItem key={`${clusterComparison.metric}-${clusterComparison.score}`} className={classes.clusterName}>
                        <ListItemText primary={`${clusterComparison.metric}:- ${clusterComparison.score}`} />
                    </ListItem>
                    <hr className={classes.hr} />
                </ div>
            ))}
</Box></div>
    }



export default ComparisonOutput;