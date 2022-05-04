window.onload = firstBotMessage;

inputId = document.getElementById('chat-input');
inputId.addEventListener('keyup', function onEvent(e) {
    if (e.keyCode === 13) {
        sendReply()
    }
});

// initial message from the bot
function firstBotMessage() {
    let firstMessage = "How's it going? Type help for a list of commands."
    document.getElementById("msg").innerHTML = '<p class="username">Chatbot</p><p>' + firstMessage + '</p>'
}


// parse message from the user and fetch the response from the bot
function sendReply() {
    let message = document.getElementById('chat-input').value
    message = message.replace(/<[^>]+>.?/g, '')
    if (message != '') {
        newMessage(message, 'User', true)
    }
    let chatinput = document.getElementById('chat-input')
    document.getElementById('chat-input').value = ""
    document.getElementById('inputbox').scrollIntoView({ block: 'end', behavior: 'smooth' })

    fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: JSON.stringify({ message: message }),
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
        }) //change this to the url of the json file
        .then(response => response.json())
        .then(response => {
            newMessage(response.answer, 'Chatbot', false)
        })
}

// display messages from the bot and user
function newMessage(text, user, darker) {
    var newDiv = document.createElement('div')
    newDiv.id = 'msg'
    if (darker) {
        newDiv.className = 'container darker'
    } else {
        newDiv.className = 'container'
    }
    newDiv.innerHTML = '<p class="username">' + user + '</p><p>' + text + '</p>'
    let lastDiv = document.getElementById("chatbox").lastChild
    insertAfter(lastDiv, newDiv)
}

// helper function to insert a new element after a given element
function insertAfter(referenceNode, newNode) {
    referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling)
}