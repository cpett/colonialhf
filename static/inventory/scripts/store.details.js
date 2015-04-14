$(function () {

  $('#show_shoppingcart_dialog').on('click', function() {

    var pid = $(this).attr('data-id')
    var qty = $('#item_qty').val()
    var type = $(this).attr('data-type')

    $.loadmodal({     
      url: '/inventory/shoppingcart.add/' + pid + '/' + qty + '/' + type,
      title: '<h2>Shopping Cart</h2>'
    })
  });//load modal--Albrecht
});//ready