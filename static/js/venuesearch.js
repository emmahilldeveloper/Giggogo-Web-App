'use strict';

/////// Search Button Functionality ///////
let searchButton = document.getElementById("search");

searchButton.addEventListener("click", (evt) => {
    evt.preventDefault();

    const data = {
        low: document.getElementById("low-payrate").checked,
        med: document.getElementById("med-payrate").checked,
        medhigh: document.getElementById("med-high-payrate").checked,
        high: document.getElementById("high-payrate").checked,
    };

    fetch(`/api/search`, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then((response) => response.json())
    .then(responseData => {
        document.getElementById("band-search-result-div").innerHTML = responseData[1]
    });
})