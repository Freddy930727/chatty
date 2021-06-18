
function connect(){
	eel.connection(document.getElementById("ip_input").value,document.getElementById("port_input").value);
}

function sendmessage(){
	eel.send(document.getElementById("input_box").value);
}

eel.expose(quit);
function quit(){
	window.close();
}

eel.expose(show_story);
function show_story(content){
	var story=document.getElementById("story");
	story.scrollTop=story.scrollHeight;
	story.value+=content;
}
