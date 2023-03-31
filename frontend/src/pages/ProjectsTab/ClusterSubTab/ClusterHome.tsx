import React, { Children } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import ClusterCreate from './ClusterCreate';
import ClusterTable from './ClusterTable';


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
	rightSide: {
		marginLeft: getWidth()*(.5),
		backgroundColor: 'yellow' 
	  },
}));

const ClusterHome = () => {
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
                <ClusterCreate />
		    </div>
		    <div className={classes.rightSide} > 
			    <ClusterTable />
		    </div>
		</div>
	);
};

export default ClusterHome;