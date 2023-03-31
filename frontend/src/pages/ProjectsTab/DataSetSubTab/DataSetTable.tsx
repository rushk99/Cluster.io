import React, { Children } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Box, Button, ListItem, ListItemText } from '@material-ui/core';
import { gql, useQuery, useMutation } from "@apollo/client";


let selectedFile = -1;
let selectedFileName: String="";

const DELETE_DATA = gql`
  mutation DeleteData ($name:String!){
    deleteDataset(name: $name)
  }
`;

const GET_DATA = gql`
	{
	datasets{
	  name
	  fileName
	  description
	  url
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
		float: 'right',
		marginTop: 50
	},
	title: {
		backgroundColor: '#C9D9D2',
		outlineColor: 'black',
		outlineWidth: '2px',
		outlineStyle: 'solid'
	},
	fileName: {
		backgroundColor: "white",
		outlineColor: 'black',
		outlineWidth: '2px',
		outlineStyle: 'solid'
	},
	clusterButton: {
		float: 'right',
		marginTop: 400,
		marginRight: 30
	}
}));

const DataSetTable = () => {
	///////////////////////////////////
	///  Inner Handlers
	///////////////////////////////////
	let url = window.location.href;
	let start = url.lastIndexOf('Project/');
    let snippedUrl = url.substring(start+8);
    let end = snippedUrl.indexOf('/');
	let projectName =snippedUrl.substring(0, end)
	console.log(url);
	const [open, setOpen] = React.useState(true);
	const classes = useStyles();
	const getData = useQuery(GET_DATA);
	const [deleteData, { data, loading, error }] = useMutation(DELETE_DATA);
	if (getData.loading){
		return <div>loading...</div>
	}
	if (getData.error){
		return <div>error...</div>
	}
	//Expands main tabs(shows file name)
	
	const selectDataSet = (text: String, index: number) => {
		selectedFile = index;
		selectedFileName=text;
		setOpen(!open);
	};

	const clusterData = () => {
		console.log("cluster");
	}
    


	////////////////////////////////////////////////////
	//                HTML
	/////////////////////////////////////////////////
	return (
		<div>
			<Box className={classes.table}>
				<ListItem key="title" className={classes.title}>
					<ListItemText disableTypography primary={"Existing Data Sets"} />
				</ListItem>
					{getData.data.datasets.map((dataset:any ,index:any ) => (
						<div>
							<ListItem button selected={selectedFile==index} 
							key={dataset.name} className={classes.fileName} onClick={() => { selectDataSet(dataset.name, index) }}>
								<ListItemText primary={dataset.name} />
							</ListItem>
						</ div>
					))}
			</Box>
			<a href={"/Project/"+projectName+":-"+selectedFileName+"/Cluster/Home"}>
			<Button variant="contained" disabled={selectedFile==-1} size="large" className={classes.clusterButton}
			onClick={() => { clusterData() }}>
				
					Perform Cluster
					
			</Button>
			</a>
			<Button variant="contained" disabled={selectedFile==-1} size="large" className={classes.clusterButton}
			onClick={(e:any) => {
				e.preventDefault();
				deleteData({variables:{name:selectedFileName}});
			}}>
				
					Delete Dataset
					
			</Button>
		</div>
	);
};

export default DataSetTable;