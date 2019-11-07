
let board = "NKeNPPPPppppnekn";

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
			updateBoard();
			updateMoveLog("computer", rdata["move"]);
		}
	);
}

function updateBoard(){
	let c = document.getElementById("myCanvas");
	let ctx = c.getContext("2d");

	let piece_size = 100;

	for (let i = 0; i < 4; i++){
		for (let j = 0; j < 4; j++){
			let idx = 4*i+j;
			ctx.drawImage(imgs[board[idx]], j*piece_size, i*piece_size, piece_size, piece_size);
		}
	}
}

function updateMoveLog(player, move){
	let moveLog = $("#move-log");
	moveLog.prepend("<li>"+ player + ": " + move+"</li>");
}

setTimeout(function(){updateBoard()}, 1000);

