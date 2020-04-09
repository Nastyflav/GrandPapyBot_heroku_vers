// Listen to the form and lauch the chat functions
let form = document.getElementById('form');
form.addEventListener('submit', getUserInput);

//Get the user input from the form
function getUserInput(event) {
    event.preventDefault();
    document.getElementById("progress").style.display="block";
    fetch('/chatbox', {method: 'POST', body: new FormData(this)})
    .then(function(response) { return response.json(); })
    .then(messagesPublishing)
};

// receiving json and creating DOM elements to print it
function messagesPublishing(json) {
    const chatAreaElement = document.getElementById("chatbox");
    messagesElement = document.createElement("div");
    const markup = `
            <p class="user-question">${json.userquestion}</p>
            <p class="adress-answer">${json.message_address}</p>
            ${json.name ? `<p class="adress-answer">${json.name} ${json.address}</p>`:""}
            ${json.map_url ? `<p class="map-answer"><img src="${json.map_url}"></p>`:""}
            ${json.extract ? `<p class="wiki-answer">${json.message_story} : ${json.extract} <br/>
                Si tu veux te cultiver, on ne sait jamais : 
                <a href='${json.url}'>en savoir plus</a></p></p>`:""}
            `;
    messagesElement.innerHTML = markup;
    chatAreaElement.appendChild(messagesElement);
    chatAreaElement.innerHTML += '\n                ';
    document.getElementById("progress").style.display="none";
    document.getElementById("userinput").textContent = '';
    window.scrollBy(0, window.innerHeight);
};
