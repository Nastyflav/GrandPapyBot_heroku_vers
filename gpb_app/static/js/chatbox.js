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
            <p class="user-question">${json.user_question}</p>
            <p class="adress-answer">${json.address}</p>
            <p class="map-answer"><img src="${json.map_url}"></p>
            <p class="wiki-answer">
                ${json.extract}
                Si tu veux te cultiver, on ne sait jamais : 
                <a href='${json.url}'></a></p>
            `;
    messagesElement.innerHTML = markup;
    chatAreaElement.appendChild(messagesElement);
    chatAreaElement.innerHTML += '\n                ';
    document.getElementById("progress").style.display="none";
    console.log(document.getElementById("userinput").textContent);
    document.getElementById("userinput").textContent = '';
    window.scrollBy(0, window.innerHeight);
};


// //-- No use time. It is a javaScript effect.
// function insertChat(who, text, time){
//     if (time === undefined){
//         time = 0;
//     }
//     var control = "";
//     var date = formatAMPM(new Date());
    
//     if (who == "me"){
//         control = '<li style="width:100%">' +
//                         '<div class="message-area">' +
//                             '<div class="text text-l">' +
//                                 '<p>'+ text +'</p>' +
//                                 '<p><small>'+date+'</small></p>' +
//                             '</div>' +
//                         '</div>' +
//                     '</li>';                    
//     }else{
//         control = '<li style="width:100%;">' +
//                         '<div class="message-area">' +
//                             '<div class="text">' +
//                                 '<p>'+text+'</p>' +
//                                 '<p><small>'+date+'</small></p>'                                
//                   '</li>';
//     }
//     setTimeout(
//         function(){                        
//             $("ul").append(control).scrollTop($("ul").prop('scrollHeight'));
//         }, time);
    
// }

// function resetChat(){
//     $("ul").empty();
// }

// $(".user-input").on("keydown", function(e){
//     if (e.which == 13){
//         var text = $(this).val();
//         if (text !== ""){
//             insertChat("me", text);              
//             $(this).val('');
//         }
//     }
// });

// $('body > div > div > div:nth-child(2) > span').click(function(){
//     $(".user-input").trigger({type: 'keydown', which: 13, keyCode: 13});
// })

// //-- Clear Chat
// resetChat();

// //-- Print Messages
// insertChat("me", "Bon, j'ai pas que ça à faire, je t'écoute...", 0);
