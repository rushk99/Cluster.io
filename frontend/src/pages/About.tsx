
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
    textAlign: 'center',
    color: theme.palette.text.secondary,
  },
}));

export default function About() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
		
   
	
<Grid>
        <Grid item xs={12}>
          <Paper className={classes.paper}>

		
		  <h1>About Us</h1>


		  <h5>Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus inventore quia maxime ipsam, distinctio culpa nemo perspiciatis 
			  nulla ex eligendi quisquam ipsum eius consequuntur tempora voluptatibus ea? Quae, dignissimos nihil. Lorem ipsum dolor sit amet 
			  consectetur adipisicing elit. Autem, consectetur ipsa asperiores ratione in maiores accusamus odio dicta itaque excepturi soluta 
			  tenetur reprehenderit est esse qui ad expedita optio dolorum. Lorem ipsum dolor sit amet consectetur, adipisicing elit. Totam, 
			  soluta nobis laborum quia quod explicabo accusantium voluptas molestias iste maiores aspernatur atque eius hic laudantium illo 
			  expedita cumque consequuntur quasi! Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus inventore quia maxime ipsam, distinctio culpa nemo perspiciatis 
			  nulla ex eligendi quisquam ipsum eius consequuntur tempora voluptatibus ea? Quae, dignissimos nihil. Lorem ipsum dolor sit amet 
			  consectetur adipisicing elit. Autem, consectetur ipsa asperiores ratione in maiores accusamus odio dicta itaque excepturi soluta 
			  tenetur reprehenderit est esse qui ad expedita optio dolorum. Lorem ipsum dolor sit amet consectetur, adipisicing elit. Totam, 
			  soluta nobis laborum quia quod explicabo accusantium voluptas molestias iste maiores aspernatur atque eius hic laudantium illo 
			  expedita cumque consequuntur quasi!Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus inventore quia maxime ipsam, distinctio culpa nemo perspiciatis 
			  nulla ex eligendi quisquam ipsum eius consequuntur tempora voluptatibus ea? Quae, dignissimos nihil. Lorem ipsum dolor sit amet 
			  consectetur adipisicing elit. Autem, consectetur ipsa asperiores ratione in maiores accusamus odio dicta itaque excepturi soluta 
			  tenetur reprehenderit est esse qui ad expedita optio dolorum. Lorem ipsum dolor sit amet consectetur, adipisicing elit. Totam, 
			  soluta nobis laborum quia quod explicabo accusantium voluptas molestias iste maiores aspernatur atque eius hic laudantium illo 
			  expedita cumque consequuntur quasi! Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus inventore quia maxime ipsam, distinctio culpa nemo perspiciatis 
			  nulla ex eligendi quisquam ipsum eius consequuntur tempora voluptatibus ea? Quae, dignissimos nihil. Lorem ipsum dolor sit amet 
			  consectetur adipisicing elit. Autem, consectetur ipsa asperiores ratione in maiores accusamus odio dicta itaque excepturi soluta 
			  tenetur reprehenderit est esse qui ad expedita optio dolorum. Lorem ipsum dolor sit amet consectetur, adipisicing elit. Totam, 
			  soluta nobis laborum quia quod explicabo accusantium voluptas molestias iste maiores aspernatur atque eius hic laudantium illo 
			  expedita cumque consequuntur quasi!</h5>
			  
			  <Button type="submit"
            
            variant="contained"
            color="inherit"
			href="https://sites.google.com/view/datadrivenmaterialsscience/team?authuser=0">
			    LEARN MORE ABOUT THE TEAM
				</Button> 
			  </Paper>

			  
        </Grid>
        
      </Grid>
	
    </div>
  );
}