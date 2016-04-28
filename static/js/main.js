function updateCellValue(cell_id, value) {
	console.log("updateCellValue() Called!")

	if(value == "")
		value = "clear";

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


$(document).ready(function() {
	// If a touch device is not being used, allow divs to be manipulated
	// by click-and-type rather than text box style input
	if(!('ontouchstart' in document.documentElement)){

		// Make the input read-only to override textbox functionality
		$("input.cell").each(function(){
			var cell = $(this);
			if(!cell.attr("immutable"))
				cell.attr("readonly", "readonly");
		});


		$("input.cell").keypress(function(e){
			if(e.keyCode == 8 || e.keyCode == 32 || e.keyCode == 46)
				e.preventDefault();
		});

		$("input.cell").keydown(function(e){
			if(e.keyCode == 8 || e.keyCode == 32 || e.keyCode == 46)
				e.preventDefault();
		});
		
		$("input.cell").keyup(function(e){
			e.preventDefault();
			var cell = $(this);

			if(!cell.attr("immutable")){
				var answer = e.keyCode;
				if(48 < answer && answer < 58){
					answer -= 48;
					cell.val(answer);
					updateCellValue(cell.attr("id"), answer);
				}
				else if(answer == 8 || answer == 32 || answer == 46){
					if(cell.val() != ""){
						cell.val("");
						updateCellValue(cell.attr("id"), "clear");
					}
				}
			}
		});

	}


	$("input.cell").focus(function(e){
		var cell = $(this);

		if(!cell.attr("immutable"))
			$(this).attr("style", "background-color:#A0A0FF");
	});

	$("input.cell").focusout(function(e){
		var cell = $(this);

		if(!cell.attr("immutable"))
			$(this).attr("style", "background-color:#FFFFFF");
	});

});
