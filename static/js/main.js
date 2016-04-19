function updateCellValue(cell_id, value) {
	console.log("updateCellValue() Called!")
		
	if (value != "") {
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


$(document).ready(function() {
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

	$("input.cell").keyup(function(e){
		var cell = $(this);

		if(!cell.attr("immutable")){
			var answer = e.keyCode - 48;
			if(0 < answer && answer < 10){
				cell.val(answer);
				updateCellValue(cell.attr("id"), answer);
			}
		}
	});
});
