$(document).ready(function () {
    if (window.location.hash.startsWith('#updateEventModal')) {
        $('#updateEventModal').modal('show');
    }
    
    // Handle the update event form submission via fetch
    $('#updateEventForm').submit(function (event) {
        event.preventDefault();

        let formData = new FormData(this);
        let eventId = $('#updateEventForm').data('event-id');

        fetch(`/dashboard/update/${eventId}`, {
            method: 'POST',
            body: formData,
        })
            .then((res) => res.json())
            .then((data) => {
                if (data.success) {
                    window.location.reload();
                } else {
                    $('#updateAlertMessage')
                        .removeClass('d-none')
                        .addClass('alert-danger')
                        .html(data.message);
                }
            })
            .catch((err) => {
                $('#updateAlertMessage')
                    .removeClass('d-none')
                    .addClass('alert-danger')
                    .html('An error occurred. Please try again.');
            });
    });

    // Pre-fill the modal with event data when the update button is clicked
    $('.update-event-button').on('click', function () {
        let eventId = $(this).data('event-id');
        let eventName = $(this).data('event-name');
        let eventLocation = $(this).data('event-location');
        let eventDate = $(this).data('event-date');
        let eventEnd = $(this).data('event-end');
        let eventDescription = $(this).data('event-description');

        // Set form data in the modal
        $('#updateEventForm').data('event-id', eventId);
        $('#updateEventModal #event_name').val(eventName);
        $('#updateEventModal #event_location').val(eventLocation);
        $('#updateEventModal #event_date').val(eventDate);
        $('#updateEventModal #event_end').val(eventEnd);
        $('#updateEventModal #event_description').val(eventDescription);
        $('#updateEventModal #thumbnail').val(''); // Clear the thumbnail input

        // Show the modal
        $('#updateEventModal').modal('show');
    });
});
