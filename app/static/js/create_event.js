$(document).ready(function () {
    if (window.location.hash === '#createEventModal') {
        $('#createEventModal').modal('show');
    }
    const urlParams = new URLSearchParams(window.location.search);
    const show_modal = urlParams.get('show_modal');

    if (show_modal === 'true') {
        $('#createEventModal').modal('show');
    }

    $('#createEventForm').submit(function (event) {
        event.preventDefault();

        let formData = new FormData(this);

        fetch('/dashboard/create', {
            method: 'POST',
            body: formData,
        })
            .then((res) => res.json())
            .then((data) => {
                console.log('data :', data);
                if (data.success) {
                    window.location.reload();
                } else {
                    $('#createAlertMessage')
                        .removeClass('d-none')
                        .addClass('alert-danger')
                        .html(data.message);
                }
            })
            .catch((err) => {
                $('#createAlertMessage')
                    .removeClass('d-none')
                    .addClass('alert-danger')
                    .html('An error occurred. Please try again.');
            });
    });
});