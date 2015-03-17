$(function () {

  $('#show_shoppingcart_dialog').on('click', function() {

    console.log("Im here")
    var pid = $(this).attr('data-pid')
    var qty = $('#item_qty').val()

    console.log(pid)
    console.log(qty)

    $.loadmodal({     
      url: '/inventory/shoppingcart.add/' + pid + '/' + qty,
      title: '<h2>Shopping Cart</h2>'
    })
  });//load modal--Albrecht
});//ready