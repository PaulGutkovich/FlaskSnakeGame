setInterval(ping, 1000);

function ping() {
    var d = new Date();
    var t = d.getTime();

    $.get("/game/ping",
    {"time": t},
    function(data) {
        console.log(data);
    }
    );
};