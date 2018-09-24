    $("#entity").change(function () {
      var entity = $(this).val();
      sendAjaxP1(entity)
      sendAjaxP2(entity)
      init();
    });
  function sendAjaxP1(entity){
          $.ajax({
        url: "/campaign/ajax/p1",
        data: {
          'data': entity  
        },
        success: function (data) {
          $("#id_p1").html(data);
          // $("#id_p1").next("button").next("div").children("div[class='inner show']").children("ul").html("<li>fsfsfsf</li>")
          $("#id_p2").children().remove()
          $("#id_m3").children().remove()
          $("#id_m4").children().remove()
          $("#id_m5").children().remove()
          $("#id_m6").children().remove()
        }
      });

  }
    function sendAjaxP2(entity){
          $.ajax({
        url: "/campaign/ajax/p1_inner",
        data: {
          'data': entity  
        },
        success: function (data) {
          // $("#id_p1").html(data);
          $("#id_p1").next("button").next("div").children("div[class='inner show']").children("ul").html(data)
          $("#id_p2").children().remove()
          $("#id_m3").children().remove()
          $("#id_m4").children().remove()
          $("#id_m5").children().remove()
          $("#id_m6").children().remove()
        }
      });

  }

    $("#id_p1").change(function () {
      var p1 = $(this).val();
      $.ajax({
        url: "/campaign/ajax/p2",
        data: {
          'data': p1
        },
        success: function (data) {
          $("#id_p2").html(data);
          $("#id_m3").children().remove()
          $("#id_m4").children().remove()
          $("#id_m5").children().remove()
          $("#id_m6").children().remove()
        }
      });
    });
    $("#id_p2").change(function () {
      var p2 = $(this).val();
      $.ajax({
        url: "/campaign/ajax/m3",
        data: {
          'data': p2
        },
        success: function (data) {
          $("#id_m3").html(data);
          $("#id_m4").children().remove()
          $("#id_m5").children().remove()
          $("#id_m6").children().remove()
        }
      });
    });
    $("#id_m3").change(function () {
      var m3 = $(this).val();
      $.ajax({
        url: "/campaign/ajax/m4",
        data: {
          'data': m3
        },
        success: function (data) {
          $("#id_m4").html(data);
          $("#id_m5").children().remove()
          $("#id_m6").children().remove()
        }
      });
    });
    $("#id_m4").change(function () {
      var m4 = $(this).val();
      $.ajax({
        url: "/campaign/ajax/m5",
        data: {
          'data': m4
        },
        success: function (data) {
          $("#id_m5").html(data);
          $("#id_m6").children().remove()
        }
      });
    });
    $("#id_m5").change(function () {
      var m5 = $(this).val();
      $.ajax({
        url: "/campaign/ajax/m6",
        data: {
          'data': m5
        },
        success: function (data) {
          $("#id_m6").html(data);
        }
      });
    });
  $("#id_generic_company").change(function () {
    var generic_company = $(this).val();
    $.ajax({
      url: "/campaign/ajax/region",
      data: {
        'data': generic_company
      },
      success: function (data) {
        $("#id_region").html(data);
      }
    });
  });
  $("#id_region").change(function () {
    var region = $(this).val();
    $.ajax({
      url: "/campaign/ajax/country",
      data: {
        'data': region
      },
      success: function (data) {
        $("#id_country").html(data);
      }
    });
  });
  $("#id_country").change(function () {
    var country = $(this).val();
    $.ajax({
      url: "/campaign/ajax/location",
      data: {
        'data': country
      },
      success: function (data) {
        $("#id_location").html(data);
      }
    });
  });