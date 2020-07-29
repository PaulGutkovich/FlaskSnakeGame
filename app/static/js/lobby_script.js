$(document).ready(function() {
    $("form").submit(function(e) {
        e.preventDefault();
        var data = {"text": $("#text").val()};
        socket.emit("add_room", data);
        join_room(data.text);
        button_clicked = false;
    });
});

var socket = io.connect("/lobby");
var button_clicked = false;

function redirect() {
    window.location.href = "/game/game_page";
}

function join_room(r) {
    if (button_clicked) {
        button_clicked = false;
    }
    else {
        socket.emit("join", {"room": r});
        button_clicked = true;
    }
};

socket.on("game", function() {
    redirect();
})

socket.on("update_rooms", function(data) {
    var new_rooms = data.new_rooms;
    var list_html = "";
    var button_html = "";
    var target_id = "";
    var target_button;

    for (var room of new_rooms) {
        list_html = list_html.concat("\n".concat("<p>", room, "</p>"));
        button_html = "\n".concat("<button type='button' id='button_", room, "' onclick='join_room(", "&#39;", room, "&#39;", ")'>Join</button>")
        list_html = list_html.concat(button_html);
    }

    $("#room_list").html(list_html);

    for (var room of new_rooms) {
        target_id = "#button_".concat(room);
        target_button = $(target_id);
        target_button.off().on("click", (function(r) {
            function f() {
                join_room(r);
            }
            return f;
        })(room)
        );
    }
});

socket.on("message", function(data) {
    alert(data);
});
