import React, { Children } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Box, Button, ListItem, ListItemText } from '@material-ui/core';


const projectNames = ["DDMS", "Clustering", "Other"];
let selectedProject = -1;

//TODO atach to backend
function getProjectNames() {
	return projectNames;
}




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
	projectName: {
		backgroundColor: "white",
		outlineColor: 'black',
		outlineWidth: '2px',
		outlineStyle: 'solid'
	},
	viewButton: {
		float: 'right',
		marginTop: 30,
		marginRight: 350
	}
}));

const ProjectTable = () => {
	///////////////////////////////////
	///  Inner Handlers
	///////////////////////////////////
	
	const [open, setOpen] = React.useState(true);
	const classes = useStyles();
	


	//Expands main tabs(shows file name)
	
	const selectProject = (text: String, index: number) => {
		selectedProject = index;
		console.log("selectedComparison");
		setOpen(!open);
	};

    const viewProject = () => {
		console.log("cluster");
	}


	////////////////////////////////////////////////////
	//                HTML
	/////////////////////////////////////////////////
	return (
		<div>
			<Box className={classes.table}>
				<ListItem className={classes.title}>
					<ListItemText disableTypography primary={"Existing Projects"} />
				</ListItem>
					{getProjectNames().map((text, index) => (
						<div>
							<ListItem button selected = {selectedProject == index}
							key={text} className={classes.projectName} onClick={() => { selectProject(text, index) }}>
								<ListItemText primary={text} />
							</ListItem>
						</ div>
					))}
			</Box>
			<a href={"/Project/"+projectNames[selectedProject]+"/DataSet/Home"}>
			<Button variant="contained" disabled={selectedProject==-1} size="large" className={classes.viewButton}
			onClick={() => { viewProject() }}>
				
					View Project
					
			</Button>
			</a>
		</div>
	);
};

export default ProjectTable;