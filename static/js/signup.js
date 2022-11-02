'use strict';

/////// Upload Profile Photo Functionality ///////

// let profilePhotoDiv = document.getElementsByClassName("profile-photo");
// let profilePhoto = document.getElementById("profile-photo");
// let fileUpload = document.getElementById("profile-photo-file");
// let photoUploadButton = document.getElementById("profile-photo-upload-button");

// profilePhotoDiv.addEventListener("mouseenter", () => {
//     photoUploadButton.style.display = "block"
// });

// profilePhotoDiv.addEventListener("mouseleave", () => {
//     photoUploadButton.style.display = "none"
// });

// fileUpload.addEventListener("change", () => {
//     let selectedFile = this.filesUpload[0];
//     if (selectedFile) {
//         let reader = new FileReader();

//         reader.addEventListener("load", () => {
//             profilePhoto.setAttribute("src", reader.result);
//         });

//         reader.readAsDataURL(selectedFile);
//     }
// });

/////// Band Radio Button Functionality ///////

let radioBand = document.getElementById("signup-user-type-band");

radioBand.addEventListener("click", () => {
    document.getElementById("search-div-band").style.display = "";
    document.getElementById("or-band").style.display = "";
    document.getElementById("create-band-div").style.display = "";
    document.getElementById("create-band-name").style.display = "";
    document.getElementById("create-band-phone").style.display = "";
    document.getElementById("create-band-payrate").style.display = "";
    document.getElementById("create-band-logo").style.display = "";

    document.getElementById("search-div-venue").style.display = "none";
    document.getElementById("or-venue").style.display = "none";
    document.getElementById("create-venue-div").style.display = "none";
    document.getElementById("create-venue-name").style.display = "none";
    document.getElementById("create-venue-phone").style.display = "none";
    document.getElementById("create-venue-payrate").style.display = "none";
    document.getElementById("create-venue-address").style.display = "none";
    document.getElementById("create-venue-logo").style.display = "none";
})

radioBand.addEventListener("click", () => {
    document.getElementById("band-dropdown").style.display = "";
    document.getElementById("venue-dropdown").style.display = "none";
})



/////// Venue Radio Button Functionality ///////

let radioVenue = document.getElementById("signup-user-type-venue");

radioVenue.addEventListener("click", () => {
    document.getElementById("search-div-venue").style.display = "";
    document.getElementById("or-venue").style.display = "";
    document.getElementById("create-venue-div").style.display = "";
    document.getElementById("create-venue-name").style.display = "";
    document.getElementById("create-venue-phone").style.display = "";
    document.getElementById("create-venue-payrate").style.display = "";
    document.getElementById("create-venue-address").style.display = "";
    document.getElementById("create-venue-logo").style.display = "";

    document.getElementById("search-div-band").style.display = "none";
    document.getElementById("or-band").style.display = "none";
    document.getElementById("create-band-div").style.display = "none";
    document.getElementById("create-band-name").style.display = "none";
    document.getElementById("create-band-phone").style.display = "none";
    document.getElementById("create-band-payrate").style.display = "none";
    document.getElementById("create-band-logo").style.display = "none";
})

radioVenue.addEventListener("click", () => {
    document.getElementById("venue-dropdown").style.display = "";
    document.getElementById("band-dropdown").style.display = "none";
})


