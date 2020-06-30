var canvas = document.getElementById("c");
var context = canvas.getContext("2d");

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