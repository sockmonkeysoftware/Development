<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0' name='viewport' />
		<meta name="viewport" content="width=device-width" />
		<!-- Bootstrap core CSS  -->
		<link href="../css/bootstrap.min.css" rel="stylesheet" />
		<!-- Custom CSS  -->
		<link href="../css/style.css" rel="stylesheet" />
		<!--  Fonts and icons  -->
		<link href="../css/pe-icon-7-stroke.css" rel="stylesheet" />

		<link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
		<link href='http://fonts.googleapis.com/css?family=Roboto:400,700,300' rel='stylesheet' type='text/css'>

		<title>Sock Monkey Sudoku</title>

	</head>
<body>
	<div class="wrapper">
<div class="row" style="">
		<nav class="navbar navbar-default navbar-fixed" style="margin-bottom:0">
      <div class="container-fluid">
        <div class="navbar-header">
					<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#collapse">
							<span class="sr-only">Toggle navigation</span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
					</button>

          <a class="navbar-brand" href="#" style="padding-top:0px"><img src="/img/sock_monkey_logo.png" class="sm-img"></a>
        </div>
				<div class="collapse navbar-collapse" id="collapse">
          <ul class="nav navbar-nav navbar-right">
						<li>
              <a href="#about">
                About Us
              </a>
            </li>
						<li>
              <a target="_blank" href="https://www.alz.org/living_with_alzheimers_4521.asp">
                Learn More
              </a>
            </li>
            <li>
              <a target="_blank" href="https://www.alz.org/join_the_cause_donate.asp">
                Donate to the Cause
              </a>
            </li>
          </ul>
				</div>
      </div>
    </nav>
</div>
    <div class="content">
			<div class="container-fluid">
				<div class="row" style="display:flex">
					<div class="col-lg-8 col-md-9 col-sm-9 col-xs-12">
						<div class="row" style="background-color:#CDC8C4;">
							<div class="center" id="sudoku-grid" style="padding-top:24px;">
								% include('sudoku_board.tpl', board=board)
							</div>
							<span><h2 style="text-align:center" id='userMessage' style="color:black;"></h2></span>
							<span><h1 style="text-align:center" id='winMessage' style="color:black;"></h1></span>

							<form style="text-align:center" role="form" method="post" onsubmit="return false;">
								<a href="./end" class="confirmation"><button class="btn btn-info btn-fill" type="button">New Game</button></a>
								<button class="btn btn-info btn-fill" type="submit" onclick="checkStatus()">Check Answers</button>
							</form>
				      		</div> <!-- Board Row -->

						<div class="row" style="background-color:black;">
							<center>
								<h1><span style="color:white;">Stuff About Us</span></h1>
							</center>
						</div>
						<div class="row stats-div" style="">
							<center>
								<h1><span style="color:white">Fancy photo with statistics overlay?</span></h1>
							</center>
						</div>

						<div class="row" style="background-color:black;">
							<center>
								<h1><span style="color:white">More stuff about us maybe</span></h1>
							</center>
						</div>
					</div>


					<div class="col-lg-4 col-md-3 col-sm-3 col-xs-12 text-center" style="background-color:black;">
						<div class="row" style="">
							<center>
								<h1><span style="color:white">Facts Here</span></h1>
							</center>
						</div>
					</div>
				</div>
			</div>
    </div> <!-- Content -->
  </div> <!-- Wrapper -->


	<!--   Core JS Files   -->
	<script src="../js/jquery-1.10.2.js" type="text/javascript"></script>
	<script src="../js/bootstrap.min.js" type="text/javascript"></script>

	</body>

	<script type="text/javascript" src="../js/main.js"></script>

	<script>
		function printChange(id, value) {
			console.log(id, value);
		};

		function validateInput(event) {
			if ((event.charCode >= 49 && event.charCode <= 57) || event.charCode == 8 || event.charCode == 32 || event.charCode == 46) {
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
