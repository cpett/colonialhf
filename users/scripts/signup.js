$(function () {
  
  $('#signup').ajaxForm(function() { 
    }); 

  $('#id_username').on('change', function() {
    var username = $('#id_username').val();
    console.log(username);

    $.ajax({
      url: '/users/signup.check_username/',
      
      data: {
        u: username,
      },//data
      
      type: "POST",
      
      success: function(resp) {
        if (resp == 1) {
          $('#id_username').after('<span id="id_username_message">This username is available.</span>')
        }else{
          $('#id_username').after('<span id="id_username_message">This username is unavailable.</span>')
        }//if

      },//success

    });//ajax

  });//change

});//ready