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
    

});



function borrar(id) {
    $('.popupConfirmation').show();
    $('#punto_to_delete').val(id);
}
