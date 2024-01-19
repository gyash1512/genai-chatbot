document.addEventListener('DOMContentLoaded', function() {
    // Get the form element
    var contactForm = document.querySelector('form');

    // Add event listener for form submission
    contactForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        // You can perform additional validation here if needed

        // Call a function to handle form submission (e.g., send data to a server)
        handleFormSubmission();
    });

    // Function to handle form submission
    function handleFormSubmission() {
        // Retrieve form data
        var firstName = document.getElementById('firstName').value;
        var lastName = document.getElementById('lastName').value;
        var email = document.getElementById('email').value;
        var mobile = document.getElementById('mobile').value;
        var message = document.querySelector('textarea').value;

        // You can perform additional processing or send data to a server here
        // For demonstration purposes, let's log the form data to the console
        console.log('Form data:', {
            firstName: firstName,
            lastName: lastName,
            email: email,
            mobile: mobile,
            message: message
        });

        // Reset the form if needed
        contactForm.reset();
    }
});