document.addEventListener('DOMContentLoaded', function() {
    const popupOverlay = document.getElementById('popup');
    const agreeBtn = document.getElementById('agreeBtn');
    const noThanksBtn = document.getElementById('noThanksBtn');
    const agreed = localStorage.getItem('disclaimerAgreed');

    if (!agreed) {
        popupOverlay.style.display = 'block';
    }

    agreeBtn.addEventListener('click', function() {
        localStorage.setItem('disclaimerAgreed', true);
        popupOverlay.style.display = '/home';
    });

    noThanksBtn.addEventListener('click', function() {
        // Redirect to the previously loaded page
        window.history.back();
    });

    // Check if the disclaimer has been agreed upon before navigating to other pages
    const links = document.querySelectorAll('a');
    links.forEach(link => {
        link.addEventListener('click', function(event) {
            if (!localStorage.getItem('disclaimerAgreed')) {
                event.preventDefault(); // Prevent default behavior (opening the link)
                popupOverlay.style.display = 'block'; // Show the disclaimer popup
            }
        });
    });
});