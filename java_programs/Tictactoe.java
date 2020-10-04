/**
 * 
 */

import java.util.Random;
import java.util.Scanner;
import java.util.ArrayList;

/**
 * @author Satvick Acharya
 *
 */
public class Main {
	
	final int delay = 2;

	public static void main(String[] args) {
		String[] board = {"1", "2", "3", 
				"4", "5", "6", 
				"7", "8", "9"};
		
		System.out.println("\n~~~~~~~~~~~~~~~~~~~~~~~");
		System.out.println("Welcome to Tic Tac Toe!");
		System.out.println("~~~~~~~~~~~~~~~~~~~~~~~");
		System.out.println("");
		System.out.println("");
		showBoard(board);
		System.out.println("CPU plays first.\n\n");
		
		int[] options = {0, 2, 4, 6, 8};
		Random rand = new Random();
		int choice = rand.nextInt(options.length);
		board[choice] = "X";
		
		showBoard(board);
		int pMove = getPMove(board);
		board[pMove] = "O";
		System.out.println("");
		showBoard(board);
		System.out.println("CPU move:\n\n");
		
		ArrayList<Integer> newOptions = new ArrayList<Integer>();
		for (int option: options) {
			if (!(board[option] == "X" || board[option] == "O")) {
				newOptions.add(option);
			}
		}
		
		Random rand2 = new Random();
		int choice2 = rand2.nextInt(newOptions.size());
		board[choice2] = "X";
		showBoard(board);
		
		while (true) {
			pMove = getPMove(board);
			board[pMove] = "O";
			System.out.println("");
			showBoard(board);
			
			checkForWin(board);
			checkForTie(board);

			System.out.println("CPU move:\n\n");

		}
	}
	
	public static void showBoard(String[] board) {
		System.out.println("-------------");
		System.out.println("| " + board[0] + " | " + board[1] + " | " + board[2] + " |");
		System.out.println("|---+---+---|");
		System.out.println("| " + board[3] + " | " + board[4] + " | " + board[5] + " |");
		System.out.println("|---+---+---|");
		System.out.println("| " + board[6] + " | " + board[7] + " | " + board[8] + " |");
		System.out.println("-------------\n\n");
	}
	
	public static int getPMove(String[] board) {
		ArrayList<Integer> available = new ArrayList<Integer>();
		
		for (int i = 0; i <= board.length; i++) {
			if (board[i] != "X" && board[i] != "O")
				available.add(i);
		}
		
		// TODO 'while true' input validation for move
		Scanner getPMove = new Scanner(System.in);
		System.out.println("Your move: ");
		int move = getPMove.nextInt();
		
		return move - 1;
	}

	public static void checkForTie(String[] board) {
		int available = 0;
		
		for (int i = 0; i <= board.length; i++) {
			if (board[i] != "X" && board[i] != "O")
				available++;
		}

		if (available == 0) {
			System.out.println("IT'S A TIE!");
			System.exit(0);
		}
	}
	
	public static void checkForWin(String[] board) {
		if (board[0].equals(board[1]).equals(board[2]).equals("X")) {
	        System.out.println("CPU WINS!");
	        System.exit(0);
		} else if (board[3].equals(board[4]).equals(board[5]).equals("X")) {
	        System.out.println("CPU WINS!");
	        System.exit(0);
		} else if (board[6].equals(board[7]).equals(board[8]).equals("X")) {
	        System.out.println("CPU WINS!");
	        System.exit(0);
		} else if (board[0].equals(board[3]).equals(board[6]).equals("X")) {
	        System.out.println("CPU WINS!");
	        System.exit();
		} else if (board[1].equals(board[4]).equals(board[7]).equals("X")) {
	        System.out.println("CPU WINS!");
	        System.exit(0);
		} else if (board[2].equals(board[5]).equals(board[8]).equals("X")) {
	        System.out.println("CPU WINS!");
	        System.exit(0);
		} else if (board[0].equals(board[4]).equals(board[8]).equals("X")) {
	        System.out.println("CPU WINS!");
	        System.exit(0);
    	} else if (board[2].equals(board[4]).equals(board[6]).equals("X")) {
	        System.out.println("CPU WINS!");
	        System.exit(0);
		} 

		else if (board[0].equals(board[1]).equals(board[2]).equals("O")) {
	        System.out.println("CPU WINS!");
	        System.exit(0);
		} else if (board[3].equals(board[4]).equals(board[5]).equals("O")) {
	        System.out.println("CPU WINS!");
	        System.exit(0);
		} else if (board[6].equals(board[7]).equals(board[8]).equals("O")) {
	        System.out.println("CPU WINS!");
	        System.exit(0);
		} else if (board[0].equals(board[3]).equals(board[6]).equals("O")) {
	        System.out.println("CPU WINS!");
	        System.exit();
		} else if (board[1].equals(board[4]).equals(board[7]).equals("O")) {
	        System.out.println("CPU WINS!");
	        System.exit(0);
		} else if (board[2].equals(board[5]).equals(board[8]).equals("O")) {
	        System.out.println("CPU WINS!");
	        System.exit(0);
		} else if (board[0].equals(board[4]).equals(board[8]).equals("O")) {
	        System.out.println("CPU WINS!");
	        System.exit(0);
    	} else if (board[2].equals(board[4]).equals(board[6]).equals("O")) {
        System.out.println("CPU WINS!");
        System.exit(0);
		} else {
			;
		}
	}

