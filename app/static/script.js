/**
 * script.js
 * ---------
 * Contains frontend JavaScript logic for interacting with the DOM.
 * Includes user interactions, file uploads, and making API calls
 * to the backend.
 */

// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    // Select the button by its id
    const button = document.getElementById("myButton");

    // Add a click event listener to the button
    button.addEventListener("click", () => {
        // Add the logic you want here
        console.log("Button was clicked!");
        alert("Button Clicked!"); // Example: Show an alert
    });
});
