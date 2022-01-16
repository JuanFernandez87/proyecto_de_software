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

function showPopUp() {
    $('.popupConfirmation').show();
}