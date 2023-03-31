import React, { Children } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import ProjectCreation from './ProjectCreation';
import ProjectTable from './ProjectTable';

function getHeight(){
	return 700;
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
	rightSide: {
		marginLeft: getWidth()*(.5)
	  },
}));

const OpenProject = () => {
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
			<div className={classes.leftSide} > 
                <ProjectCreation />
		    </div>
		    <div className={classes.rightSide} > 
			    <ProjectTable />
		    </div>
		</div>
	);
};

export default OpenProject;
