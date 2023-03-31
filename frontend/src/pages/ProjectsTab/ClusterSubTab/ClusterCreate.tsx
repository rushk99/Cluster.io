import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Box, Button } from '@material-ui/core';
import { Add } from '@material-ui/icons';
import { gql, useQuery } from "@apollo/client";
import { Console } from 'console';
import ClusterConfig from './ClusterConfig';

///////////////////////////////////////////////////////////////
//            CSS
///////////////////////////////////////////////////////////////
const useStyles = makeStyles(theme => ({
	window: {
	  marginLeft: 250,
	  marginTop: 100,
	  backgroundColor: '#C9D9D2',
	  padding: 30,
	  borderRadius: 30,
	  boxShadow: '0px 4px 4px rgba(0, 0, 0, 0.25)',
	},
	title: {
	  fontSize: 28,
	  fontWeight: 'bold',
	  marginBottom: 20,
	},
	dropDown: {
	  display: "flex",
	  justifyContent:'center',
	  alignItems:'center', 
	  marginBottom:20
	},
	select: {
	  width: '100%',
	  padding: '10px 20px',
	  border: 'none',
	  borderRadius: 10,
	  backgroundColor: '#F5F5F5',
	  outline: 'none',
	  cursor: 'pointer',
	  fontSize: 16,
	  fontWeight: 'bold',
	},
	selectOption: {
	  padding: 10,
	},
  }));

const GET_CLUSTER = gql`
	query{clusteringMethods{name}}
  `;


const ClusterCreate = () => {
	///////////////////////////////////
	///  Inner Handlers
	///////////////////////////////////
	const classes = useStyles();
  	const [selectedOption, setSelectedOption] = useState("");
	//Expands main tabs(shows file name)
	const getCluster = useQuery(GET_CLUSTER);
	const [showDiv1, setShowDiv1] = useState(true);
	const [showDiv2, setShowDiv2] = useState(false);
	if (getCluster.loading){
		return <div>loading...</div>
	}
	if (getCluster.error){
		return <div>error...</div>
	}
	


	////////////////////////////////////////////////////
	//                HTML
	/////////////////////////////////////////////////
	return (
		<div>
		  <Box display="flex" flexWrap="wrap" className={classes.window}>
			<div>
			  <h1 className={classes.title}>Create a New Cluster Configuration</h1>
			  <div className={classes.dropDown}>
				<select value={selectedOption} className={classes.select} onChange={(e) => { setSelectedOption(e.target.value);
																				setShowDiv2(true); }}>
				  <option value="" disabled>--Select a Clustering Algorithm--</option>
				  {getCluster.data.clusteringMethods.map((cluster:any) => (
					<option key={cluster.name} value={cluster.name} className={classes.selectOption}>
					  {cluster.name}
					</option>
				  ))}
				</select>
			  </div>
			</div>
		  </Box>
		  {showDiv2&&(<div>
			<ClusterConfig clusterName={selectedOption} />
		  </div>)}
		</div>
	  );
};

export default ClusterCreate;