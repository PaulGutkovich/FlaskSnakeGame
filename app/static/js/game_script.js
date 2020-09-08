var canvas = document.getElementById("c");
var ctx = canvas.getContext("2d");

var form = document.getElementById("dead_form");
form.style.display = "none";

form.onsubmit = function(e) {
    e.preventDefault();
};

var WIDTH = 40;
var HEIGHT = 30;
var SIZE = 20;

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
    draw(data.blocks);
})

socket.on("food", function(data){
    draw_food(data.food);
})

socket.on("update", function(data) {
    background();
    draw_food(data.food);
    draw(data.blocks, data.colors);
    socket.emit("dead_check");
})

socket.on("dead_status", function(data) {
    if (data.dead) {
        if (form.style.display == "none") {
            form.style.display = "block";
        }
    }
})

function respawn() {
    socket.emit("respawn");
}

socket.on("hide_form", function() {
    form.style.display = "none";
})

function draw(blocks, colors) {
    ctx.fillStyle = "#000000";
    ctx.strokeStyle = "#FF0000";
    for (var i = 0; i++; i< blocks.length) {
        var snake = blocks[i];
        var color = colors[i];
        for (var block of snake) {
            draw_block(block, color);
        }
    }
}

function background() {
    ctx.fillStyle = "#FFFFFF";
    ctx.fillRect(0, 0, WIDTH*SIZE, HEIGHT*SIZE);
    ctx.strokeStyle = "#000000";
    ctx.strokeRect(0, 0, WIDTH*SIZE, HEIGHT*SIZE);
}


function draw_block(block, color) {
    x = block[0];
    y = block[1];
    ctx.fillRect(SIZE*x, (HEIGHT-1-y)*SIZE, SIZE, SIZE);
    ctx.strokeStyle = color;
    console.log(ctx.strokeStyle);
    ctx.strokeRect(SIZE*x, (HEIGHT-1-y)*SIZE, SIZE, SIZE);
}

function draw_food(food) {
    x = food[0];
    y = food[1];
    ctx.fillStyle = "#0000FF"
    ctx.strokeStyle = "#000000"
    ctx.fillRect(SIZE*x, (HEIGHT-1-y)*SIZE, SIZE, SIZE)
    ctx.strokeRect(SIZE*x, (HEIGHT-1-y)*SIZE, SIZE, SIZE)
}