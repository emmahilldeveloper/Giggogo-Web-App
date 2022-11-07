'use strict';

/////// Search Button Functionality ///////
let searchButton = document.getElementById("search");

function onClick(evt) {
    evt.preventDefault();
    low = document.getElementById("low-payrate");
    med = document.getElementById("med-payrate");
    medhigh = document.getElementById("med-high-payrate");
    high = document.getElementById("high-payrate");

    let payrate = document.getElementById("payrate").value;


    // data = {
    //     low: low.checked,
    //     med: med.checked,
    //     med_high: medhigh.checked,
    //     high: high.checked
    // }

    fetch(`/ap(i/search?payrate=${payrate}`)
        .then((response) => response.json())
        .then(jsonData => {
            document.getElementById("band-search-result-div").innerHTML = 
            // DOM elements

        });
}

searchButton.addEventListener("click", onClick(evt));