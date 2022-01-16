$(window).load(function () {
  $(".popupConfirmation").click(function () {
    $(".popupConfirmation").hide();
  });
  $(".popupCloseButton").click(function () {
    $(".popupConfirmation").hide();
  });
  $(".cancelButton").click(function () {
    $(".popupConfirmation").hide();
  });

  $("input[type=search]").on("search", function () {
    $(".searchBtn").click();
    return false;
  });

  /** Cargo en el inpur de color, el color de capa seleccionado. */
  $("#color-input").val($("#color_capa").val());


});

function deleteZona(id) {
  $(".popupConfirmation").show();
  $("#zone_to_delete").val(id);
}

/** Llamo a la funcion que me devuelve un nuevo código */
function generarHash() {          
  $.ajax({
      url: '/Zonas/GenerarCodigo',
      type: 'GET',
      success: function (response) {
        $("#code").val(response);
      },
      error: function (error) {
          console.log(error);
      }
   });
}

/**  Setea el color seleccionado en el input de colores. */
function setColor(t) {
  $("#color_capa").val(t.value);
}

$(document).ready(function() {
  $("body").tooltip({ selector: '[data-toggle=tooltip]' });
});

