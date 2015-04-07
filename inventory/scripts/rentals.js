$(function() {
	$('#search_button').on('click', function() {
		var search = $('#search_input').val();

		console.log(search)

		$('tr td.product_name').each(function() {
			if ($(this).text().toUpperCase() == search.toUpperCase()) 
			{
				$(this).parent().show();
			}
			else if(search.length < 1)
			{
				$('tr').show();
			}
			else{
				$(this).parent().hide();
			}
		})
	})
})