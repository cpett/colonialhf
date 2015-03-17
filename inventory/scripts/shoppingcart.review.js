$(function () {

  $('#login_dialog').modal({
    show: false,
  });//modal

  $('#cart_login_dialog').on('click', function() {
    $('#login_dialog').modal('show');
    $.ajax({
      url: '/inventory/shoppingcart.loginform',
      success: function(data) {
        $('#login_dialog').find('.modal-body').html(data);
      },//success
    });//ajax
  });//click

  $('.remove').on('click', function() {
    var id = $(this).attr('data-id')

    console.log(id)

    $.ajax({
      url: '/inventory/shoppingcart.remove/' + id,
      type: 'POST',
      success: function(data) {
        $('.target').html(data)
      }
    })
  })

});//ready