'use strict';

/////// Add Band or Find Band Buttons ///////
let addVenueButton = document.getElementById("addvenue");
let findVenueButton = document.getElementById("findvenue");

addVenueButton.addEventListener("click", () => {
    window.location.href = "/newvenue";
})

findVenueButton.addEventListener("click", () => {
    window.location.href = "/findvenue";
})
