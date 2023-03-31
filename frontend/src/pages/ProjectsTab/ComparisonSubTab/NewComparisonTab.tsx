import React, { Children } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import ComparisonCreation from './ComparisonCreation';
import ComparisonTable from './ComparisonTable';
import ClusterTable from '../ClusterSubTab/ClusterTable';
import ComparisonMethodSelect from './ComparisonMethodSelect';

function getHeight(){
	return 600;
}

function getWidth(){
	return 1500;
}


///////////////////////////////////////////////////////////////
//            CSS
///////////////////////////////////////////////////////////////
const useStyles = makeStyles(theme => ({
	//Title, the top of the side bar where the project name is
	leftSide: {
		width: getWidth()*.5,
		float: 'left'
	  },
	middle: {
		marginLeft: getWidth()*(.5)
	  },
}));

const NewComparisonCreation = () => {
	///////////////////////////////////
	///  Inner Handlers
	///////////////////////////////////
	const [open, setOpen] = React.useState(true);
	const classes = useStyles();
	
	

	//Expands main tabs(shows file name)
	/*
	const handleExpandTab = (index: number) => {


		tabsEnabled[index] = !tabsEnabled[index];
		setOpen(!open);
	};
    */


	////////////////////////////////////////////////////
	//                HTML
	/////////////////////////////////////////////////
	return (
		<div>
		    <div className={classes.middle} > 
			    <ComparisonMethodSelect />
		    </div>
		</div>
	);
};

export default NewComparisonCreation;