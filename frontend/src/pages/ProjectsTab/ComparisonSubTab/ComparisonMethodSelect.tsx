import React, { Children, useContext } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Box, Button, FormControl, InputLabel, MenuItem, Select } from '@material-ui/core';
import { Add } from '@material-ui/icons';
import ClusterTable from '../ClusterSubTab/ClusterTable';
import { gql, useQuery } from "@apollo/client";
import ComparisonOutput from './ComparisonOutput';
let method = "";




///////////////////////////////////////////////////////////////
//            CSS
///////////////////////////////////////////////////////////////
const useStyles = makeStyles(theme => ({
	//Title, the top of the side bar where the project name is
	window: {
		width: 600,
		height: 600,
		marginLeft: 50,
		marginTop: 100,
		backgroundColor: '#C9D9D2' 
	},
	createButton: {
		marginTop: 100
	},
	text: {
		paddingTop: 15
	},
	dropDown: {
		width: 300
	}
}));

const ComparisonMethodSelect = () => {
	///////////////////////////////////
	///  Inner Handlers
	///////////////////////////////////
	const [open, setOpen] = React.useState(true);
	const classes = useStyles();
	const [showDiv2, setShowDiv2] = React.useState(false);
	//Expands main tabs(shows file name)
	
	const handleComparisonClick = () => {
		setShowDiv2(true);
	};

    const handleComparisonMethodChange = (event: any) => {
        method = event.target.value;
	};
    
	const query = new URLSearchParams(window.location.search);
	const selectedFileNamesQueryParam = query.get("selectedFileNames");
	const selectedFileNames = JSON.parse(decodeURIComponent(selectedFileNamesQueryParam??""));
	const fileNamesString = selectedFileNames.map((name :any) => `${name}`).join(",");
	
	

	////////////////////////////////////////////////////
	//                HTML
	/////////////////////////////////////////////////
	return (
		<div>
			<Box borderRadius="30px" className={classes.window}>
			<h1 >
        Select Comparison Method for: <br />
        {selectedFileNames.map((fileName:any, index:any) => (
          <span key={fileName}>
            <h6>{(index + 1)}. {fileName} <br /></h6>
          </span>
        ))}
      </h1>


                <FormControl className={classes.dropDown}>
                    <InputLabel id="dropdownLabel">Comparison Method</InputLabel>
                    <Select labelId="dropdownLabel" onChange={handleComparisonMethodChange}>
                        <MenuItem value={"calinski_harabasz_score"}>Calinski Harabasz Score</MenuItem>
                        <MenuItem value={"davies_bouldin_score"}>Davies Bouldin Score</MenuItem>
                        <MenuItem value={"silhouette_score"}>Silhouette Score</MenuItem>
                    </Select>
                </FormControl>


                <br></br>
				<Button variant="contained" size="large"
				className={classes.createButton} onClick={() => { handleComparisonClick() }}>
					Compare
				</Button>
			</Box>
			{showDiv2&&(<div>
					
					
					<ComparisonOutput data={{ fileNamesString, method}} />
					
				</div>)}
		</div>
	);
};

export default ComparisonMethodSelect;