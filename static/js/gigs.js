'use strict';

/////// Edit Gig Button Functionality ///////

let allGigEditButtons = document.querySelectorAll(".edit-gig");

allGigEditButtons.forEach((element) => {
    element.addEventListener("click", () => {

        const gigID = element.getAttribute('value');

        window.location.href = `/editgig/${gigID}`;
    });
});

const testChart = new Chart(
      document.querySelector('#test-chart'),
      {
        type: 'line',
        data: {
          labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'],
          datasets: [
            {data: [20000, 50000, 8000, 45000, 34023, 15000, 34000, 20500, 55000, 29500, 43000, 12000]}
          ]
        }
      }
    );