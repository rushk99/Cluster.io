import React, { Children } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Box, Button, ListItem, ListItemText } from '@material-ui/core';
import { ArrowBack, ArrowForward } from '@material-ui/icons';
import { classicNameResolver } from 'typescript';
import { gql, useQuery } from "@apollo/client";
const GET_CLUSTER_OUTPUT = gql`
  query getClusterOutput($clusterName: String!) {
    config(name: $clusterName) {
		rawData clusteredData clustersFractions 
    }
  }
`;

let imageIndex = 0;

function GetImage({clusterName}:any){
    const { loading, error, data } = useQuery(GET_CLUSTER_OUTPUT, {
        variables: { clusterName },
    });
    if (loading) {
        return "loading"
    }
    if (error){
        return "error"
    }
    if(imageIndex == 0){
        return data.config.rawData;
    }else if(imageIndex == 1){
        return data.config.clusteredData;
    }else{
        return data.config.clustersFractions;
    }
}

///////////////////////////////////////////////////////////////
//            CSS
///////////////////////////////////////////////////////////////
const useStyles = makeStyles(theme => ({
	//Title, the top of the side bar where the project name is
    image: {
        width: '45%',
        marginLeft: '20%'
    },
    leftSide: {
		width: '5%',
        marginTop: '5%',
        marginLeft: '40%',
		float: 'left'
	  },
	rightSide: {
        marginTop: '5%'
	  },
    
}));

const ClusterGraphs = ({clusterName}:any) => {
	///////////////////////////////////
	///  Inner Handlers
	///////////////////////////////////
	
    const classes = useStyles();
	const [open, setOpen] = React.useState(true);
    

    const imageBack = () => {
        //adding 5 bc it was acting wierd with negative numbers
        imageIndex = (imageIndex + 5)%3;
		setOpen(!open);
    }

    const imageForward = () => {
        imageIndex = (imageIndex + 1)%3;
		setOpen(!open);
    }


	////////////////////////////////////////////////////
	//                HTML
	/////////////////////////////////////////////////
	return (
		<div>
			<img src={GetImage({clusterName})} className={classes.image} />
			<br />
            <Button className={classes.leftSide} onClick={() => {imageBack()}}> 
                <ArrowBack  fontSize='large' />
		    </Button>
		    <Button className={classes.rightSide}  onClick={() => {imageForward()}} > 
                <ArrowForward fontSize='large' />
		    </Button>
		</div>
	);
};

export default ClusterGraphs;