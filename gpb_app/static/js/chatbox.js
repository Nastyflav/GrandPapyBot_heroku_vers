//Get the user input from the form
function getUserInput(event) {
    event.preventDefault();
    document.getElementById("progress").style.display="block";
    fetch('/chatbox', {method: 'POST', body: new FormData(this)})
    .then(function(response) { return response.json(); })
    .then(publish)
};

// format JSON received
function publish(json) {
    const chatElt = document.getElementById("chatbox");
    answerElt = document.createElement("div");
    const loadElt  = document.getElementById('load');
    const markup = `
            <p class='question left'>${json.userquestion}</p>
            <p class='answer right txtright'>${json.address}</p>
            <p class='answer right txtright'>
                ${json.extract}
                ${json.url ? `                Mais je fatigue : c'est l'heure de la sieste!
                Va donc voir <a href='https://fr.wikipedia.org/w/index.php?curid=${json.url}'>sur wikipedia</a>.` :   ''}
            </p>
            ${json.map_img_src ? `<p class='answer right txtcenter'><a href="${json.map_link}"><img src="${json.map_img_src}"></a></p>` : ''}
            `;
    answerElt.innerHTML = markup;
    chatElt.appendChild(answerElt);
    chatElt.innerHTML += '\n                ';
    document.getElementById("progress").style.display="none";
    console.log(document.getElementById("userinput").textContent);
    document.getElementById("userinput").textContent = '';
    window.scrollBy(0, window.innerHeight);
};

const form = document.getElementById('form');
form.addEventListener('submit', getUserInput);

// function formatAMPM(date) {
//     var hours = date.getHours();
//     var minutes = date.getMinutes();
//     var ampm = hours >= 12 ? 'PM' : 'AM';
//     hours = hours % 12;
//     hours = hours ? hours : 12; // the hour '0' should be '12'
//     minutes = minutes < 10 ? '0'+minutes : minutes;
//     var strTime = hours + ':' + minutes + ' ' + ampm;
//     return strTime;
// }            

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
