import React, { Children } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Box, Button} from '@material-ui/core';
import { Add} from '@material-ui/icons';
import logo from "./logo.svg";
import { gql, useQuery } from "@apollo/client";
import { MenuItem } from "@material-ui/core";
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import NewProject from "./NewProject"

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

const ProjectCreation = () => {
	///////////////////////////////////
	///  Inner Handlers
	///////////////////////////////////
	const [open, setOpen] = React.useState(true);
	const classes = useStyles();
	
	function handleCreationClick():String {
		console.log("handleCreationClick");
		let url = window.location.href;
        let start = url.lastIndexOf('Project/');
        let snippedUrl = url.substring(start+8);
        let end = snippedUrl.indexOf('/');
        console.log(snippedUrl.substring(0, end));

        return "NewProject";
	}

	////////////////////////////////////////////////////
	//                HTML
	/////////////////////////////////////////////////
    return (
        <div>
            <Box borderRadius="30px" className={classes.window}>
                <h1 className={classes.text}>Create New Project</h1>
                <a href={"/NewProject"}>
                    <Button variant="contained" size="large" endIcon={<Add />}
                    className={classes.createButton} onClick={() => { handleCreationClick() }}>
                        New
                    </Button>
                </a>
            </Box>
        </div>
    );

};

export default ProjectCreation;