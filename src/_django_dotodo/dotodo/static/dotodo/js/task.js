document.addEventListener("DOMContentLoaded", function() {
    var node = document.createElement("video");
    var child = document.getElementById('id_video');
    child.parentNode.appendChild(node);
    /*'<button id="addVideo" class="button small">Record video</button> ' +
        '<video autoplay muted ></video> <button id="removeVideo" class="button small">Remove video</button> ' +
        '<button id="stopVideo" class="button small">Stop recording</button> <div id="links"></div>');*/
	document.getElementById("addVideo").addEventListener("click", recordSound);
	document.getElementById("stopVideo").addEventListener("click", stopRecord);
    //document.getElementById("playVideo").addEventListener("click", playRecord);
    document.getElementById("removeVideo").addEventListener("click", removeVideo);
});

function hasGetUserMedia() {
  return !!(navigator.getUserMedia || navigator.webkitGetUserMedia ||
            navigator.mozGetUserMedia || navigator.msGetUserMedia);
}

function recordSound(event){
    event.preventDefault();
    document.getElementById("stopVideo").style.visibility = "visible";
    document.getElementsByTagName("video")[0].style.display = "block";
	if (hasGetUserMedia()) {
	    // can record
		var videoElement = document.querySelector('video');
	    navigator.getUserMedia  = navigator.getUserMedia ||
                          navigator.webkitGetUserMedia ||
                          navigator.mozGetUserMedia ||
                          navigator.msGetUserMedia;


		if (navigator.getUserMedia) {
		  navigator.getUserMedia({audio: true, video: true}, function(stream) {

			window.stream = stream; // make stream available to console
			videoElement.src = window.URL.createObjectURL(stream);
			videoElement.play();
			  window.recorder = new MediaRecorder(stream, {
				mimeType: 'video/webm'
			  });
			  window.recorder.start();
		  }, errorCallback);
		} else {
		  video.src = 'video/somevideoID.webm'; // fallback.
		}
	} else {
	  alert('getUserMedia() is not supported in your browser');
	}
}

function stopRecord(event){
    event.preventDefault();
    var videoElement = document.querySelector('video');
    document.getElementById("stopVideo").style.visibility = "hidden";
    document.getElementById("removeVideo").style.visibility = "visible";
   // document.getElementById("playVideo").style.visibility = "visible";
	var el = document.querySelector('#links');
	window.recorder.ondataavailable = e => {
    el.style.display = 'block';
    var a = document.createElement('a'),
    li = document.createElement('br');
    a.download = ['video_', (new Date() + '').slice(4, 28), '.webm'].join('');
    a.href = URL.createObjectURL(e.data);
    a.textContent = a.download;
    el.appendChild(a);
    el.appendChild(li);
        videoElement.pause();
      //  videoElement.setAttribute('controls', 'true');

	videoElement.src = window.URL.createObjectURL(e.data);
		//window.stream = e.data;
  };
	window.recorder.stop();
	
}

function playRecord(event){
    event.preventDefault();
    //var el = document.querySelector('a');
    //var a = el.querySelector('a')[0];

    video.src = 'video/somevideoID.webm';
}

function removeVideo(event){
    event.preventDefault();
    var el = document.querySelector('#links');
    el.innerHTML = "";
}

function errorCallback(error) {
  //console.log('navigator.getUserMedia error: ', error);
    alert(error);
}
