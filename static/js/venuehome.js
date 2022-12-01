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

/////// Google Maps Functionality ///////

let lat = parseFloat(document.getElementById("lat").getAttribute('value'));
let lng = parseFloat(document.getElementById("lon").getAttribute('value'));

console.log(lat)
console.log(lng)

function initMap() {
    // The location of Uluru
    const venue = { lat: lat, lng: lng };
    // The map, centered at venue
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 18,
      center: venue,
    });
    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
      position: venue,
      map: map,
    });
  }
  
  window.initMap = initMap;