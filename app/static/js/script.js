$(document).ready(function() {
    var socket = io.connect("/game");

    $("form").submit(function (e) {
        e.preventDefault();
        var data = {"text": $("#text").val()};
        socket.emit("add_room", data);
    });

    socket.on("update_rooms", function(data) {
        console.log(data);
    });
});

