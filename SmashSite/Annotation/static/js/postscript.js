//references the youtube api
var tag = document.createElement('script');
tag.id = 'yt-iframe';
tag.src = 'https://www.youtube.com/iframe_api';
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var player;
function onYouTubeIframeAPIReady() {
/**
*Instantiates a new Youtube player when the API has loaded.
*/
  player = new YT.Player('yt-player');
}

function logTime(event){
/**
*Sets the value of the post's time to the current time of the video.
*/
  document.getElementById("id_time").value = Math.floor(player.getCurrentTime());
}

function skipTo(time, halfSpeed){
/**
*Skips video to time and sets playback speed.
*@param {time} int: the target time
*@param {halfSpeed} boolean: true for 0.5 playback speed, false for 1.0
*/
  player.seekTo(time, true);
  if(halfSpeed)
    player.setPlaybackRate(0.5);
  else
    player.setPlaybackRate(1);
  player.pauseVideo();
}

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
