/*
var currentSelector = "";
var currentGame = "";
var p1 = "";
var p2 = "";
var p3 = "";
var p4 = "";
var map = "";
var cursorsOn = false;
*/
/*
function setGame(elem){
	/**
		Sets the game to the element selected and then disables the buttons for the other games
		Also restores all variables for characters etc.
		@param {element} elem - the element selected
	if(elem.id == "Melee"){
		if(currentGame != ""){
			resetSelections(elem);
		}
		else{
			currentGame = elem.id;
			setBorder(elem);
			document.getElementById("MeleeIcons").style.display = "block";
			document.getElementById("S64").style.visibility = "hidden";
			document.getElementById("Smash4").style.visibility = "hidden";
		}
	}
	if(elem.id == "S64"){
		if(currentGame != ""){
			resetSelections(elem);
		}
		else{
			currentGame = elem.id;
			setBorder(elem);
			document.getElementById("S64Icons").style.display = "block";
			document.getElementById("Melee").style.visibility = "hidden";
			document.getElementById("Smash4").style.visibility = "hidden";
		}
	}
	if(elem.id == "Smash4"){
		if(currentGame != ""){
			resetSelections(elem);
		}
		else{
			currentGame = elem.id;
			setBorder(elem);
			document.getElementById("Smash4Icons").style.display = "block";
			document.getElementById("S64").style.visibility = "hidden";
			document.getElementById("Melee").style.visibility = "hidden";
		}
	}
}
*/
function show(){
	/**
		Shows the inputWell.
	*/
	document.getElementById("search").style.display = "none";
	document.getElementById("inputWell").style.display = "block";
	document.getElementById("showBtn").style.display = "none";
}

function hide(){
	/**
		Hides the inputWell.
	*/
	document.getElementById("search").style.display = "block";
	document.getElementById("inputWell").style.display = "none";
	document.getElementById("showBtn").style.display = "block";
}

/*
function setTags(){
	/**
		Sets the value of the hidden form data.
	var totalTags = p1 + "," + p2 + "," + p3 + "," + p4 + "," + map;
	document.getElementById("id_tags").value = totalTags;
}
/*
function setBorder(elem){
	/**
		Sets borders to target element.
		@param {element} elem - the target element
	if(elem.id != "Melee" || elem.id != "Smash4" || elem.id !="S64"){
		if(currentSelector == "P1" || elem.id == "P1"){
			document.getElementById(elem.id).style.border = "thick solid #8B2726";
			document.getElementById(elem.id).style.borderRadius = "5px";
		}
		else if(currentSelector == "P2" || elem.id == "P2"){
			document.getElementById(elem.id).style.border = "thick solid #2D2C7A";
			document.getElementById(elem.id).style.borderRadius = "5px";
		}
		else if(currentSelector == "P3" || elem.id == "P3"){
			document.getElementById(elem.id).style.border = "thick solid #867909";
			document.getElementById(elem.id).style.borderRadius = "5px";
		}
		else if(currentSelector == "P4" || elem.id == "P4"){
			document.getElementById(elem.id).style.border = "thick solid #1D5F22";
			document.getElementById(elem.id).style.borderRadius = "5px";
		}
		else if(currentSelector == "Map" || elem.id == "Map"){
			document.getElementById(elem.id).style.border = "thick solid #B7BAC0";
			document.getElementById(elem.id).style.borderRadius = "5px";
		}
	}
	else{
		document.getElementById(elem.id).style.border = "thick solid #ff9800";
		document.getElementById(elem.id).style.borderRadius = "5px";
	}
}
*/

/*
function resetSelections(elem){
	/**
		Resets all the variables to their default values.
		@param {element} elem - the element that is currently selected
	p1 = "";
	p2 = "";
	p3 = "";
	p4 = "";
	map = "";
	currentGame = "";
	document.getElementById(elem.id).style.border = "0";
	setBorder(elem, true);
	var elemIcon = elem.id + "Icons";
	document.getElementById(elemIcon).style.display = "none";
	document.getElementById("S64").style.visibility = "visible";
	document.getElementById("Smash4").style.visibility = "visible";
	document.getElementById("Melee").style.visibility = "visible";
}
*/

/** I thought that info about players isn't too useful
function setSelector(elem){
	/**
		Sets the current selector.
		@param {element} elem - the element we are using to choose the selector

	if(elem.id == "P1"){
		if(currentSelector == elem.id){currentSelector = "";}
		else{currentSelector = "P1";}
	}
	else if(elem.id == "P2"){
		if(currentSelector == elem.id){currentSelector = "";}
		else{currentSelector = "P2";}
	}
	else if(elem.id == "P3"){
		if(currentSelector == elem.id){currentSelector = "";}
		else{currentSelector = "P3";}
	}
	else if(elem.id == "P4"){
		if(currentSelector == elem.id){currentSelector = "";}
		else{currentSelector = "P4";}
	}
	else if(elem.id == "Map"){
		if(currentSelector == elem.id){currentSelector = "";}
		else{currentSelector = "Map";}
	}
	
	if(currentSelector != ""){setBorder(elem);}
	else{document.getElementById(elem.id).style.border = "0";}
}
*/

/*
function setSelection(elem){
	/**
		Sets the selection of the current selector.
		@param {element} elem - the target selection
	if(currentSelector == ""){
		return;
	}
	else{
		if(currentSelector == "P1"){
			p1 = elem.id;
			alert(p1);
			//change img to something indicating p1
		}
		else if(currentSelector == "P2"){
			p2 = elem.id;
			alert(p2);
			//change img to something indicating p2
		}
		else if(currentSelector == "P3"){
			p3 = elem.id;
			alert(p3);
			//change img to something indicating p3
		}
		else if(currentSelector == "P4"){
			p4 = elem.id;
			alert(p4);
			//change img to something indicating p4
		}
		else if(currentSelector == "Map"){
			map = elem.id;
			alert(map);
			//change img to something indicating map
		}
		
	}
}
*/
