import React, { Children } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Box, Button, ListItem, ListItemText } from '@material-ui/core';
import { CheckBoxOutlineBlank, CheckBox } from '@material-ui/icons';
import { useHistory } from "react-router-dom";

///////////////////////////////////////////////////////////////
//            CSS
///////////////////////////////////////////////////////////////
const useStyles = makeStyles(theme => ({
	leftSide: {
	  width: '50%',
	  float: 'left',
	  outlineColor: 'black',
	  outlineWidth: '1px',
	  outlineStyle: 'solid',
	  margin: '0px',
	  paddingTop: '5px',
	  paddingBottom: '5px'
	},
	midSide: {
	  width: '25%',
	  float: 'left',
	  outlineColor: 'black',
	  outlineWidth: '1px',
	  outlineStyle: 'solid',
	  margin: '0px',
	  paddingTop: '5px',
	  paddingBottom: '5px'
	},
	rightSide: {
	  width: '25%',
	  float: 'left',
	  outlineColor: 'black',
	  outlineWidth: '1px',
	  outlineStyle: 'solid',
	  margin: '0px',
	  paddingTop: '5px',
	  paddingBottom: '5px'
	}
  }));
  
  const ClusterDataRow = (props: { leftText: String, midText: String, rightText: String }) => {
	const [open, setOpen] = React.useState(true);
	const classes = useStyles();
  
	const handleDownload = () => {
	  // implementation here
	}
  
	return (
	  <div>
		<ListItemText disableTypography className={classes.leftSide} primary={props.leftText} />
		<ListItemText disableTypography className={classes.midSide} primary={props.midText} />
		<ListItemText disableTypography className={classes.rightSide} primary={props.rightText} />
	  </div>
	);
  };

export default ClusterDataRow;