'use strict';

/////// Message Functionality ///////

let message = document.getElementById("message")

message.addEventListener("click", (evt) => {
    evt.preventDefault();

    document.getElementById("message-details").innerHTML = "";
    const messageRecipient = document.getElementById("message").getAttribute('value');
    const messageClick = document.getElementById("message").addEventListener("click", () => {return true});

    const data = {
        messageClick: messageClick,
        messageValue: messageRecipient,
    }

    console.log(data)

    fetch(`/api/bandmessages`, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then((response) => response.json())
    .then(responseData => {

        responseData.message_recipient_details.forEach((element) => {

            //Create parent div to house messages
            const parentDiv = document.getElementById("message-details");

            const borderDiv = document.createElement("div");
            borderDiv.className = "py-2 px-4 border-bottom d-none d-lg-block";
            parentDiv.appendChild(borderDiv)

            const messageAlignDiv = document.createElement("div");
            messageAlignDiv.className = "d-flex align-items-center py-1";
            borderDiv.appendChild(messageAlignDiv);

            const messageRecipient = document.createElement("div");
            messageRecipient.className = "position-relative";
            messageAlignDiv.appendChild(messageRecipient);

            const messageRecipientImage = document.createElement("img");
            messageRecipientImage.src = element.venue_logo;
            messageRecipientImage.className = "square mr-1";
            messageRecipientImage.alt = "Venue";
            messageRecipientImage.style = "width: 40px; height:40px;";
            messageAlignDiv.appendChild(messageRecipientImage);

            const messageRecipientName = document.createElement("div");
            messageRecipientName.className = "flex-grow-1 pl-3";
            messageRecipientName.innerText = element.venue_name;
            messageAlignDiv.appendChild(messageRecipientName);

            const chatBubbleRecipient = document.createElement("div");
            chatBubbleRecipient.className = "position-relative";
            parentDiv.appendChild(chatBubbleRecipient);




        })
    });
})

    // <div class="py-2 px-4 border-bottom d-none d-lg-block">
    //     <div class="d-flex align-items-center py-1">
    //         <div class="position-relative">
    //             <img src="" class="square mr-1" alt="Venue" width="40" height="40">
    //         </div>
    //         <div class="flex-grow-1 pl-3">
    //             <strong>Venue</strong>
    //         </div>
    //     </div>
    // </div>
    // <div class="position-relative">

    //     <div class="chat-messages p-4">
    //         <div class="chat-message-right pb-4">
    //             <div>
    //                 <img src="" class="square mr-1" alt="Venue" width="40" height="40">
    //                 <div class="font-weight-bold mb-1"> Venue Name </div>
    //             </div>
    //             <div class="flex-shrink-1 bg-light rounded py-2 px-3 mr-3">
    //                 Let us know when you show up!
    //             </div>
    //         </div>

    //         <div class="chat-message-left pb-4">
    //             <div>
    //                 <img src="{{ user_info.profile_photo}}" class="square mr-1" alt="Me" width="40" height="40">
    //                 <div class="font-weight-bold mb-1"> {{ user_info.first_name }} {{ user_info.last_name }} </div>
    //             </div>
    //             <div class="flex-shrink-1 bg-light rounded py-2 px-3 ml-3">
    //                 Hey we're here. Where should we load the gear?
    //             </div>
    //         </div>
    //     </div>
    // </div>