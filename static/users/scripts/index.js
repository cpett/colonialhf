$(function () {

  $('#login_dialog').modal({
    show: false,
  });//modal

  $('#show_login_dialog').on('click', function() {
    $('#login_dialog').modal('show');
    $.ajax({
      url: '/users/index.loginform',
      success: function(data) {
        $('#login_dialog').find('.modal-body').html(data);
      },//success
    });//ajax
  });
});//ready