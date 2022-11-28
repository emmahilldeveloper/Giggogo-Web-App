'use strict';

/////// Message Functionality ///////

let message = document.getElementById("message");

let allMessageButtons = document.querySelectorAll("#message");

allMessageButtons.forEach((element) => {

    element.addEventListener("click", (evt) => {
        evt.preventDefault();
    
        document.getElementById("message-details").innerHTML = "";
        const messageRecipient = element.getAttribute('value');
    
        const data = {
            messageValue: messageRecipient,
        }
    
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
    
                const recipientBubbleDiv = document.createElement("div");
                recipientBubbleDiv.className = "chat-messages p-4";
                chatBubbleRecipient.appendChild(recipientBubbleDiv);
    
                const recipientBubble = document.createElement("div");
                recipientBubble.className = "chat-message-right pb-4";
                recipientBubbleDiv.appendChild(recipientBubble);
    
                const recipientBubbleDetails = document.createElement("div");
                recipientBubble.appendChild(recipientBubbleDetails);
    
                const recipientBubbleImage = document.createElement("img");
                recipientBubbleImage.src = element.venue_logo;
                recipientBubbleImage.className = "square mr-1";
                recipientBubbleImage.alt = "Venue";
                recipientBubbleImage.style = "width: 40px; height:40px;";
                recipientBubbleDetails.appendChild(recipientBubbleImage);
    
                const recipientBubbleName = document.createElement("div");
                recipientBubbleName.className = "font-weight-bold mb-1";
                recipientBubbleName.innerText = element.venue_name
                recipientBubbleDetails.appendChild(recipientBubbleName);

                const senderBubble = document.createElement("div");
                senderBubble.className = "chat-message-left pb-4";
                recipientBubbleDiv.appendChild(senderBubble);
    
                const senderBubbleDetails = document.createElement("div");
                senderBubble.appendChild(senderBubbleDetails);
    
                const senderBubbleImage = document.createElement("img");
                senderBubbleImage.src = element.band_logo;
                senderBubbleImage.className = "square mr-1";
                senderBubbleImage.alt = "Band";
                senderBubbleImage.style = "width: 40px; height:40px;";
                senderBubbleDetails.appendChild(senderBubbleImage);
    
                const senderBubbleName = document.createElement("div");
                senderBubbleName.className = "font-weight-bold mb-1";
                senderBubbleName.innerText = element.band_name
                senderBubbleDetails.appendChild(senderBubbleName);

                // responseData.messages.forEach((element) => {
                //     const senderMessageContent = document.createElement("div");
                //     senderMessageContent.className = "flex-shrink-1 bg-primary rounded py-2 px-3 ml-3";
                //     if (element.sender_type == "Band") {
                //         senderMessageContent.innerText = element.message;
                //         senderBubble.appendChild(senderMessageContent);
                //     }
                // });

                responseData.messages.forEach((element) => {
                    const recipientMessageContent = document.createElement("div");
                    recipientMessageContent.className = "flex-shrink-1 bg-primary rounded py-2 px-3 mr-3";
                    if (element.sender_type == "Venue") {
                        recipientMessageContent.innerText = element.message;
                        recipientBubble.appendChild(recipientMessageContent);
                    }

                    const senderMessageContent = document.createElement("div");
                    senderMessageContent.className = "flex-shrink-1 bg-primary rounded py-2 px-3 ml-3";
                    senderMessageContent.id = element.message_id;
                    if (element.sender_type == "Band") {
                        senderMessageContent.innerText = element.message;
                        senderBubble.appendChild(senderMessageContent);
                    }
                });

                // Sorting my messages
                let sortedMessages = [];
                let divs = document.getElementsByClassName("flex-shrink-1 bg-primary rounded py-2 px-3 ml-3");
                for (let i=0; i < divs.length; i++) {
                    sortedMessages.push(divs.item(i));
                }
                sortedMessages.sort( (a, b) => {
                    let compA = a.getAttribute("id");
                    let compB = b.getAttribute("id");
                    retrun (compA < compB) ? -1 : (compA > compB) ? 1 : 0;
                });
                for (let i = 0; i < sortedMessages.length; i++) {
                    recipientBubbleDiv.appendChild(sortedMessages[i]);
                }
            });
        });
    })
})

