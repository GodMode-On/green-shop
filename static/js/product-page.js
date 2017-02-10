$(document).ready(function() {
    $('#id_child_id').val(location.pathname);
});


$('#id_child_id').bind('change', function () {
    var url = $(this).val();
    if (url != '') {
        window.location = url;
    }
    return false;
})