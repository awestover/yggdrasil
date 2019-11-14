
let board = "NeKeNPPPPPeeeeepppppneken";
let n = parseInt(Math.sqrt(board.length));
let piece_size = 100;

let imgs = {
	"K": new Image(),
	"k": new Image(),
	"P": new Image(),
	"p": new Image(),
	"N": new Image(),
	"n": new Image(),
	"e": new Image()
}
imgs["K"].src = 'static/blackking.jpg';
imgs["k"].src = 'static/whiteking.png';
imgs["P"].src = 'static/blackpawn.jpg';
imgs["p"].src = 'static/whitepawn.png';
imgs["N"].src = 'static/blackhorse.jpg';
imgs["n"].src = 'static/whitehorse.jpeg';
imgs["e"].src = 'static/empty.bmp';


function sendMove(){
	updateMoveLog("player", $("#move").val());
	$.post('/sendMove', {"board": board, "move": $("#move").val()}, 
		function(data){
			let rdata = JSON.parse(data);
			board = rdata["board"];
			updateBoard([rdata["move_ij"]]);
			updateMoveLog("computer", rdata["move"]);
			console.log(rdata["move_ij"]);
		}
	);
}

function updateBoard(highlight_squares){
	let c = document.getElementById("myCanvas");
	let ctx = c.getContext("2d");

	for (let i = 0; i < n; i++){
		for (let j = 0; j < n; j++){
			let idx = n*i+j;
			ctx.drawImage(imgs[board[idx]], j*piece_size, i*piece_size, piece_size, piece_size);
		}
	}

	for (let i in highlight_squares){
		ctx.beginPath();
		ctx.lineWidth = "6";
		ctx.strokeStyle = "red";
		ctx.rect(highlight_squares[i][1]*piece_size, highlight_squares[i][0]*piece_size, piece_size, piece_size);
		ctx.stroke();
	}
}

function updateMoveLog(player, move){
	let moveLog = $("#move-log");
	moveLog.prepend("<li>"+ player + ": " + move+"</li>");
}

setTimeout(function(){updateBoard([])}, 1000);

