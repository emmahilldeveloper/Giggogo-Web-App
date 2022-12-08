'use strict';

/////// Edit Gig Button Functionality ///////

let allGigEditButtons = document.querySelectorAll(".edit-gig");

allGigEditButtons.forEach((element) => {
    element.addEventListener("click", () => {

        const gigID = element.getAttribute('value');

        window.location.href = `/editgig/${gigID}`;
    });
});


window.addEventListener("load", (evt) => {

  evt.preventDefault();

  let bandID = document.getElementById("venue-gig-card").getAttribute('value');

  let data = {
    bandID: bandID
  }

  fetch(`/api/sales`, {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
        'Content-Type': 'application/json'
    },
  })
  .then((response) => response.json())
  .then(responseData => {

      let january = 0
      let february = 0
      let march = 0
      let april = 0
      let may = 0
      let june = 0
      let july = 0
      let august = 0
      let september = 0
      let october = 0
      let november = 0
      let december = 0

    responseData.sales.forEach((element) => {

      if (element.jan) {
        let janSum = element.jan.reduce((accumulator, value) => {
          return accumulator + value;
        }, 0);

        january = janSum
      }

      else if (element.feb) {
        let febSum = element.feb.reduce((accumulator, value) => {
          return accumulator + value;
        }, 0);

        february = febSum
      }

      else if (element.mar) {
        let marSum = element.mar.reduce((accumulator, value) => {
          return accumulator + value;
        }, 0);

        march = marSum
      }

      else if (element.apr) {
        let aprSum = element.apr.reduce((accumulator, value) => {
          return accumulator + value;
        }, 0);

        april = aprSum
      }

      else if (element.may) {
        let maySum = element.may.reduce((accumulator, value) => {
          return accumulator + value;
        }, 0);

        may = maySum
      }

      else if (element.jun) {
        let junSum = element.jun.reduce((accumulator, value) => {
          return accumulator + value;
        }, 0);

        june = junSum
      }

      else if (element.jul) {
        let julSum = element.jul.reduce((accumulator, value) => {
          return accumulator + value;
        }, 0);

        july = julSum
      }

      else if (element.aug) {
        let augSum = element.aug.reduce((accumulator, value) => {
          return accumulator + value;
        }, 0);

        august = augSum
      }

      else if (element.sept) {
        let septSum = element.sept.reduce((accumulator, value) => {
          return accumulator + value;
        }, 0);

        september = septSum
      }

      else if (element.oct) {
        let octSum = element.oct.reduce((accumulator, value) => {
          return accumulator + value;
        }, 0);

        october = octSum
      }
      else if (element.nov) {
        let novSum = element.nov.reduce((accumulator, value) => {
          return accumulator + value;
        }, 0);

        november = novSum
      }

      else if (element.dec) {
        let decSum = element.dec.reduce((accumulator, value) => {
        return accumulator + value;
      }, 0);

        december = decSum
      }
    });

    const testChart = new Chart(
      document.querySelector('#test-chart'),
      {
        type: 'line',
        data: {
          labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'],
          datasets: [
            {
              label: 'Gig Sales',
              data: [january, february, march, april, may, june, july, august, september, october, november, december],
            }
          ]
        },
        options: {
          legend: {
            position: "right",
          }
        }
      }
    );

});
});