import React from 'react';
import Header from './Header';

import {
Nav,
NavLink,
Bars,
NavMenu,
NavBtn,
NavBtnLink,
} from './NavBarElements';

const Navbar = () => {
	const isAbout = () => {
		return window.location.pathname.indexOf('/About') != -1;
	};

	const isOpenProject = () => {
		return window.location.pathname.indexOf('/OpenProject') != -1 || window.location.pathname.indexOf('/Project') != -1;
	};

	const isSettings = () => {
		return window.location.pathname.indexOf('/Settings') != -1;
	};

	const isManual = () => {
		return window.location.pathname.indexOf('/UserManual') != -1;
	};

return (
	<>
	<Nav>
		<Bars />
        <Header/>
		<NavMenu>
        {/* <NavLink to='/Home' activeStyle={{ color: 'white' }}>
			HOME
		</NavLink> */}
		<NavLink to='/About' isActive={() => isAbout()} activeStyle={{ color: 'white' }} >
        {/* activeStyle */}
			ABOUT
		</NavLink>
        <NavLink to='/OpenProject' isActive={() => isOpenProject()} activeStyle={{ color: 'white' }} >
        {/* activeStyle */}
			PROJECTS
		</NavLink>
		<NavLink to='/Settings' isActive={() => isSettings()} activeStyle={{ color: 'white' }} >
        {/* activeStyle */}
			SETTINGS
		</NavLink>
		<NavLink to='/UserManual' isActive={() => isManual()} activeStyle={{ color: 'white' }} >
        {/* activeStyle */}
			USER MANUAL
		</NavLink>
		{/* Second Nav */}
		{/*<NavBtnLink to='/Login'>Sign In</NavBtnLink> */}
		</NavMenu>
		<NavBtn>
		<NavBtnLink to='/Login' activeStyle={{ color: 'white' }} >LOG OUT</NavBtnLink>
		</NavBtn>
	</Nav>
	</>
);
};

export default Navbar;


