$(document).ready(function () {
    if (window.location.hash === '#registerModal') {
        $('#registerModal').modal('show');
    }

    $('#registerForm').submit(function (event) {
        event.preventDefault();

        let formData = new FormData(this);
        let pwd = formData.get('password');
        let confirmPwd = formData.get('confirm_password');

        if (pwd !== confirmPwd) {
            $('#registerAlertMessage')
                .removeClass('d-none')
                .addClass('alert-danger')
                .html('Passwords must match.');
                return;
        }

        fetch(urlRegister, {
            method: 'POST',
            body: formData
        })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                $('#registerAlertMessage')
                    .removeClass('d-none alert-danger')
                    .addClass('alert-success')
                    .html(data.message);

                setTimeout(function () {
                    $('#registerModal').modal('hide');
                    $('#loginModal').modal('show');
                }, 5000);

            } else {
                $('#registerAlertMessage')
                    .removeClass('d-none')
                    .addClass('alert-danger')
                    .html(data.message);
            }
        })
        .catch(err => {
            $('#registerAlertMessage')
                .removeClass('d-none')
                .addClass('alert-danger')
                .html('An error occurred. Please try again.');
        });
    });
});
