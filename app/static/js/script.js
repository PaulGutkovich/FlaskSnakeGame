$(document).ready(function() {
    var socket = io.connect();
   window.onunload = socket.disconnect();
});