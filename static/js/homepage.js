'use strict';

/////// Sign Up Button Functionality ///////
let signUpButton = document.getElementById("homepage-signup-button");

signUpButton.addEventListener("click", () => {
    window.location.href = "/signup";
})

/////// Log In Button Functionality ///////
let logInButton = document.getElementById("homepage-login-button");

logInButton.addEventListener("click", () => {
    window.location.href = "/login"
})