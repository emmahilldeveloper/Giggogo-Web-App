'use strict';

/////// Book Gig Button Functionality ///////

let venueBookButton = document.getElementById("book-venue-button");
let currentVisibility = venueBookButton.style.display;

let venue = document.getElementById("venue");
let band = document.getElementById("band");

function showBookButton() {
    if(band) {
        venueBookButton.style.display = 'block';
    }
    else {
        venueBookButton.style.display = 'none';
    }
}

window.onload = showBookButton;