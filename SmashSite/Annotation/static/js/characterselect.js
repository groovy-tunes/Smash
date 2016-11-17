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