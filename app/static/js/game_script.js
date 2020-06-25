var canvas = document.getElementById("c");
var context = canvas.getContext("2d");

var socket = io.connect("/game");

socket.on("lobby", function() {
    window.location.href = "/game"
});