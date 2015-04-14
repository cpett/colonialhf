$(function () {

  $('#loginform').ajaxForm(function(data) { 
      $('#login_dialog').find('.modal-body').html(data);
    }); 

});//ready