'use strict';

/////// Search Button Functionality ///////
let searchButton = document.getElementById("search");
let clearButton = document.getElementById("clear");

if (document.getElementById("venue-search-result-div").innerText == "") {
    document.getElementById("venue-search-result-div").innerText = "No results."
}

clearButton.addEventListener("click", () => {});

searchButton.addEventListener("click", (evt) => {
    evt.preventDefault();

    document.getElementById("venue-search-result-div").innerHTML = "";

    let genres = document.getElementsByClassName("genre-select");

    let genre_ids = [];

    for (let genre of genres) {
        if (genre.checked) {
            genre_ids.push(genre.value)
        }
    }

    let data = {
        low: document.getElementById("low-payrate").checked,
        med: document.getElementById("med-payrate").checked,
        medhigh: document.getElementById("med-high-payrate").checked,
        high: document.getElementById("high-payrate").checked,
        genre: genre_ids,
    };

    fetch(`/api/bandsearch`, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then((response) => response.json())
    .then(responseData => {
        responseData.matches.forEach((element) => {

            //Create parent div to house all venue search results
            const parentDiv = document.getElementById("venue-search-result-div");

            //Venue div for each individual venue in the loop
            const venueDivCard = document.createElement("div");
            venueDivCard.className = "card";
            venueDivCard.style = "width:18rem;";
            venueDivCard.id = "band-search-result";
            parentDiv.appendChild(venueDivCard);

            //Shows the venue logo
            const venueLogo = document.createElement("img");
            venueLogo.className = "card-img-top";
            venueLogo.alt = "Card image cap";
            venueLogo.id = "band-search-result-img";
            venueLogo.src = element.venue_logo;
            venueDivCard.appendChild(venueLogo);

            //Another venue div inside initial band div
            const venueDivCardBody = document.createElement("div");
            venueDivCardBody.className = "card-body";
            venueDivCard.appendChild(venueDivCardBody);

            //Shows the venue name
            const venueNameCardTitle = document.createElement("h5");
            venueNameCardTitle.className = "card-title";
            venueNameCardTitle.innerText = element.venue_name;
            venueDivCardBody.appendChild(venueNameCardTitle);

            //Show details button
            const venueLink = document.createElement("a");
            venueLink.className = "btn btn-primary";
            venueLink.innerHTML= "Venue Details";
            venueLink.type = "click";
            venueLink.setAttribute("href",`/venuehome/${element.venue_id}`);
            venueDivCardBody.appendChild(venueLink);
        })
    });
})