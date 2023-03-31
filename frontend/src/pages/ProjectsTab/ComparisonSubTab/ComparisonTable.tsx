import React, { Children } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Box, ListItem, ListItemText } from '@material-ui/core';


const comparisonNames = ["PVC", "AVB", "K Mean V K Nice"];
let selectedComparison = -1;

//TODO atach to backend
function getComparisonNames() {
	return comparisonNames;
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
	comparisonName: {
		backgroundColor: "white",
		outlineColor: 'black',
		outlineWidth: '2px',
		outlineStyle: 'solid'
	}
}));

const ComparisonTable = () => {
	///////////////////////////////////
	///  Inner Handlers
	///////////////////////////////////
	
	const [open, setOpen] = React.useState(true);
	const classes = useStyles();
	


	//Expands main tabs(shows file name)
	
	const selectComparison = (text: String, index: number) => {
		selectedComparison = index;
		console.log("selectedComparison");
		setOpen(!open);
	};

    


	////////////////////////////////////////////////////
	//                HTML
	/////////////////////////////////////////////////
	return (
		<div>
			<Box className={classes.table}>
				<ListItem className={classes.title}>
					<ListItemText disableTypography primary={"Existing Comparisons"} />
				</ListItem>
					{getComparisonNames().map((text, index) => (
						<div>
							<ListItem button selected={selectedComparison==index}
							key={text} className={classes.comparisonName} onClick={() => { selectComparison(text, index) }}>
								<ListItemText primary={text} />
							</ListItem>
						</ div>
					))}
			</Box>
		</div>
	);
};

export default ComparisonTable;