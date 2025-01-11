/**
 * script.js
 * ---------
 * Contains frontend JavaScript logic for interacting with the DOM.
 * Includes user interactions, file uploads, and making API calls
 * to the backend.
 */

document.addEventListener("DOMContentLoaded", () => {
    const greetButton = document.getElementById("myButton");

    // Function to send an action to the backend
    const sendAction = async (action) => {
        try {
            const response = await fetch('/api/action', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ action }),
            });

            const result = await response.json();
            alert(result.message); // Show the backend's response
        } catch (error) {
            console.error("Error:", error);
        }
    };

    // Add click listeners for each button
    greetButton.addEventListener("click", () => sendAction('greet'));
});
