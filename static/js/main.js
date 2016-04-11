function updateCellValue(cell_id, value) {
	console.log("updateCellValue() Called!")
	
	$('#'+cell_id).css('background-color', 'white');
	
	if (value == "") {
		/* $('#'+cell_id).css('background-color', 'white'); */
	} else {
		$.ajax({
			type: "POST",
			url: "/update",
			data : { 'id': cell_id, 'value': value },
			success: function(results) {
				console.log(results);
				/*
				if (results['correct'] === true) {
					console.log("Correct Number!");
					$('#'+cell_id).css('background-color', 'green');
				}
				else if (results['correct'] === false) {
					console.log("Incorrect Number!");
					$('#'+cell_id).css('background-color', 'red');
				}
				*/
			},
			error: function(error) {
				console.log(error)
			}
		});
	};
};

function checkStatus() {
	console.log("checkStatus() Called!")

	$.ajax({
		type: "GET",
		url: "/status",
		data : {},
		success: function(results) {
			console.log(results);
			status_map = results['status_map']
			for (cell in status_map) {
				current_cell = status_map[cell]
				cell_id = current_cell[0]
				isMutable = current_cell[1]
				isCorrect = current_cell[2]
				
				if (isMutable === true) {
					if (isCorrect === true) {
						$('#'+cell_id).css('background-color', 'green');
					}
					else if (isCorrect === false) {
						$('#'+cell_id).css('background-color', 'red');
					}
				}
				
				if (results['status'] === 'Correct') {
					win()
				}
			};
		},
		error: function(error) {
			console.log(error)
		}
	});
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