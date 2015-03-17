$(function() {

	$('.remove').on('click', function() {
		var id = $(this).attr('data-id')

		console.log(id)

		$.ajax({
			url: '/inventory/shoppingcart.removeitem/' + id,
			type: 'POST',
			success: function(data) {
				$('.target').html(data)
			}
		})
	})

});