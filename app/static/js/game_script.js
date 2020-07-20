var canvas = document.getElementById("c");
var ctx = canvas.getContext("2d");

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

socket.on("snakes", function(data){;
    draw(data.blocks);
})

function draw(data) {
    ctx.fillStyle = "#FFFFFF";
    ctx.fillRect(0, 0, 640, 460);
    ctx.strokeStyle = "#000000";
    ctx.strokeRect(0, 0, 640, 460);
    ctx.fillStyle = "#000000";
    ctx.strokeStyle = "#FF0000";
    for (var snake of data) {
        for (var block of snake) {
            draw_block(block);
        }
    }
}

function draw_block(block) {
    x = block[0];
    y = block[1];
    ctx.fillRect(20*x, 440-20*y, 20, 20);
    ctx.strokeRect(20*x, 440-20*y, 20, 20);
}