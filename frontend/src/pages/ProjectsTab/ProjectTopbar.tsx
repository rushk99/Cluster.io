import {ArrowRightAlt} from '@material-ui/icons';
import {
Nav,
NavLink,
NavMenu
} from './TopbarElements';

const ProjectTopbar = (props: { projName: String } ) => {
	const isCluster = () => {
		return window.location.pathname.indexOf('/Cluster/') != -1;
	};

	const isDataSet = () => {
		return window.location.pathname.indexOf('/DataSet/') != -1;
	};

	const isComparison = () => {
		return window.location.pathname.indexOf('/Comparison/') != -1;
	};

return (
	<>
	<Nav>
		<h1 style={{marginTop: "10px", marginLeft: "20px", width: "250px", textAlign: "left"}}>{props.projName}</h1>
		<NavMenu style={{ marginLeft: "0px" }}>
		<NavLink to={'/Project/'+props.projName+'/DataSet/Home'} isActive={() => isDataSet()} activeStyle={{ background: '#EEFFFF' }}>
        {/* activeStyle */}
			Data Sets/Upload
		</NavLink>
		<ArrowRightAlt />
		<NavLink to={'/Project/'+props.projName+'/Cluster/Home'} isActive={() => isCluster()} activeStyle={{ background: '#EEFFFF' }} >
        {/* activeStyle */}
			Cluster Configuations
		</NavLink>
		<ArrowRightAlt />
        <NavLink to={'/Project/'+props.projName+'/Comparison/Home'} isActive={() => isComparison()} activeStyle={{ background: '#EEFFFF' }} >
        {/* activeStyle */}
			Comparisons
		</NavLink>
		</NavMenu>
	</Nav>
	</>
);
};

export default ProjectTopbar;







