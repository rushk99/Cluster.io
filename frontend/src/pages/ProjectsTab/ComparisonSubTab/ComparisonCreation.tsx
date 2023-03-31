import React, { Children } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Box, Button} from '@material-ui/core';
import { Add} from '@material-ui/icons';





///////////////////////////////////////////////////////////////
//            CSS
///////////////////////////////////////////////////////////////
const useStyles = makeStyles(theme => ({
	//Title, the top of the side bar where the project name is
	window: {
		width: 400,
		height: 300,
		marginLeft: 250,
		marginTop: 100,
		backgroundColor: '#C9D9D2' 
	},
	createButton: {
		marginTop: 150
	},
	text: {
		paddingTop: 15
	}
}));

const ComparisonCreation = () => {
	///////////////////////////////////
	///  Inner Handlers
	///////////////////////////////////
	const [open, setOpen] = React.useState(true);
	const classes = useStyles();

	//Expands main tabs(shows file name)
	
	const handleCreationClick = () => {
		console.log("works");
	};
    


	////////////////////////////////////////////////////
	//                HTML
	/////////////////////////////////////////////////
	return (
		<div>
			<Box borderRadius="30px" className={classes.window}>
				<h1 className={classes.text}>Create New Comparison</h1>
				<Button variant="contained" size="large" endIcon={<Add />} 
				className={classes.createButton} onClick={() => { handleCreationClick() }}>
					New
				</Button>
			</Box>
		</div>
	);
};

export default ComparisonCreation;