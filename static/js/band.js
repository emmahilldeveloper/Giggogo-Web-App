'use strict';

/////// Sign Up Button Functionality ///////
let addBandButton = document.getElementById("addband");
let findBandButton = document.getElementById("findband");

addBandButton.addEventListener("click", () => {
    window.location.href = "/newband";
})

findBandButton.addEventListener("click", () => {
    window.location.href = "/findband";
})

