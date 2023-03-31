import React, { Children } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Box, Button, ListItem, ListItemText } from '@material-ui/core';
import { CheckBoxOutlineBlank, CheckBox } from '@material-ui/icons';
import { useHistory } from "react-router-dom";
import ClusterGraphs from'./ClusterGraphs';
import ClusterDataTable from'./ClusterDataTable';





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
		float: 'left',
        marginTop: '0px',
        paddingTop: '0px'
	  },
	rightSide: {
		marginLeft: getWidth()*(.5)
	  },
      clusterName: {
		marginBotom: '0px',
        paddingBottom: '0px'
	  }
}));

const ClusterView = () => {
	///////////////////////////////////
	///  Inner Handlers
	///////////////////////////////////
	
    
	const [open, setOpen] = React.useState(true);
	const classes = useStyles();
	
	let url = window.location.href;
    let start = url.lastIndexOf('/Cluster/');
    let snippedUrl = url.substring(start + 9);
    let end = snippedUrl.indexOf('/view');
	let clusterName=decodeURIComponent(snippedUrl.substring(0, end));

	////////////////////////////////////////////////////
	//                HTML
	/////////////////////////////////////////////////
	return (
		<div>
			<h3 className={classes.clusterName}>Cluster Config Name :- {clusterName}</h3>
           
            <div className={classes.leftSide} > 
                <ClusterGraphs clusterName={clusterName} />
		    </div>
		    <div className={classes.rightSide} > 
			    <ClusterDataTable clusterName={clusterName} />
		    </div>
		</div>
	);
};

export default ClusterView;