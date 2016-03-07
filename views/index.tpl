<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<!--
		<link rel="stylesheet" type="text/css" media="screen"
		href="../css/skeleton.css" /> -->
		<link rel="stylesheet" type="text/css" media="screen"
		href="../css/style.css" />
		<title></title>
	</head>
	<body>
		<center>
		<h1 style="color:white; font-size: 60px;">SUDOKU</h1>
		<table id="sudoku-grid" cellspacing="0" cellpadding="0">
		<!--  Header -->
		%for y in range(9):
			<tr>
			%for x in range(9):
				%id = chr(ord('a')+y) + str(x+1)
					<td>
					<div id="boxdiv">
					<input class="cell"
					
					%if (board.has_key(id)):
						value={{board[id]}}
						readonly
						style="background-color:black"
					%else:
						value=""
					%end
					
					name={{id}}
					id={{id}} 
					maxlength="1" size="1"
					onchange="printChange(this.id, this.value)"
					onkeypress="return validateInput(event)"
					/>
					</div></td>
			%end
			<tr>
		%end
		</table>
		<span><h2 id='userMessage' style="color:white;"></h2></span>
		</center>
	</body>
	<script>
	function printChange(id, value) {
		console.log(id, value);
	};
	
	function validateInput(event) {
		if (event.charCode >= 49 && event.charCode <= 57) {
			document.getElementById('userMessage').innerHTML = ""
			return true;
		} else {
			document.getElementById('userMessage').innerHTML = "Whoops! Make sure you enter a valid digit 1-9!"
			return false;
		};
	};
	</script>

</html>