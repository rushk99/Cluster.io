import React from 'react';
import { Container } from '@material-ui/core';
import { palette } from '@material-ui/system';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';

import Box from '@material-ui/core/Box';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'left',
    color: theme.palette.text.secondary,
  },
  heading:{padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,}
}));

export default function UserManual() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
		
      <Grid container spacing={0}>
        <Grid item xs={12}>
          <Paper className={classes.heading}>

		
			  <h1>User Manual</h1>

		  </Paper>
        </Grid>
        <Grid item xs={12}>
          <Paper className={classes.paper}>
			  
		<h2>Clustering Methods</h2>
		<h3>KMeans</h3>
		  <h5>One of the most commonly used clustering techniques that rely on centroids-based models is K-means. 
		  These models attempt to find the most appropriate cluster in terms of similarity based on the distance measure between data points and a set of representative points known as centroids. 
		  The algorithm iteratively updates the pre-defined centroids to assign the new data to the closest. The basic idea is to give an initial centroid, in a step-by-step process, 
		  reassign each point to its closest center, and then the clustering centers will be updated by calculating the mean of the member points. 
		  It repeats the procedure of relocating-and-updating process until meeting the convergence criteria. 
		  The criteria can be a predefined number of iterations or when the total sum of the squared distances between each data point 
		  and its respective centroid falls below a specified threshold.</h5>
			  
			  
			  </Paper>

			  
        </Grid>
        <Grid item xs={12}>
          <Paper className={classes.paper}>
			  
		  <h3>KMedoids</h3>
		  <h5>In k-medoids clustering, each cluster is represented by one of the data points in the cluster, 
			which is the most centrally located point in a cluster, named cluster medoids. 
			K-medoids proceeds by first randomly selecting k data points to serve as the initial medoids for k clusters. 
			The algorithm then improves the medoids by swapping them with other points in the dataset and computing the total cost of the clustering. 
			The cost function of the clustering is defined as the sum of the distances between each point and its assigned medoid. 
			The goal of the algorithm is to find the set of medoids that minimizes the total cost function 
			which is the intercluster distance and maximize intracluster distance.</h5>


		  </Paper>
        </Grid>
		<Grid item xs={12}>
          <Paper className={classes.paper}>
			  
		  <h3>Fuzzy C-Means</h3>
		  <h5>This algorithm works by assigning membership to each data point corresponding 
			to each cluster center based on the distance between the cluster center and the data point. 
		  The closer a point is to the center of the cluster, the more its membership has towards the cluster center.</h5>


		  </Paper>
        </Grid>
		<Grid item xs={12}>
          <Paper className={classes.paper}>
			  
		  <h3>Gaussian Mixture Model</h3>
		  <h5>A Gaussian mixture model involves the mixture of multiple Gaussian distributions. 
			In GMM, each Gaussian distribution represents a cluster in the dataset. 
			It uses the Expectation-Maximization (EM) that iteratively estimates the probabilities of each data point 
			belonging to each mixture component and updates the parameters of that based on the estimated probabilities.</h5>


		  </Paper>
        </Grid>
		<Grid item xs={12}>
          <Paper className={classes.paper}>
			  
		  <h3>Agglomerative</h3>
		  <h5>Agglomerative clustering is a hierarchical Algorithm that constructs a dendrogram or tree-like structure 
			of nested clusters based on the pairwise similarity between data points. 
			It uses a bottom-up approach. First, this approach considers all data points as separate clusters. 
			Then, it attempts to merge them based on the distance function on the notion that 
			data should be assigned to the closest neighbor rather than the farther ones, in terms of distance metrics.</h5>


		  </Paper>
        </Grid>
		<Grid item xs={12}>
          <Paper className={classes.paper}>
			  
		  <h3>Birch</h3>
		  <h5>Balanced iterative Reducing and Clustering Hierarchies (BIRCH) introduces a data structure called a Clustering Feature Tree (CFT), 
			which summarizes information about the data points in a compact form, which allows for faster clustering and reduces memory requirements.
Once the CFT is constructed, the algorithm can perform clustering by traversing the tree and applying a traditional clustering algorithm, 
such as K-means or DBSCAN, to the data points in each leaf node of the tree. 
Overall, BIRCH is a powerful and efficient clustering algorithm that can handle large datasets 
by incrementally reducing the dimensional of the data and clustering the reduced data using hierarchical clustering. 
It is also robust to noise and outliers and can handle clusters with arbitrary shapes and sizes. 
However, BIRCH can be sensitive to the choice of parameters, such as the threshold for merging nodes in the CFT, and may not work well for datasets with highly skewed distributions.</h5>


		  </Paper>
        </Grid>
		<Grid item xs={12}>
          <Paper className={classes.paper}>
			  
		  <h3>Optics</h3>
		  <h5> In the OPTICS algorithm, every individual data point is assigned a reachability distance, 
			which measures the closeness between the point and its neighboring points. 
			The reachability distance is used to order the points in the dataset according to their density and connectivity. 
			The points with the smallest reachability distance are the densest, while the points with the largest reachability distance are the least dense.
The key parameters are the minimum number of points in a cluster (MinPts) 
which is the parameter that roughly controls the minimum size of a cluster and the maximum reachability distance (Eps) 
which determines the maximum reachability distance that a point can be considered part of a cluster.</h5>


		  </Paper>
        </Grid>
		<Grid item xs={12}>
          <Paper className={classes.paper}>
			  
		  <h3>DBSCAN</h3>
		  <h5>In the DBSCAN method, each data point is assigned a density, defined by the number of points 
			that exist within a certain radius (eps) of that point. 
			The algorithm proceeds by identifying "core points" that have at least a minimum 
			number of neighboring points (minPts) within a radius of eps, and "border points" 
			are those points that are located within the eps radius of a core point but not satisfying 
			the minPts criteria. The points that are connected to a core point are considered 
			part of the same cluster, and the border points are assigned to the cluster of their 
			nearest core point. We should keep in mind that it has its own pros and cons that should 
			be considered before applying that.</h5>


		  </Paper>
        </Grid>
      </Grid>
	
    </div>
  );
}