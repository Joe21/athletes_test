// button functionality
function meME(){
	var el = $('#music-container');
	var player = $('#audio-player');
	var body = $('body');

	if(stealth === true){
		el.append("<audio id='audio-player' src='https://s3.amazonaws.com/samplepublicbucket/me-unchartered_worlds_cutup.mp3' controls autoplay>");
		$('body').css("background-image", "url('/static/crud/n7.jpg')");
		stealth = false;
	} else {
		el.empty();
		$('body').css("background-image", "url('/static/crud/football.jpg')");
		stealth = true;
	}
}

// {% static 'crud/style.css' %}
// 	background-image: url('background.jpg');


// Global variable
var stealth = true;

// On window load
$(function(){
	$('#crazy-button').on('click', meME);
});