function showDelete(){
/**
*Brings up yes or no text to confirm a user wants to delete their post.
*/
var yesNo = document.getElementsByClassName("confirm");
var i;
for(i = 0;i < yesNo.length; i++){
  yesNo[i].style.display = "inline";
}
document.getElementById("delBtn").style.display = "none";
}

function hideDelete(){
  /**
  *Hides yes or no text for deletion confirmation.
  */
  var yesNo = document.getElementsByClassName("confirm");
  var i;
  for(i = 0;i < yesNo.length; i++){
    yesNo[i].style.display = "none";
  }
  document.getElementById("delBtn").style.display = "inline";
}