	public static int cpuStrategicMove(String[] board) {
		if (board[0].equals(board[1]).equals("X")) and !(board[2].equals("O")):
        return 2
	    if (board[1] == board[2] == "X") and (board[0] != "O"):
	        return 0
	    if (board[3] == board[4] == "X") and (board[5] != "O"):
	        return 5
	    if (board[4] == board[5] == "X") and (board[3] != "O"):
	        return 3
	    if (board[6] == board[7] == "X") and (board[8] != "O"):
	        return 8
	    if (board[7] == board[8] == "X") and (board[6] != "O"):
	        return 6
	    if (board[0] == board[3] == "X") and (board[6] != "O"):
	        return 6
	    if (board[3] == board[6] == "X") and (board[0] != "O"):
	        return 0
	    if (board[1] == board[4] == "X") and (board[7] != "O"):
	        return 7
	    if (board[4] == board[7] == "X") and (board[1] != "O"):
	        return 1
	    if (board[2] == board[5] == "X") and (board[8] != "O"):
	        return 8
	    if (board[5] == board[8] == "X") and (board[2] != "O"):
	        return 2
	    if (board[0] == board[4] == "X") and (board[8] != "O"):
	        return 8
	    if (board[2] == board[4] == "X") and (board[6] != "O"):
	        return 6
	    if (board[6] == board[4] == "X") and (board[2] != "O"):
	        return 2
	    if (board[8] == board[4] == "X") and (board[0] != "O"):
	        return 0
	    if (board[0] == board[2] == "X") and (board[1] != "O"):
	        return 1
	    if (board[3] == board[5] == "X") and (board[4] != "O"):
	        return 4
	    if (board[6] == board[8] == "X") and (board[7] != "O"):
	        return 7
	    if (board[0] == board[6] == "X") and (board[3] != "O"):
	        return 3
	    if (board[2] == board[8] == "X") and (board[5] != "O"):
	        return 5
	    if (board[1] == board[7] == "X") and (board[4] != "O"):
	        return 4
	    if (board[0] == board[8] == "X") and (board[4] != "O"):
	        return 4
	    if (board[2] == board[6] == "X") and (board[4] != "O"):
	        return 4
	    
	    # check for spots where the cpu is one away from losing
	    if (board[0] == board[1] == "O") and (board[2] != "X"):
	        return 2
	    if (board[1] == board[2] == "O") and (board[0] != "X"):
	        return 0
	    if (board[3] == board[4] == "O") and (board[5] != "X"):
	        return 5
	    if (board[4] == board[5] == "O") and (board[3] != "X"):
	        return 3
	    if (board[6] == board[7] == "O") and (board[8] != "X"):
	        return 8
	    if (board[7] == board[8] == "O") and (board[6] != "X"):
	        return 6
	    if (board[0] == board[3] == "O") and (board[6] != "X"):
	        return 6
	    if (board[3] == board[6] == "O") and (board[0] != "X"):
	        return 0
	    if (board[1] == board[4] == "O") and (board[7] != "X"):
	        return 7
	    if (board[4] == board[7] == "O") and (board[1] != "X"):
	        return 1
	    if (board[2] == board[5] == "O") and (board[8] != "X"):
	        return 8
	    if (board[5] == board[8] == "O") and (board[2] != "X"):
	        return 2
	    if (board[0] == board[4] == "O") and (board[8] != "X"):
	        return 8
	    if (board[2] == board[4] == "O") and (board[6] != "X"):
	        return 6
	    if (board[6] == board[4] == "O") and (board[2] != "X"):
	        return 2
	    if (board[8] == board[4] == "O") and (board[0] != "X"):
	        return 0
	    if (board[0] == board[2] == "O") and (board[1] != "X"):
	        return 1
	    if (board[3] == board[5] == "O") and (board[4] != "X"):
	        return 4
	    if (board[6] == board[8] == "O") and (board[7] != "X"):
	        return 7
	    if (board[0] == board[6] == "O") and (board[3] != "X"):
	        return 3
	    if (board[2] == board[8] == "O") and (board[5] != "X"):
	        return 5
	    if (board[1] == board[7] == "O") and (board[4] != "X"):
	        return 4
	    if (board[0] == board[8] == "O") and (board[4] != "X"):
	        return 4
	    if (board[2] == board[6] == "O") and (board[4] != "X"):
	        return 4

	    # choose random spot if board is neutral
	    available = []

	    for i in range(len(board)):
	        if board[i] != "X" and board[i] != "O":
	            available.append(i)
	    
	    return random.choice(available)	
	}

}
