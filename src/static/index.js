
// let board = "NeKeNPPPPPeeeeepppppneken";
let board = "NeeeKeeNPPPPPPPPeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeppppppppneekeeen"
let n = parseInt(Math.sqrt(board.length));
let piece_size = 62.5;

let img_side = 132
// "piece": [i, j] in grid
let imgs = { 
	"N": [1, 1],
	"n": [0, 1],
	"K": [1, 4],
	"k": [0, 4],
	"P": [1, 5],
	"p": [0, 5]
};

let pieces_sprite_sheet = new Image();
pieces_sprite_sheet.src = "static/chessPieces.png";

function sendMove(){
	$.post("/doPlayerMove", {"board": board, "move": $("#move").val()}, 
		function(data){
			let rdata = JSON.parse(data);
			board = rdata["board"];
			updateBoard([rdata["move_ij"]]);
			updateMoveLog("player", $("#move").val());
			$.post("/doComputerMove", {"board": board}, function(c_data){
				let c_rdata = JSON.parse(c_data);
				board = c_rdata["board"];
				updateBoard([c_rdata["move_ij"]]);
				updateMoveLog("computer", c_rdata["move"]);
			});
		}
	);
}

function updateBoard(highlight_squares){
	let c = document.getElementById("myCanvas");
	let ctx = c.getContext("2d");
	ctx.clearRect(0, 0, c.width, c.height);

	for (let i = 0; i < n; i++){
		for (let j = 0; j < n; j++){
			let idx = n*i+j;
			if(board[idx] != "e"){

				let si = imgs[board[idx]][0];
				let sj = imgs[board[idx]][1];
				ctx.drawImage(pieces_sprite_sheet, sj*img_side, si*img_side, img_side, img_side, j*piece_size, i*piece_size, piece_size, piece_size);
			}
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

