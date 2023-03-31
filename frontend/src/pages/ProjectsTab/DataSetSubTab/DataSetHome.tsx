import React, { Children } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import DataSetUpload from './DataSetUpload';
import DataSetTable from './DataSetTable';


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
		marginLeft: getWidth()*(.5)
	  },
}));

const DataSetHome = () => {
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
                <DataSetUpload />
		    </div>
		    <div className={classes.rightSide} > 
			<DataSetTable />
		    </div>
		</div>
	);
};

export default DataSetHome;