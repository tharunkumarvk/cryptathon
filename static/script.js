document.getElementById("prediction-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    // Get the input data, which should be comma-separated values
    const inputData = document.getElementById("feature-inputs").value.split(',').map(Number);

    // Validate that the input contains exactly 9 features
    if (inputData.length !== 9) {
        alert("Please enter exactly 9 numeric features.");
        return;
    }

    // Show the loading spinner
    document.getElementById("loading-spinner").style.display = "block";

    try {
        // Send the input data to the backend via POST request
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ input_data: inputData }),
        });

        // Parse the JSON response from the backend
        const result = await response.json();

        // Hide the loading spinner once the response is received
        document.getElementById("loading-spinner").style.display = "none";

        // Display the prediction result (status and message)
        document.getElementById("result").innerText = `Status: ${result.status}, Message: ${result.message}`;

        // If the status is 'safe', show the encrypted data and HMAC
        if (result.status === "safe") {
            document.getElementById("encrypted_data").innerText = `Encrypted Data: ${result.encrypted_data}`;
            document.getElementById("hmac").innerText = `HMAC: ${result.hmac}`;
        } else {
            // If the status is 'blocked', clear the encrypted data and HMAC
            document.getElementById("encrypted_data").innerText = '';
            document.getElementById("hmac").innerText = '';
        }
    } catch (error) {
        // Hide the loading spinner in case of an error
        document.getElementById("loading-spinner").style.display = "none";
        alert("An error occurred while processing your request. Please try again.");
    }
});
