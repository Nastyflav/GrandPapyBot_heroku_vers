// Listen to the form and lauch the chat functions
let form = document.getElementById('form');
form.addEventListener('submit', getUserInput);

// Initializes the map, based on the GPS coordinates given by the server
function mapInit(json) {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: json.latitude, lng: json.longitude},
        zoom: 15
      });
    marker = new google.maps.Marker({
        position: {lat: json.latitude, lng: json.longitude},
        map: map,
        });
};
 
//Gets the user input from the form and lauches the publishing function as a JS promise
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
            ${json.address ? `<p class="adress-answer">${json.address}</p>`:""} 
            ${json.extract ? `<p class="wiki-answer">${json.message_story} : ${json.extract} <br/>
                Si tu veux te cultiver (on ne sait jamais) : 
                <a href='${json.url}'>en savoir plus</a></p></p>`:""}
            `;
    messagesElement.innerHTML = markup;
    chatAreaElement.appendChild(messagesElement);
    chatAreaElement.innerHTML += '\n                ';
    document.getElementById("progress").style.display="none";
    document.getElementById("userinput").textContent = '';
    window.scrollBy(0, window.innerHeight);
    mapInit(json);
};

