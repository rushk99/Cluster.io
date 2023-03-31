import React, { Children } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Box, Button, ListItem, ListItemText } from '@material-ui/core';
import { CheckBoxOutlineBlank, CheckBox } from '@material-ui/icons';
import { Switch, useHistory } from "react-router-dom";
import { gql, useQuery, useMutation } from "@apollo/client";


let clusterSelected = [false, false,false,false, false, false, false, false, false, false, false, false];
let numSelected = 0;
let selectedFileName: string="";
let selectedFileNames: string[] = [];
let displayButton = true;
const DELETE_CONFIG = gql`
  mutation DeleteConfig ($name:String!){
    deleteConfig(name: $name)
  }
`;
const GET_CONFIG = gql`
	{configs{name}}
  `;

function getClusterSelected() {
	return clusterSelected;
}





///////////////////////////////////////////////////////////////
//            CSS
///////////////////////////////////////////////////////////////
const useStyles = makeStyles(theme => ({
	//Title, the top of the side bar where the project name is
	table: {
		width: 400,
		marginRight: 250,
		float: 'right',
		marginTop: 50
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
	}
}));

const ClusterTable = () => {
	///////////////////////////////////
	///  Inner Handlers
	///////////////////////////////////
	
	const init = () => {
		const pathname = window.location.pathname;
		if(pathname.indexOf('/Cluster') == -1){
			displayButton = false;
		}else{
			displayButton = true;
		}
	};

	let history = useHistory();
	const [open, setOpen] = React.useState(true);
	const classes = useStyles();
	init();


	//Expands main tabs(shows file name)


	const selectCluster = (text: string, index: number) => {
		clusterSelected[index] = !clusterSelected[index];
		if (clusterSelected[index]){
			numSelected = numSelected + 1;
			selectedFileName=text;
			selectedFileNames.push(text);
		}else{
			numSelected = numSelected -1;
			selectedFileNames = selectedFileNames.filter(name => name !== text);
		}
		setOpen(!open);
	};

	const viewCluster = (text: String, index: number) => {
		const pathname = window.location.pathname;
		history.push(pathname.substring(0, pathname.lastIndexOf('/')+1) + text + "/view");
	};

	const compareClusters = () => {
		const selectedFileNamesQueryParam = encodeURIComponent(JSON.stringify(selectedFileNames));
		const pathname = window.location.pathname;
		let url = pathname.substring(0, pathname.lastIndexOf('/Cluster')) + "/Comparison/New?selectedFileNames=" + selectedFileNamesQueryParam;
		history.push(url);
	  };
    
	const [deleteConfig, { data, loading, error }] = useMutation(DELETE_CONFIG);
	const getConfig = useQuery(GET_CONFIG);
	if (getConfig.loading){
		return <div>loading...</div>
	}
	if (getConfig.error){
		return <div>error...</div>
	}
	////////////////////////////////////////////////////
	//                HTML
	//onClick={() => { selectCluster(text, index) }}
	/////////////////////////////////////////////////
	return (
		<div>
			<Box className={classes.table}>
				<ListItem key="title" className={classes.title}>
					<ListItemText disableTypography primary={"Existing Cluster Configurations"} />
				</ListItem>
					{getConfig.data.configs.map((config:any, index:any) => (
						<div>
							<ListItem button 
							key={config.name} className={classes.clusterName} onDoubleClick = {() => { viewCluster(config.name, index) }} onClick={() => { selectCluster(config.name, index) }}>
								<ListItemText primary={config.name} />
								{getClusterSelected()[index] ? <CheckBox /> : <CheckBoxOutlineBlank />}
							</ListItem>
						</ div>
					))}
			{displayButton ? 
			<Button style={{display: 'flex'}} variant="contained" disabled={numSelected<2} size="large" className={classes.compareButton}
			onClick={() => { compareClusters() }}>
				Compare Clusters
			</Button> : <br></br>}
			{displayButton ? 
			<Button style={{display: 'flex'}} variant="contained" disabled={numSelected!==1} size="large" className={classes.compareButton}
			onClick={(e:any) => { e.preventDefault();
				deleteConfig({variables:{name:selectedFileName}}); }}>
				Delete Cluster
			</Button> : <br></br>}
			</Box>
			
			
		</div>
	);
};

export default ClusterTable;
