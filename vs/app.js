var gridSize = 5;
var players = [
    { id: 1, x: 0, y: 0, direction: 'right', points: 0, moves: 30 },
    { id: 2, x: gridSize - 1, y: gridSize - 1, direction: 'left', points: 0, moves: 30 }
];
var blocks = [];
var yellowBlock = null;
var winer = null;

function createGrid() {
    var grid = document.getElementById('grid');
    grid.innerHTML = '';

    grid.style.gridTemplateColumns = `repeat(${gridSize}, 1fr)`;

    for (var y = 0; y < gridSize; y++) {
        for (var x = 0; x < gridSize; x++) {
            var cell = document.createElement('div');
            cell.className = 'cell';
            var player = getPlayerAtPosition(x, y);
            if (player) {
                cell.className += ' player' + player.id;
            } else if (hasBlockAtPosition(x, y)) {
                cell.className += ' block';
            } else if (yellowBlock && yellowBlock.x === x && yellowBlock.y === y) {
                cell.className += ' yellow-block';
            }
            grid.appendChild(cell);
        }
    }
}

function getPlayerAtPosition(x, y) {
    return players.find(function (player) {
        return player.x === x && player.y === y;
    });
}

function hasBlockAtPosition(x, y) {
    return blocks.find(function (block) {
        return block.x === x && block.y === y;
    });
}

function movePlayer(player, direction) {
    var newX = player.x;
    var newY = player.y;

    switch (direction) {
        case 'left':
            newX = Math.max(0, player.x - 1);
            break;
        case 'right':
            newX = Math.min(gridSize - 1, player.x + 1);
            break;
        case 'up':
            newY = Math.max(0, player.y - 1);
            break;
        case 'down':
            newY = Math.min(gridSize - 1, player.y + 1);
            break;
    }

    if (newX !== player.x || newY !== player.y) {
        if (!hasBlockAtPosition(newX, newY) || player.points > 0) {
            player.x = newX;
            player.y = newY;
            player.direction = direction;

            if (hasBlockAtPosition(newX, newY)) {
                if (player.points > 0) {
                    player.points--;
                    removeBlockAtPosition(newX, newY);
                } else {
                    player.x = player.direction === 'left' || player.direction === 'right' ? player.x : player.direction === 'up' ? player.x + 1 : player.x - 1;
                    player.y = player.direction === 'up' || player.direction === 'down' ? player.y : player.direction === 'left' ? player.y + 1 : player.y - 1;
                }
            }
        }
        checkYellowBlock(player);
        updatePlayer();
        createGrid();
    }
}

function placeBlock(player) {
    var blockX = player.x;
    var blockY = player.y;

    switch (player.direction) {
        case 'left':
            blockX = Math.max(0, player.x - 1);
            break;
        case 'right':
            blockX = Math.min(gridSize - 1, player.x + 1);
            break;
        case 'up':
            blockY = Math.max(0, player.y - 1);
            break;
        case 'down':
            blockY = Math.min(gridSize - 1, player.y + 1);
            break;
    }

    if (!hasBlockAtPosition(blockX, blockY)) {
        blocks.push({ x: blockX, y: blockY });
        createGrid();
    }
}

function removeBlockAtPosition(x, y) {
    var index = blocks.findIndex(function (block) {
        return block.x === x && block.y === y;
    });

    if (index !== -1) {
        blocks.splice(index, 1);
    }
}

function checkYellowBlock(player) {
    if (yellowBlock && yellowBlock.x === player.x && yellowBlock.y === player.y) {
        player.points++;
        yellowBlock = null;
    }
}

function generateYellowBlock() {
    if (yellowBlock) return;

    var emptyPositions = [];
    for (var x = 0; x < gridSize; x++) {
        for (var y = 0; y < gridSize; y++) {
            if (!getPlayerAtPosition(x, y) && !hasBlockAtPosition(x, y)) {
                emptyPositions.push({ x: x, y: y });
            }
        }
    }

    if (emptyPositions.length > 0) {
        var randomPosition = emptyPositions[Math.floor(Math.random() * emptyPositions.length)];
        yellowBlock = { x: randomPosition.x, y: randomPosition.y };
    }
}

function updatePlayer() {
    var p1 = players[0];
    var p2 = players[1];
    document.getElementById('points-1').innerHTML = `Puntos: ${p1.points} <br> Movimientos: ${p1.moves}`;
    document.getElementById('points-2').innerHTML = `Puntos: ${p2.points} <br> Movimientos: ${p2.moves}`;
}

function TerminarPartida() {
    var p1 = players[0];
    var p2 = players[1];
    if (p1.points > p2.points) {
        winer = 'Rojo';
    } else {
        winer = 'Azul';
    }

    if (winer != null) {
        alert(`Gano el ${winer}`);
    }
}

document.addEventListener('keydown', function (event) {
    if (players[0].moves <= 0 || players[1].moves <= 0) {
        TerminarPartida();
        return;
    }
    switch (event.key) {
        case 'ArrowLeft':
            players[1].moves -= 1;
            movePlayer(players[1], 'left');
            break;
        case 'ArrowRight':
            players[1].moves -= 1;
            movePlayer(players[1], 'right');
            break;
        case 'ArrowUp':
            players[1].moves -= 1;
            movePlayer(players[1], 'up');
            break;
        case 'ArrowDown':
            players[1].moves -= 1;
            movePlayer(players[1], 'down');
            break;
        case '.':
            placeBlock(players[1]);
            break;
        case 'a':
            players[0].moves -= 1;
            movePlayer(players[0], 'left');
            break;
        case 'd':
            players[0].moves -= 1;
            movePlayer(players[0], 'right');
            break;
        case 'w':
            players[0].moves -= 1;
            movePlayer(players[0], 'up');
            break;
        case 's':
            players[0].moves -= 1;
            movePlayer(players[0], 'down');
            break;
        case 'e':
            placeBlock(players[0]);
            break;
    }
    updatePlayer();
});

setInterval(generateYellowBlock, 500);
createGrid();
updatePlayer();
