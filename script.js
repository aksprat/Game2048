// Assuming `board` is a 2D array representing the game board
function renderBoard(board) {
    var boardContainer = document.getElementById('board-container');
    boardContainer.innerHTML = ''; // Clear the board container

    for (var i = 0; i < board.length; i++) {
        for (var j = 0; j < board[i].length; j++) {
            var tileValue = board[i][j];
            var tileClass = 'tile tile-' + tileValue;
            var tile = document.createElement('div');
            tile.className = tileClass;
            tile.textContent = tileValue !== 0 ? tileValue : '';
            boardContainer.appendChild(tile);
        }
    }
}
