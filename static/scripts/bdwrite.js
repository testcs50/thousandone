document.addEventListener('DOMContentLoaded', () => {
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    socket.on('connect', () => {
        document.querySelector('button').addEventListener('click', () => {
            socket.emit('submit vote')
        })
    })
    socket.on('announce vote', data => {
        document.querySelector('h1').innerHTML = data.num
        console.log(data.question)
    })
    socket.on('questions', data => {
        console.log(data)
        for (const question of data.questions) {
            console.log(question)
        }
    })
})