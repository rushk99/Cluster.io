import React, { Children } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Box, Button, ListItem, ListItemText, Paper } from '@material-ui/core';
import { CheckBoxOutlineBlank, CheckBox } from '@material-ui/icons';
import { useHistory } from "react-router-dom";
import ClusterDataRow from './ClusterDataRow';
import { gql, useQuery } from "@apollo/client";
const GET_CLUSTER_DATASET = gql`
  query getClusterdATASET($clusterName: String!) {
    clusteredDataset(name: $clusterName) {
		x y labeldata cluster 
    }
  }
`;
const GET_CLUSTER_LABEL_NAME = gql`
  query getClusterLabelName($clusterName: String!) {
    config(name: $clusterName) {
		label 
    }
  }
`;

///////////////////////////////////////////////////////////////
//            CSS
///////////////////////////////////////////////////////////////
const useStyles = makeStyles(theme => ({
	//Title, the top of the side bar where the project name is
	table: {
		width: 400,
		marginRight: 250,
		float: 'right'
	},
	title: {
		backgroundColor: '#C9D9D2',
		outlineColor: 'black',
		outlineWidth: '2px',
		outlineStyle: 'solid',
		marginLeft: '3px',
		width: '100%', 
		position: 'relative',
		zIndex: 1
	},
	outlined: {
		outlineColor: 'black',
		outlineWidth: '2px',
		outlineStyle: 'solid'
	},
	projectName: {
		backgroundColor: "white",
		outlineColor: 'black',
		outlineWidth: '2px',
		outlineStyle: 'solid'
	},
	viewButton: {
		float: 'right',
		marginTop: 30,
		marginRight: 350
	},
	paperStyle: {
		maxHeight: 350, 
		zIndex: -1, 
		overflow: 'auto', 
		width: '416.5px', 
		paddingRight: 5, 
		paddingLeft: 3 
	}
	
}));
const ClusterDataTable = ({clusterName}:any) => {
	///////////////////////////////////
	///  Inner Handlers
	///////////////////////////////////
	
	
	const [open, setOpen] = React.useState(true);
	const classes = useStyles();

	const handelDownload = () => {


	}

	const getLeftText = (row: any) => {
		return "(" + row[0] + ", " + row[1] + ")";

	}
	const getMidText = (row: any) => {
		return row[2].toString();
	}
	const getRightText = (row: any) => {
		return row[3].toString();
	}
	const { loading, error, data } = useQuery(GET_CLUSTER_DATASET, {
        variables: { clusterName },
    });
	const { data: labeldata, loading: labelloading, error: labelerror }=useQuery(GET_CLUSTER_LABEL_NAME,{variables: { clusterName }});
	if (labelloading) {
        return <div>"loading"</div>
    }
    if (labelerror){
		return <div>"error"</div>
    }
	
	const label= labeldata.config.label;
	
	if (loading) {
        return <div>"loading"</div>
    }
    if (error){
		return <div>"error"</div>
    }
	const dataset: Array<[number, number,number, number]> = [];

	data.clusteredDataset.forEach((item:any) => {
	const { x, y,labeldata, cluster } = item;
	dataset.push([x, y,labeldata, cluster]);
	});
	////////////////////////////////////////////////////
	//                HTML
	/////////////////////////////////////////////////
	return (
		<div>
			<Box className={classes.table}>
				<ListItem className={classes.title}>
					<ListItemText disableTypography primary={"Data"} />
				</ListItem>
				<div className={classes.title}>
					<ClusterDataRow leftText={'X Cord(um), Y Cord(um)'} midText={label} rightText={'Cluster'} />
				</div>
				<Paper className={classes.paperStyle}>
					<div className={classes.outlined}>
						{dataset.map((row, index) => (
							<ClusterDataRow leftText={getLeftText(row)} midText={getMidText(row)} rightText={getRightText(row)} />
						))}
					</div>
				</Paper>
			</Box>
			<Button variant="contained" size="large" className={classes.viewButton}
				onClick={() => { handelDownload() }}>

				Download

			</Button>
		</div>
	);
};

export default ClusterDataTable;