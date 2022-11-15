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

function initMap() {
    // The location of Uluru
    const venue = { lat: 40.750512900000004, lng: -73.99351594545152};
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 4,
      center: venue,
    });
    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
      position: venue,
      map: map,
    });
  }
  
  window.initMap = initMap;