function backgroundChange() {
	var body = $('body');
	if(body.css('background-color')==='rgb(255, 255, 255)'){
		$('body').css('background-color', '#000000');
	} else {
		$('body').css('background-color', '#ffffff');
	}
}