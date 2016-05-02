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
		<link rel=”shortcut icon” href=”../img/favicon.ico” type=”image/x-icon” />
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
						<div class="row" style="background-color:#CDC8C4; padding-bottom:24px;">
							<center>
								<div id="sudoku-grid" style="padding-top:24px;">
									% include('sudoku_board.tpl', board=board)
								</div>
								<span><h2 style="text-align:center" id='userMessage' style="color:black;"></h2></span>
								<span><h1 style="text-align:center" id='winMessage' style="color:black;"></h1></span>
	
								<form style="text-align:center" role="form" method="post" onsubmit="return false;">
									<a href="./end" class="confirmation"><button class="btn btn-info btn-fill" type="button">New Game</button></a>
									<button class="btn btn-info btn-fill" type="submit" onclick="checkStatus()">Check Answers</button>
								</form>
							</center>
				      		</div> <!-- Board Row -->
					</div>


					<div class="col-lg-4 col-md-3 col-sm-3 col-xs-12 text-center" style="background-color:black;">
						<div class="row stats-div" style="">
							<center>
								<h1><span style="color:white;">What Is This?</span></h1>
							</center>
							<p style="text-align:left; color:white; text-indent:16px; padding-left:8px">
								Welcome to Sock Monkey Sudoku!<br>
								We designed this web app to challenge minds across the world;
								not just to solve puzzles, but to learn a bit about
								a growing problem in our world, as well: Alzheimer's.<br>
								There are few who have not heard of this all-to-common form of
								dementia, but how much do you really know about it?<br>
								Who is it likely to target? How often and how early can it be caught?
								Are there any cures or methods of prevention?<br>
								With each puzzle you solve, you may find answers to these questions and
								more!<br>
								We strongly encourage you to visit the Alzheimer's Association's site,
								and make a donation to aid in the battle against Alzheimer's; every
								dollar, fact and game counts!
							</p>
						</div>
						<div class="row" style="background-color:black;">
							<center>
								<h1><span style="color:white">Why Sudoku?</span></h1>
							</center>
							<p style="text-align:left; color:white; text-indent:16px; padding-left:8px">
								Sudoku is a timeless mathematical puzzle, and a constant exciting
								challenge for any mind.<br>
								Alzheimer's has no cure, but its daunting symptoms can be slowed
								by active learning and regular brain exercise, such as playing Sudoku.
								It is our hope that each and every game will help to fight off the symptoms
								for an Alzheimer's victim, if even just to educate you, the player, as
								to the on-going struggle around you.
							</p>
						</div>
					</div>
				</div>
			</div>
    </div> <!-- Content -->
  </div> <!-- Wrapper -->

	<div id="winModal" class="modal fade" role="dialog">
	<div class="modal-dialog">
	<!-- Modal content-->
	<div class="modal-content">
		<div class="modal-header">
			<button type="button" class="close" data-dismiss="modal">&times;</button>
			<center>
				<h1 class="modal-title">You Win!</h1>
			</center>
		</div>
		<div class="modal-body">
			<form action='./end' method="GET" role="form">
				<div class="form-group">
				<div class="row" style="margin-bottom:20px;">
					<div class="col-md-12">
						<span style="text-indent:16px">
							{{fact}}
						</span>
					</div>
				</div>
			</div>
	  </div>
			<div class="modal-footer">
				<button type="submit" class="btn btn-info btn-fill pull-left">Play Again?</button>
			</form>
				<button type="button" class="btn btn-default" data-dismiss="modal">Gaze on my victory...</button>
			</div>
		</div>
	</div>

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
			$('#winModal').modal('show');
		};

	</script>

	<script type="text/javascript">
		$('.confirmation').on('click', function () {
			return confirm('Are you sure you want to start a new game?');
		});
	</script>

</html>
