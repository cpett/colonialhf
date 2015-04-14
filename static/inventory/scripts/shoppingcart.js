$(function() {

	$('.remove').on('click', function() {
		var id = $(this).attr('data-id')
		var ptype = $(this).attr('data-type')

		$.ajax({
			url: '/inventory/shoppingcart.remove/' + id + '/' + ptype,
			type: 'POST',
			success: function(data) {
				$('.target').html(data)
			}
		})
	})

});