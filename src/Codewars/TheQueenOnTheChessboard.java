package Codewars;
import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;
import java.util.Collections;

public class TheQueenOnTheChessboard {
    public static List<String> availableMoves(String position) {
        if( !(position instanceof String) || !isValidPosition(position)) {
            return new ArrayList<String>();
        }
        Set<String> star = createStar(position);
        star.removeIf(move -> !isValidPosition(move) || move.equals(position));
        ArrayList<String> possibleMoves = new ArrayList<String>(star);
        Collections.sort(possibleMoves);
        return possibleMoves;
    }

    public static Set<String> createStar(String position) {
        Set<String> moves = new HashSet<>();
        moves.addAll(createRay(position,-1,1));
        moves.addAll(createRay(position,0,1));
        moves.addAll(createRay(position,1,1));
        moves.addAll(createRay(position,1,0));
        return moves;
    }

    public static Set<String> createRay(String position, int idiretion, int jdirection) {
        Set<String> moves = new HashSet<>();
        int ifile = Integer.valueOf(position.charAt(0));
        int irank = Character.getNumericValue(position.charAt(1));
        for (int i = ifile-7*idiretion, j = irank-7*jdirection; (i<=ifile+7 && j<=irank+7) ; i+=idiretion,j+=jdirection){
            moves.add((char)i + "" + j);
        }
        return moves;
    }

    public static boolean isValidPosition(String position) {
        if (position.length()!=2 || !isValidFile(position) || !isValidRank(position)){
            return false;
        }
        return true;
    }
    public static boolean isValidFile(String position) {
        String possibleFiles = "ABCDEFGH";
        if (possibleFiles.indexOf(position.charAt(0)) == -1){
            return false;
        }
        return true;
    }
    public static boolean isValidRank(String position) {
        String possibleRanks = "12345678";
        if (possibleRanks.indexOf(position.charAt(1)) == -1){
            return false;
        }
        return true;
    }

}
