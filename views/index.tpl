<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0' name='viewport' />
		<meta name="viewport" content="width=device-width" />
		<!-- Bootstrap core CSS  -->
		<link href="../css/bootstrap.min.css" rel="stylesheet" />
		<!--  Light Bootstrap Table core CSS -->
		<link href="../css/light-bootstrap-dashboard.css" rel="stylesheet"/>
		<!-- Custom CSS  -->
		<link href="../css/style.css" rel="stylesheet" />
		<!--  Fonts and icons  -->
		<link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
		<link href='http://fonts.googleapis.com/css?family=Roboto:400,700,300' rel='stylesheet' type='text/css'>
		<link href="../css/pe-icon-7-stroke.css" rel="stylesheet" />
		<title>Sock Monkey Sudoku</title>
	</head>
	<body>
		<center>
		<h1>SOCK MONKEY SUDOKU</h1><hr /><br />

		<div class="table-responsive" id="sudoku-grid">
			<table>
		<!--  Header -->
		%for y in range(9):
			<tr>
			%for x in range(9):
				%id = chr(ord('a')+y) + str(x+1)
					%if x % 3 == 0 and y % 3 == 0 :
						<td class="vert-hor-3 content">
					%elif x % 3 == 0 and y % 3 != 0 :
						<td class="vert-3 content">
					%elif x % 3 != 0 and y % 3 == 0 :
						<td class="hor-3 content">
					%elif x % 8 == 0 and y % 8 == 0 :
						<td class="vert-hor-8 content">
					%elif x % 8 == 0 and y % 8 != 0 :
						<td class="vert-8 content">
					%elif x % 8 != 0 and y % 8 == 0 :
						<td class="hor-8 content">
					%else:
						<td class="content">
					%end

					<input class="cell" readonly
					
					%if (id in board):
						value={{board[id][0]}}
						
						%if (board[id][1] == False):
							style="background-color:black"
							immutable="immutable"
						%end
		
					%else:
						value=""
					%end

					name={{id}}
					id={{id}}
					maxlength="1" size="1"
					onkeypress="return validateInput(event)"
					/>
					</div></td>
			%end
			<tr>
		%end
		</table>
		</div>

		<span><h2 id='userMessage' style="color:black;"></h2></span>
		<span><h1 id='winMessage' style="color:black;"></h1></span>


		<form role="form" method="post" onsubmit="return false;">
			<a href="./end" class="confirmation"><button class="btn btn-info btn-fill" type="button">New Game</button></a>
			<button class="btn btn-info btn-fill" type="submit" onclick="checkStatus()">Check Answers</button>
		</form>

		</center>
		<!--   Core JS Files   -->
		<script src="../js/jquery-1.10.2.js" type="text/javascript"></script>
		<script src="../js/bootstrap.min.js" type="text/javascript"></script>
		<script src="../js/light-bootstrap-dashboard.js"></script>
	</body>

	<script type="text/javascript" src="../js/main.js"></script>

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

		function win() {
			document.getElementById('winMessage').innerHTML = "You win!"
		};
		
	</script>

	<script type="text/javascript">
		$('.confirmation').on('click', function () {
			return confirm('Are you sure you want to start a new game?');
		});
	</script>

</html>
