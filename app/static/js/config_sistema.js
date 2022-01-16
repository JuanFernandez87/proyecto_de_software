$(window).load(function () {
    $('.popupConfirmation').click(function(){
        $('.popupConfirmation').hide();
    });
    $('.popupCloseButton').click(function(){
        $('.popupConfirmation').hide();
    });
    $('.cancelButton').click(function(){
        $('.popupConfirmation').hide();
    });

    $('.popupCancelar').click(function(){
        $('.popupConfirmation').hide();
    });

    $(".resetBtn").click(function(){
        $(".searchInput").val('');
        $(".searchBtn").click(); 
        return false;
    });
});

function uptadeConfig() {
    $('.popupConfirmation').show();
}