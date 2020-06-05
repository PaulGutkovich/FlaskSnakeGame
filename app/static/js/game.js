console.log("this is a test bitches");

const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
document.addEventListener("keydown", keyPressed);
setInterval(game, 1000/15);

const form = document.getElementById("submit_form");

var score = 0;

var vx = 20;
var vy = 0;

var ate = false;
var new_food = true;

var food_x = 0;
var food_y = 0;

var snake = [{x:320, y:200}];

var died = false;
var just_died = false;

function game() {
    if (died) {
        ctx.fillStyle = "black";
        ctx.font = "30px Arial";
        ctx.fillText("You died. Your score was ".concat(score, "."), 170, 220);
        return 1;
    }

    ctx.fillStyle = "white";
    ctx.strokestyle = "black";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.strokeRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "black";
    ctx.font = "30px Arial";
    ctx.fillText(score, 10, 40);

    if (new_food) {
        score = score + 1;
        food_x = 20*Math.floor(Math.random()*32);
        food_y = 20*Math.floor(Math.random()*23);
        new_food = false;
    }

    ctx.fillStyle = "red";
    ctx.strokestyle = "black";

    ctx.fillRect(food_x, food_y, 20, 20);
    ctx.strokeRect(food_x, food_y, 20, 20);

    for (let part of snake){
        ctx.fillStyle = "green";
        ctx.strokestyle = "lightgreen";
        ctx.fillRect(part.x, part.y, 20, 20);
        ctx.strokeRect(part.x, part.y, 20, 20);
    }

    head = snake[0];
    if (head.x<0) {
        head.x += 640;
    }
    if (head.x>=640) {
        head.x -= 640;
    }
    if (head.y<0){
        head.y += 460;
    }
    if (head.y>=460){
        head.y -= 460;
    }

    if (head.x == food_x) {
        if (head.y == food_y){
            ate = true;
            new_food = true;
        }
    }

    new_head = {x: head.x+vx, y:head.y+vy};
    snake.unshift(new_head)

    if (ate==false) {
        snake.pop();
    }

    if (ate) {
        ate=false;
    }

    for (let i = 1; i < snake.length; i++){
        let part = snake[i];
        if (new_head.x == part.x){
            if (new_head.y == part.y){
                died = true;
                just_died = true;
            }
        }
    }
}

function keyPressed(evt) {
    switch (evt.keyCode) {
        case 37:
            vx = -20; vy = 0;
            break;
        case 38:
            vx = 0; vy = -20;
            break;
        case 39:
            vx = 20; vy = 0;
            break;
        case 40:
            vx = 0; vy = 20;
            break;
    }
}