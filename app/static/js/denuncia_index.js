$(window).load(function () {
    $('.popupConfirmation').click(function () {
        $('.popupConfirmation').hide();
    });
    $('.popupCloseButton').click(function () {
        $('.popupConfirmation').hide();
    });
    $('.cancelButton').click(function () {
        $('.popupConfirmation').hide();
    });

    $('input[type=search]').on('search', function () {
        $(".searchBtn").click();
        return false;
    });
});

function deleteDenuncia(id) {
    $('.popupConfirmation').show();
    $('#denuncia_to_delete').val(id);
}
    