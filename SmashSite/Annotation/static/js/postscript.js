//references the youtube api
var tag = document.createElement('script');
tag.id = 'yt-iframe';
tag.src = 'https://www.youtube.com/iframe_api';
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var player;

/**
*Instantiates a new Youtube player when the API has loaded.
*/
function onYouTubeIframeAPIReady() {
  player = new YT.Player('yt-player');
}

/**
*Sets the value of the post's time to the current time of the video.
*/
function logTime(event){
  document.getElementById("id_time").value = Math.floor(player.getCurrentTime());
}

/**
*Skips video to time and sets playback speed.
*@param {time} int: the target time
*@param {halfSpeed} boolean: true for 0.5 playback speed, false for 1.0
*/
function skipTo(time, halfSpeed){
  player.seekTo(time, true);
  if(halfSpeed)
    player.setPlaybackRate(0.5);
  else
    player.setPlaybackRate(1);
  player.pauseVideo();
}

/**
*Brings up yes or no text to confirm a user wants to delete their post.
*/
function showDelete(){
  var yesNo = document.getElementsByClassName("confirm");
  var i;
  for(i = 0;i < yesNo.length; i++){
    yesNo[i].style.display = "inline";
  }
  document.getElementById("delBtn").style.display = "none";
}

/**
*Hides yes or no text for deletion confirmation.
*/
function hideDelete(){
  var yesNo = document.getElementsByClassName("confirm");
  var i;
  for(i = 0;i < yesNo.length; i++){
    yesNo[i].style.display = "none";
  }
  document.getElementById("delBtn").style.display = "inline";
}
