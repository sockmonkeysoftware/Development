function updateCellValue(cell_id, value) {
	console.log("updateCellValue() Called!")
	if (value == "") {
		$('#'+cell_id).css('background-color', 'white');
	} else {
		$.ajax({
			type: "POST",
			url: "/update",
			data : { 'id': cell_id, 'value': value },
			success: function(results) {
				console.log(results);
				
				if (results['correct'] === true) {
					console.log("Correct Number!");
					$('#'+cell_id).css('background-color', 'green');
				}
				else if (results['correct'] === false) {
					console.log("Incorrect Number!");
					$('#'+cell_id).css('background-color', 'red');
				}
				
				//if (results.length > 0) {
				//} else {
				//	$('#results').html('Something went terribly wrong! Please try again.')
				//}
			},
			error: function(error) {
				console.log(error)
			}
		});
	};
};


//$(document).ready(function() {
	//console.log("ready!");

	//$('#try-again').hide();

	// on form submission ...
	// $('form').on('submit', function() {
	//$('.cell').on('function', function updateCellValue() {
		//var cell_id = $(this).attr("id");
		//var value = $(this).val();
		
		//console.log("the form has beeen submitted");

		// grab values
		//valueOne = $('input[name="location"]').val();
		//valueTwo = $('input[name="language"]').val();
		//console.log(valueOne, valueTwo)
	//$('#try-again').on('click', function(){
	//	$('input').val('').show();
	//	$('#try-again').hide();
	//	$('#results').html('');
	//});

//});