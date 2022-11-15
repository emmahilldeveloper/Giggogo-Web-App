'use strict';

/////// Update User Data ///////

// let editButton = document.getElementById("edit-user-data");
// let parentDiv = document.getElementById("information-row");

// editButton.addEventListener("click", (evt) => {
//     evt.preventDefault();

//     parentDiv.innerHTML = "";

//     const form = document.createElement("form")
//     form.action("/user/<user_id>");
//     form.method("POST");
//     form.class("edit-user-data");
//     parentDiv.appendChild(form);

//     const formattingDiv = document.createElement("div");
//     formattingDiv1.class("mx-auto");
//     formattingDiv1.style("width: 200px;");
//     form.appendChild(formattingDiv);

//     // Form for Profile Photo URL
//     const formattingDivPhoto = document.createElement("div");
//     formattingDivPhoto.class("col-5 col-md-3 order-md-1");
//     formattingDiv.appendChild(formattingDivPhoto);

//     const profilePhotoURLdiv = document.createElement("div");
//     profilePhotoURLdiv.class("form-floating mb-3");
//     profilePhotoURLdiv.style("width: 250px;");
//     formattingDivPhoto.appendChild(profilePhotoURLdiv);

//     const profilePhotoURL = document.createElement("input");
//     profilePhotoURL.class("form-control");
//     profilePhotoURL.id("floatingInput");
//     profilePhotoURL.type("text");
//     profilePhotoURL.name("profile-photo");
//     profilePhotoURL.placeholder("Photo URL");
//     profilePhotoURLdiv.appendChild(profilePhotoURL);

//     const profilePhotoURLLabel = document.createElement("label");
//     profilePhotoURLLabel.for("floatingInput");
//     profilePhotoURLLabel.innerText = "Profile Photo URL";
//     profilePhotoURLdiv.appendChild(profilePhotoURLLabel);

//     // Form for First Name
//     const formattingDivFirstName = document.createElement("div");
//     formattingDivFirstName.class("col-5 col-md-3 order-md-1");
//     formattingDiv.appendChild(formattingDivFirstName);

//     const firstNameDiv = document.createElement("div");
//     firstNameDiv.class("form-floating mb-3");
//     firstNameDiv.style("width: 250px;");
//     formattingDivFirstName.appendChild(firstNameDiv);

//     const firstName = document.createElement("input");
//     firstName.class("form-control");
//     firstName.id("floatingInput");
//     firstName.type("text");
//     firstName.name("first-name");
//     firstName.placeholder("First Name");
//     firstNameDiv.appendChild(firstName);

//     const firstNameLabel = document.createElement("label");
//     firstNameLabel.for("floatingInput");
//     firstNameLabel.innerText = "First Name";
//     firstNameDiv.appendChild(firstNameLabel);

//     // Form for Last Name
//     const formattingDivLastName = document.createElement("div");
//     formattingDivLastName.class("col-5 col-md-3 order-md-1");
//     formattingDiv.appendChild(formattingDivLastName);

//     const lastNameDiv = document.createElement("div");
//     lastNameDiv.class("form-floating mb-3");
//     lastNameDiv.style("width: 250px;");
//     formattingDivLastName.appendChild(lastNameDiv);

//     const lastName = document.createElement("input");
//     lastName.class("form-control");
//     lastName.id("floatingInput");
//     lastName.type("text");
//     lastName.name("last-name");
//     lastName.placeholder("Last Name");
//     lastNameDiv.appendChild(lastName);

//     const lastNameLabel = document.createElement("label");
//     lastNameLabel.for("floatingInput");
//     lastNameLabel.innerText = "Last Name";
//     lastNameDiv.appendChild(lastNameLabel);

//     // Form for Email
//     const formattingDivEmail = document.createElement("div");
//     formattingDivEmail.class("col-5 col-md-3 order-md-1");
//     formattingDiv.appendChild(formattingDivEmail);

//     const emailDiv = document.createElement("div");
//     emailDiv.class("form-floating mb-3");
//     emailDiv.style("width: 250px;");
//     formattingDivLastName.appendChild(emailDiv);

//     const email = document.createElement("input");
//     email.class("form-control");
//     email.id("floatingInput");
//     email.type("text");
//     email.name("email");
//     email.placeholder("Email");
//     emailDiv.appendChild(email);

//     const emailLabel = document.createElement("label");
//     emailLabel.for("floatingInput");
//     emailLabel.innerText = "Email";
//     emailDiv.appendChild(emailLabel);

//     //Save New User Data
//     const saveButton = document.createElement("a");
//     saveButton.className = "btn btn-primary";
//     saveButton.innerHTML= "Save";
//     saveButton.type = "click";
//     formattingDiv.appendChild(saveButton);

//     saveButton.addEventListener("click", () => {

//         const data = {
//             profile_photo: document.getElementsByName("profile-photo").value,
//             first_name: document.getElementByName("first-name").value,
//             last_name: document.getElementByName("last-name").value,
//             email: document.getElementByName("email").value,
//         };

//         fetch(`/api/user`, {
//             method: 'POST',
//             body: JSON.stringify(data),
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//         })
//         .then((response) => response.json())
//         .then(responseData => {
//             //here something
//     });
// });
// });