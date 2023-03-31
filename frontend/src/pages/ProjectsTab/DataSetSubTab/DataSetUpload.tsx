import React, { Children } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Box, Button} from '@material-ui/core';
import { ArrowUpward } from '@material-ui/icons';
import { useRef } from 'react';
import {SpreadsheetComponent} from "@syncfusion/ej2-react-spreadsheet";
import { gql, useMutation } from "@apollo/client";




///////////////////////////////////////////////////////////////
//            CSS
///////////////////////////////////////////////////////////////
const useStyles = makeStyles((theme) => ({
	window: {
	  width: 400,
	  height: 400,
	  marginLeft: "auto",
	  marginRight: "auto",
	  marginTop: 100,
	  backgroundColor: "#C9D9D2",
	  padding: theme.spacing(3),
	  display: "flex",
	  flexDirection: "column",
	  alignItems: "center",
	  justifyContent: "center",
	  borderRadius: theme.spacing(3),
	  boxShadow: theme.shadows[3],
	},
	title: {
	  fontSize: 28,
	  fontWeight: "bold",
	  textAlign: "center",
	  marginBottom: theme.spacing(2),
	},
	form: {
	  display: "flex",
	  flexDirection: "column",
	  alignItems: "center",
	  justifyContent: "center",
	  width: "100%",
	},
	input: {
	  width: "100%",
	  marginBottom: theme.spacing(2),
	  padding: theme.spacing(1),
	  fontSize: 18,
	  border: `1px solid ${theme.palette.primary.main}`,
	  borderRadius: theme.spacing(1),
	  "&:focus": {
		outline: "none",
		borderColor: theme.palette.secondary.main,
	  },
	},
	fileInput: {
	  display: "none",
	},
	label: {
	  fontSize: 18,
	  fontWeight: "bold",
	  marginBottom: theme.spacing(1),
	},
	button: {
		marginTop: theme.spacing(2),
	  backgroundColor: theme.palette.secondary.main,
	  color: "#fff",
	  padding: theme.spacing(1.5, 3),
	  borderRadius: theme.spacing(1),
	  transition: "all .3s ease-in-out",
	  "&:hover": {
		backgroundColor: theme.palette.secondary.dark,
		boxShadow: theme.shadows[4],
	  },
	},
	fileName: {
	  fontSize: 16,
	  marginTop: theme.spacing(1),
	  textAlign: "center",
	},
	uploadButton: {
	  backgroundColor: theme.palette.primary.main,
	  color: "#fff",
	  padding: theme.spacing(1, 2),
	  borderRadius: theme.spacing(1),
	  transition: "all .3s ease-in-out",
	  "&:hover": {
		backgroundColor: theme.palette.primary.dark,
		boxShadow: theme.shadows[4],
	  },
	},
  }));

const ADD_DATA = gql`
  mutation AddData ($name:String!, $file:Upload!, $description:String!){
    uploadDataset(name: $name, file:$file, description:$description)
	{
		name
		fileName
		description
		url
	}
  }
`;

const DataSetUpload = () => {
	///////////////////////////////////
	///  Inner Handlers
	///////////////////////////////////
	//const [open, setOpen] = React.useState(true);
	const [name, setName] = React.useState('');
  	const [description, setDescription] = React.useState('');
  	const [file, setFile] = React.useState< File | null>(null);
	const [addData, { data, loading, error }] = useMutation(ADD_DATA);
	

	const classes = useStyles();




	////////////////////////////////////////////////////
	//                HTML
	/////////////////////////////////////////////////
	return (
		<div>
		  <Box className={classes.window}>
			<h1 className={classes.title}>Upload New Data Set</h1>
			<form
			  className={classes.form}
			  onSubmit={(e: any) => {
				e.preventDefault();
				console.log(name, description, file, file!.name);
				addData({
				  variables: { name: name, description: description, file: file },
				});
			  }}
			>
			  <label className={classes.label} htmlFor="name">
				Name:
			  </label>
			  <input
				className={classes.input}
				type="text"
				id="name"
				value={name}
				onChange={(e) => setName(e.target.value)}
			  />
			  <label className={classes.label} htmlFor="description">
				Description:
			  </label>
			  <textarea
				className={classes.input}
				id="description"
				value={description}
				onChange={(e) => setDescription(e.target.value)}
			  />
			  <label className={classes.label} htmlFor="file">
				Choose a file
			  </label>
			  <div>
				<input
				  className={classes.fileInput}
				  type="file"
				  id="file"
				  onChange={(e: any) => {
					setFile(e.target.files[0]);
}}
/>
<label htmlFor="file" className={classes.uploadButton}>
Browse...
</label>
</div>
{file && (
<p className={classes.fileName}>
File Selected: <strong>{file.name}</strong>
</p>
)}
<button className={classes.button} type="submit">
Upload
</button>
</form>
</Box>

  </div>
);
};


export default DataSetUpload;



/* const DataSetUpload = () => {
	///////////////////////////////////
	///  Inner Handlers
	///////////////////////////////////
	//const [open, setOpen] = React.useState(true);
	const classes = useStyles();

	const inputFile = useRef< HTMLInputElement | null>(null);

	const handleUploadClick  = () => {
		inputFile?.current?.click();
	};


	////////////////////////////////////////////////////
	//                HTML
	/////////////////////////////////////////////////
	return (
		<div>
			<Box borderRadius="30px" className={classes.window}>
				<h1 className={classes.text}>Upload New Data Set</h1>
				<input type='file' id='file' ref={inputFile} style={{ display: 'none' }}  />
				<Button variant="contained" size="large" endIcon={<ArrowUpward/>}
					className={classes.uploadButton} onClick={() => { handleUploadClick() }}>
					Upload 
					{ (inputFile.current?.files !== null) ?  inputFile?.current?.files[0].name : null }
				</Button>
			</Box>
			<SpreadsheetComponent
				allowOpen={true}
				openUrl="https://ej2services.syncfusion.com/production/web-services/api/spreadsheet/open"
				allowSave={true}
				saveUrl="https://ej2services.syncfusion.com/production/web-services/api/spreadsheet/save"
	></SpreadsheetComponent>
		</div>
		);
	};
	*/