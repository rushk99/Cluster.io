import React from "react";
import logo from "./logo.svg";
import ClusterMenue from "./components/ClusterMenue";
import "./App.css";
import { gql, useQuery } from "@apollo/client";
import { MenuItem } from "@material-ui/core";
import Header from './components/Header';
import NavBar from './components/index';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './pages/Home';
import About from './pages/About';
import OpenProject from "./pages/ProjectsTab/OpenProject";
import Login from "./pages/Login";
import UserManual from "./pages/UserManual";
import ViewProject from "./pages/ProjectsTab/ViewProject";
import NewProject from "./pages/ProjectsTab/NewProject"


function App() {
  return (
   

    <div className="App">
      
    <Router>
    <NavBar />
    <Switch>
    <Route path='/OpenProject' component={OpenProject} />  
    {/* Route deactivated*/}
      {/* <Route path='/Home'  component={Home} /> */} 
      <Route path='/About' component={About} />
      <Route path='/Project' component={ViewProject} />
      <Route path='/Login' component={Login} />
      <Route path='/UserManual' component={UserManual} />
      <Route path='/NewProject' component={NewProject} />
    </Switch>
    </Router>

    </div>
  );
}

export default App;


