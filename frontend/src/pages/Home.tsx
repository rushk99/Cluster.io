/*  Removed from Navlink and router */

import React from 'react';
import Button from '@material-ui/core/Button';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import { ButtonGroup } from '@material-ui/core';

export default function Home() {


  return (
    <div>
  <ButtonGroup orientation='vertical'>
  <Button>About</Button>
  <Button>User Manual</Button>
  <Button>Projects</Button>
  </ButtonGroup>
    </div>
  );
}