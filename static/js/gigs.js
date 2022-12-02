'use strict';

/////// Edit Gig Button Functionality ///////

let allGigEditButtons = document.querySelectorAll(".edit-gig");

console.log(allGigEditButtons)

allGigEditButtons.forEach((element) => {
    element.addEventListener("click", () => {

        const gigID = element.getAttribute('value');

        window.location.href = `/editgig/${gigID}`;
    });
});