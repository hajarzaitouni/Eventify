$(document).ready(function () {
    if (window.location.hash === '#loginModal') {
        $('#loginModal').modal('show');
    }

    $('#loginForm').submit(function(event) {
        event.preventDefault();
        
        let formData = new FormData(this);

        fetch(urlLogin, {
            method: 'POST',
            body: formData
        })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                window.location.href = urlDashboard;
            } else {
                $('#alertMessage')
                    .removeClass('d-none')
                    .addClass('alert-danger')
                    .html(data.message);
            }
        })
        .catch(err => {
            $('#alertMessage')
                .removeClass('d-none')
                .addClass('alert-danger')
                .html('An error is occurred. Please try again.');
        });
    });
});