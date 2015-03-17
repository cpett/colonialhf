$(function() {

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

});