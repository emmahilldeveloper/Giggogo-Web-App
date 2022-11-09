'use strict';

/////// Spotify Functionality ///////

//here eventually

/////// Book Gig Button Functionality ///////

let bandBookButton = document.getElementById("book-band-button");
let currentVisibility = bandBookButton.style.display;

let band = document.getElementById("band");
let venue = document.getElementById("venue");

function showBookButton() {
    if(venue) {
        bandBookButton.style.display = 'block';
    }
    else {
        bandBookButton.style.display = 'none';
    }
}

window.onload = showBookButton;