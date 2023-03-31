import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { classicNameResolver } from 'typescript';
import ProjectTopbar from './ProjectTopbar';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import DataSetHome from './DataSetSubTab/DataSetHome';
import ClusterHome from './ClusterSubTab/ClusterHome';
import ComparisonHome from './ComparisonSubTab/ComparisonHome';
import ClusterView from './ClusterSubTab/ClusterView';
import NewComparisonCreation from './ComparisonSubTab/NewComparisonTab'

//THe percentage the sidebar should take up
const sidebarAproxHeight = .1

function getProjectName():String{
	let url = window.location.href;
	let start = url.lastIndexOf('Project/');
	let snippedUrl = url.substring(start+8);
	let end = snippedUrl.indexOf('/');

	return snippedUrl.substring(0, end);
}


function getClusterName():String{
	let url = window.location.href;
	let start = url.lastIndexOf('/Cluster/');
	if(start==-1){
		return "not a cluster tab";
	}
	let snippedUrl = url.substring(start+9);
	let end = snippedUrl.indexOf('/view');
	return decodeURIComponent(snippedUrl.substring(0, end));
}


const useStyles = makeStyles((theme) => ({
	topbar: {
		height: 60,
	}
}));

const NewProject = () => {
	const classes = useStyles();
	return (
		<div>
			<div className={classes.topbar} onClick={()=>{getProjectName()}} >
				<ProjectTopbar projName={ getProjectName()} />
			</div>
			<div >
				<Switch>
					<Route path={'/Project/'+getProjectName()+'/DataSet/Home'} component={DataSetHome} />
					<Route path={'/Project/'+getProjectName()+'/Cluster/Home'} component={ClusterHome} />
					<Route path={'/Project/'+getProjectName()+'/Comparison/Home'} component={ComparisonHome} />
					<Route path={'/Project/'+getProjectName()+'/Comparison/New'} component={NewComparisonCreation} />
					<Route path={'/Project/'+getProjectName()+'/Cluster/'+getClusterName()+'/view'} component={ClusterView} />
				</Switch>
			</div>
		</div>
	);
};


export default NewProject;
