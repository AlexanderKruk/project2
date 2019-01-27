
function myFunc(vars) {
    return vars
}

document.addEventListener('DOMContentLoaded', () => {

    // Connect to websocket
    var channel_name = localStorage.getItem("channel");
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // When connected, configure buttons
    socket.on('connect', () => {

        $(document).on('submit', '#my-form', () => {

                        let text = document.querySelector('#text').value;
                        socket.emit('send to chat', {'text': text});
                        document.querySelector('#text').value = "";
                        return false;
                    });
    });

    // When a new vote is announced, add to the unordered list
    socket.on('broadcast chat', data => {
        const li = document.createElement('li');
        li.innerHTML = `${data.text}`;
        document.querySelector('#chat').append(li);
    });
});
