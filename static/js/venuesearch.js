'use strict';

/////// Search Button Functionality ///////
let searchButton = document.getElementById("search");
let clearButton = document.getElementById("clear");

clearButton.addEventListener("click", () => {});

if (document.getElementById("band-search-result-div").innerText == "") {
    document.getElementById("band-search-result-div").innerText = "No results."
}

searchButton.addEventListener("click", (evt) => {
    evt.preventDefault();

    document.getElementById("band-search-result-div").innerHTML = "";

    let genres = document.getElementsByClassName("genre-select");

    let genre_ids = [];

    for (let genre of genres) {
        if (genre.checked) {
            genre_ids.push(genre.value)
        }
    }

    let sizes = document.getElementsByClassName("size-select");

    let band_sizes = [];

    for (let size of sizes) {
        if (size.checked) {
            band_sizes.push(size.value)
        }
    }

    const data = {
        low: document.getElementById("low-payrate").checked,
        med: document.getElementById("med-payrate").checked,
        medhigh: document.getElementById("med-high-payrate").checked,
        high: document.getElementById("high-payrate").checked,
        genre: genre_ids,
        size: band_sizes,
    };

    fetch(`/api/venuesearch`, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then((response) => response.json())
    .then(responseData => {

        responseData.matches.forEach((element) => {

            //Create parent div to house all band search results
            const parentDiv = document.getElementById("band-search-result-div");
            parentDiv.style = "text-align: center;";

            //Band div for each individual band in the loop
            const bandDivCard = document.createElement("div");
            bandDivCard.className = "card";
            bandDivCard.style = "width:18rem; background-color: #d3d3d3; border-color: black; border-radius: 20px; display: inline-block; margin: 20px;";
            bandDivCard.id = "band-search-result";
            parentDiv.appendChild(bandDivCard);

            //Shows the band logo
            const bandLogo = document.createElement("img");
            bandLogo.className = "card-img-top";
            bandLogo.alt = "Card image cap";
            bandLogo.id = "band-search-result-img";
            bandLogo.src = element.band_logo;
            bandLogo.style = "border-color: black; border-radius: 20px 20px 0px 0px; object-fit: cover; width: 286px; height: 286px;";
            bandDivCard.appendChild(bandLogo);

            //Another band div inside initial band div
            const bandDivCardBody = document.createElement("div");
            bandDivCardBody.className = "card-body";
            bandDivCard.appendChild(bandDivCardBody);

            //Shows the band name
            const bandNameCardTitle = document.createElement("h5");
            bandNameCardTitle.className = "card-title";
            bandNameCardTitle.innerText = element.band_name;
            bandDivCardBody.appendChild(bandNameCardTitle);

            //Book Gig Button
            const bandLink = document.createElement("a");
            bandLink.className = "btn btn-primary";
            bandLink.innerHTML= "Band Details";
            bandLink.type = "click";
            bandLink.style = "text-align: left;";
            bandLink.setAttribute("href",`/bandhome/${element.band_id}`);
            bandDivCardBody.appendChild(bandLink);
        })
    });
})