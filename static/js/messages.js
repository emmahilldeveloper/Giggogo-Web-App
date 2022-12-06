'use strict';

/////// Message Functionality ///////

let message = document.getElementById("message");

let allMessageButtons = document.querySelectorAll("#message");

allMessageButtons.forEach((element) => {
    element.addEventListener("click", (evt) => {
        // evt.preventDefault(); // Add this back in if you want to click "Send and not have refresh."
    
        document.getElementById("message-details").innerHTML = "";
        const messageRecipient = element.getAttribute('value');
    
        let recipientID = element.getAttribute('value');
        console.log(recipientID);

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
    
                if (element.current_user == "Band") {
                    // When user clicks on message venue button, shows venue image
                    const messageRecipientImage = document.createElement("img");
                    messageRecipientImage.src = element.venue_logo;
                    messageRecipientImage.className = "square mr-1";
                    messageRecipientImage.alt = "Venue";
                    messageRecipientImage.style = "width: 40px; height:40px;";
                    messageAlignDiv.appendChild(messageRecipientImage);
        
                    // When user clicks on message venue button, shows venue name
                    const messageRecipientName = document.createElement("div");
                    // document.getElementById("hidden-message-recipient").value = element.venue_id;
                    messageRecipientName.className = "flex-grow-1 pl-3";
                    messageRecipientName.innerText = element.venue_name;
                    messageAlignDiv.appendChild(messageRecipientName);

                    // All chat bubbles
                    const chatBubbleRecipient = document.createElement("div");
                    chatBubbleRecipient.className = "position-relative";
                    parentDiv.appendChild(chatBubbleRecipient);
        
                    // div for all chat bubbles
                    const recipientBubbleDiv = document.createElement("div");
                    recipientBubbleDiv.className = "chat-messages";
                    chatBubbleRecipient.appendChild(recipientBubbleDiv);




                    // Shows the text input form to send a message
                    const form = document.createElement("form");
                    form.action = `/messages/${ element.current_user_id }`;
                    form.method = "POST";
                    form.className = "signup-form";
                    form.name = "sign-up-form";
                    parentDiv.appendChild(form);

                    const formDivBorder = document.createElement("div");
                    formDivBorder.className = "flex-grow-0 py-3 px-4 border-top";
                    form.appendChild(formDivBorder);

                    const formDivInput = document.createElement("div");
                    formDivInput.className = "input-group";
                    formDivInput.name = "";
                    formDivBorder.appendChild(formDivInput);

                    const input = document.createElement("input");
                    input.type = "text";
                    input.name = "message-text";
                    input.style = "border-radius: 20px; border-color: black;";
                    input.className = "form-control";
                    input.placeholder ="Type your message...";
                    formDivInput.appendChild(input);

                    const button = document.createElement("button");
                    button.className = "btn btn-primary";
                    button.style = "border-radius: 20px; margin: 30px;";
                    button.type = "submit";
                    button.innerText = "Send";
                    formDivInput.appendChild(button);

                    const inputHidden = document.createElement("input");
                    inputHidden.style = "display: None;";
                    inputHidden.name = "hidden-message-recipient";
                    inputHidden.id = "hidden-message-recipient";
                    inputHidden.value = recipientID;
                    formDivInput.appendChild(inputHidden);




                    responseData.messages.forEach((element) => {
                        // Styles the venue messages differently
                        if (element.sender_type == "Venue") {
                            const recipientMessageContent = document.createElement("div");
                            recipientMessageContent.className = "py-2 px-3 venue";
                            recipientMessageContent.style = "background-color: #d3d3d3; border-radius: 20px; margin: 20px; text-align: left;"
                            recipientMessageContent.innerText = element.message;
                            recipientMessageContent.id = element.message_id;
                            recipientBubbleDiv.appendChild(recipientMessageContent);
                        }
                        // Styles the band messages differently
                        if (element.sender_type == "Band") {
                            const senderMessageContent = document.createElement("div");
                            senderMessageContent.className = "py-2 px-3 band";
                            senderMessageContent.id = element.message_id;
                            senderMessageContent.style = "background-color: #248bf5; border-radius: 20px; margin: 20px; text-align: right;"
                            senderMessageContent.innerText = element.message;
                            recipientBubbleDiv.appendChild(senderMessageContent);
                            }
                        });
                    }

                if (element.current_user == "Venue") {
                    // When the user is a venue, will show band images
                    const messageRecipientImage = document.createElement("img");
                    messageRecipientImage.src = element.band_logo;
                    messageRecipientImage.className = "square mr-1";
                    messageRecipientImage.alt = "Band";
                    messageRecipientImage.style = "width: 40px; height:40px;";
                    messageAlignDiv.appendChild(messageRecipientImage);
        
                    // Will also show band names
                    const messageRecipientName = document.createElement("div");
                    document.getElementById("hidden-message-recipient").value = element.band_id;
                    messageRecipientName.className = "flex-grow-1 pl-3";
                    messageRecipientName.innerText = element.band_name;
                    messageAlignDiv.appendChild(messageRecipientName);
        
                    //  All chat bubbles
                    const chatBubbleRecipient = document.createElement("div");
                    chatBubbleRecipient.className = "position-relative";
                    parentDiv.appendChild(chatBubbleRecipient);
        
                    // Contains all chat bubbles between two parties
                    const recipientBubbleDiv = document.createElement("div");
                    recipientBubbleDiv.className = "chat-messages p-4";
                    chatBubbleRecipient.appendChild(recipientBubbleDiv);

                    responseData.messages.forEach((element) => {

                        if (element.sender_type == "Venue") {
                            const recipientMessageContent = document.createElement("div");
                            recipientMessageContent.className = "py-2 px-3 venue";
                            recipientMessageContent.innerText = element.message;
                            recipientMessageContent.style = "background-color: #248bf5; border-radius: 20px; margin: 20px; text-align: right;"
                            recipientMessageContent.id = element.message_id;
                            recipientBubbleDiv.appendChild(recipientMessageContent);
                        }

                        if (element.sender_type == "Band") {
                            const senderMessageContent = document.createElement("div");
                            senderMessageContent.className = "py-2 px-3 band";
                            senderMessageContent.style = "background-color: #d3d3d3; border-radius: 20px; margin: 20px; text-align: left;"
                            senderMessageContent.id = element.message_id;
                            senderMessageContent.innerText = element.message;
                            recipientBubbleDiv.appendChild(senderMessageContent);
                        }
                    });
                }
            });
        });
    });
});