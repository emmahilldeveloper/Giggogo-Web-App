'use strict';

/////// Message Functionality ///////

let message = document.getElementById("message")

message.addEventListener("click", (evt) => {
    evt.preventDefault();

    document.getElementById("message-details").innerHTML = "";

    const data = {
        messageClick: document.getElementById("message").click(),
        messageValue: document.getElementById.getAttribute('value'),
    }

    fetch(`/api/messages`, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then((response) => response.json())
    .then(responseData => {

        responseData.messages.forEach((element) => {

            //Create parent div to house messages
            const parentDiv = document.getElementById("message-details");

            //

            
        })
    });
})

    <div class="py-2 px-4 border-bottom d-none d-lg-block">
        <div class="d-flex align-items-center py-1">
            <div class="position-relative">
                <img src="" class="square mr-1" alt="Venue" width="40" height="40">
            </div>
            <div class="flex-grow-1 pl-3">
                <strong>Venue</strong>
            </div>
        </div>
    </div>
    <div class="position-relative">
        <div class="chat-messages p-4">
            <div class="chat-message-right pb-4">
                <div>
                    <img src="" class="square mr-1" alt="Venue" width="40" height="40">
                    <div class="font-weight-bold mb-1"> Venue Name </div>
                </div>
                <div class="flex-shrink-1 bg-light rounded py-2 px-3 mr-3">
                    Let us know when you show up!
                </div>
            </div>

            <div class="chat-message-left pb-4">
                <div>
                    <img src="{{ user_info.profile_photo}}" class="square mr-1" alt="Me" width="40" height="40">
                    <div class="font-weight-bold mb-1"> {{ user_info.first_name }} {{ user_info.last_name }} </div>
                </div>
                <div class="flex-shrink-1 bg-light rounded py-2 px-3 ml-3">
                    Hey we're here. Where should we load the gear?
                </div>
            </div>
        </div>
    </div>