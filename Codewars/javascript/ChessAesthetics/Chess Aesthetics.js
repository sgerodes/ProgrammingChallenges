function get_without_every_piece(fen) {
    let fens = [];
    for (let i = 0; i < fen.indexOf(" "); ++i) {
        if (isNaN(fen[i])) {
            if ( fen[i] !== "/") {
                fens.push( subtituteOnePiece(fen, i) );
            }
        }
    }
    return fens;
}

function subtituteOnePiece(fen, index) {
    function isNumeric(str) {
        return str === ' '? false : !isNaN(str);
    }
    let isLeftNumber = isNumeric(fen[index - 1]);
    let isRightNumber = isNumeric(fen[index + 1]);
    let leftIndex = isLeftNumber ? index - 1 : index;
    let rightIndex = isRightNumber ? index + 1 : index;
    let left = isLeftNumber ? parseInt(fen[index - 1]) : 0;
    let right = isRightNumber ? parseInt(fen[index + 1]) : 0;
    let leftSub = fen.substring(0, leftIndex);
    let rightSub = fen.substring(rightIndex + 1);
    return leftSub + (left + right + 1) + rightSub;
}