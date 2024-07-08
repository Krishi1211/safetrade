document.addEventListener('DOMContentLoaded', (event) => {
    // Check if disclaimer has been shown before
    if (!localStorage.getItem('disclaimerShown')) {
        // Show the disclaimer
        document.getElementById('disclaimer').style.display = 'block';
        document.querySelector('.content').style.filter = 'blur(5px)';
    }

    // Agree button functionality
    document.getElementById('agree-button').addEventListener('click', function() {
        document.getElementById('disclaimer').style.display = 'none';
        let elements = document.getElementsByClassName('rest');
        for (let i = 0; i < elements.length; i++) {
            elements[i].style.opacity = '1';
        }
        document.querySelector('.content').style.filter = 'none';
        // Set local storage to remember that disclaimer has been shown
        localStorage.setItem('disclaimerShown', 'true');
    });

    // Don't Agree button functionality
    document.getElementById('dont-agree-button').addEventListener('click', function() {
        window.history.back(); // Redirect to the previous page
    });
});
