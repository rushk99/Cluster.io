import { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { gql, useQuery } from "@apollo/client";
import { Box } from '@material-ui/core';
import ClusterOutput from './ClusterOutput';
///////////////////////////////////////////////////////////////
//            CSS
///////////////////////////////////////////////////////////////
const useStyles = makeStyles(theme => ({
	//Title, the top of the side bar where the project name is
	window: {
		marginLeft: 250,
		marginTop: 100,
		backgroundColor: '#C9D9D2',
		width: '500px',
	},
	config:{
		textAlign: "left",
		marginLeft:10
	},
	clusterButton: {
        textAlign: "center",
        marginBottom: 20,
        backgroundColor: '#63ace5',
        color: '#fff',
        borderRadius: '5px',
        padding: '10px 20px',
        cursor: 'pointer',
        '&:hover': {
            backgroundColor: '#408bcf',
        },
    },
	clusterOutput:{
		
		marginLeft:100,
		marginTop:0
	}
}));




const GET_CLUSTER_CONFIG = gql`
  query getClusterConfig($clusterName: String!) {
    clusteringMethod(name: $clusterName) {
		name label options {
    	name description type default}
    }
  }
`;

function ClusterConfig({ clusterName }: any) {
    const classes = useStyles();
    const [formData, setFormData] = useState({});
    let [copyformData, setcopyFormData] = useState({});
    const [showDiv2, setShowDiv2] = useState(false);
    const [selectedClusterDataOn, setselectedClusterDataOn] = useState("Hardness"); 
    const { loading, error, data } = useQuery(GET_CLUSTER_CONFIG, {
        variables: { clusterName },
    });

    if (loading) {
        return <div>loading...</div>;
    }
    if (error) {
        return <div>error...</div>;
    }

    const handleChange = (event: any) => {
        setFormData({ ...formData, [event.target.name]: event.target.value });
    };

    const handleClusterDataChange = (event: any) => {
        setselectedClusterDataOn(event.target.value);
    };

    const handleSubmit = (event: any) => {
        console.log("testing columns");
        
        console.log(formData);
        
        event.preventDefault();
        setcopyFormData({ ...formData, selectedClusterDataOn });
        setShowDiv2(true);
    };

    return (
        <div style={{ display: "flex" }}>
            <div style={{ flex: 1 }}>
                <Box
                    display="flex"
                    flexWrap="wrap"
                    borderRadius="30px"
                    className={classes.window}
                >
                    <form onSubmit={handleSubmit}>
                        {data.clusteringMethod.options.map(
                            (option: any, index: any) => (
                                <div className={classes.config}>
                                    <h3>
                                        {index + 1}) Parameter :-{" "}
                                        {option.name}
                                    </h3>
                                    <h5>
                                        Description :-{" "}
                                        {option.description}
                                    </h5>
                                    <h4>
                                        &emsp;&emsp;&emsp;Type :-{" "}
                                        {option.type}
                                    </h4>
                                    <label>
                                        <h4>
                                            &emsp;&emsp;&emsp;Set Parameter:- <br />
                                            &emsp;&emsp;&emsp;(default value = "
                                            {option.default}")<br />
                                            &emsp;&emsp;&emsp;
                                            <input
                                                type="text"
                                                name={option.name}
                                                placeholder={option.default}
                                                onChange={handleChange}
                                            />
                                        </h4>
                                    </label>
                                </div>
                            )
                        )}
                        <div className={classes.config}>
                            <h3>Select Cluster Data On:</h3>
                            <label>
                                <input
                                    type="radio"
                                    value="Hardness"
                                    checked={selectedClusterDataOn === "Hardness"}
                                    onChange={handleClusterDataChange}
                                />
                                &nbsp;Hardness
                            </label>
                            <br />
                            <label>
                                <input
                                    type="radio"
                                    value="Modulus"
                                    checked={selectedClusterDataOn === "Modulus"}
                                    onChange={handleClusterDataChange}
                                />
                                &nbsp;Modulus
                            </label>
                        </div>
                        <br />
                        <button className={classes.clusterButton} type="submit">
                            Perform Clustering!
                        </button>
                    </form>
                </Box>
            </div>
            {showDiv2 && (
                <div style={{ flex: 1 }}>
                    <div className={classes.clusterOutput}>
                        <ClusterOutput
                            fdata={copyformData}
                            cname={clusterName}
                        />
                    </div>
                </div>
            )}
        </div>
    );
}
export default ClusterConfig;