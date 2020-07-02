var canvas = document.getElementById("c");
var context = canvas.getContext("2d");

document.onkeydown = checkKey;

function checkKey(e) {

    e = e || window.event;

    if (e.keyCode == '38') {
        socket.emit("dir_change", {"dir": [0, 1]});
    }
    else if (e.keyCode == '40') {
        socket.emit("dir_change", {"dir": [0, -1]});
    }
    else if (e.keyCode == '37') {
        socket.emit("dir_change", {"dir": [-1, 0]});
    }
    else if (e.keyCode == '39') {
        socket.emit("dir_change", {"dir": [1, 0]});
    }

}

var socket = io.connect("/game");

function redirect() {
    window.location.href = "/game";
}

socket.on("entrance_check", function() {
    //console.log("entrance check");
    socket.emit("entrance_check_response");
})

socket.on("kick", function() {
    alert("You are not in a room. You will be redirected to the lobby.");
    redirect();
})

socket.on("snakes", function(data){
    console.log(data.blocks);
    //draw(data);
})