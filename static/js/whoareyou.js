'use strict';

/////// Sign Up Button Functionality ///////
let bandButton = document.getElementById("band");
let venueButton = document.getElementById("venue");

bandButton.addEventListener("click", () => {
    window.location.href = "/band";
})

venueButton.addEventListener("click", () => {
    window.location.href = "/venue";
})

