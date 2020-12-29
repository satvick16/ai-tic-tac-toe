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
		String[] board = {"1", "2", "3", "4", "5", "6", "7", "8", "9"};
		
		System.out.println("\n~~~~~~~~~~~~~~~~~~~~~~~");
		System.out.println("Welcome to Tic Tac Toe!");
		System.out.println("~~~~~~~~~~~~~~~~~~~~~~~\n\n");
		showBoard(board);
		
		boolean cpu_is_first = whoGoesFirst();

		if (cpu_is_first) {
			System.out.println("CPU move:\n\n");
			int cpu_move = cpuStrategicMove(board);
			board[cpu_move] = "X";
			showBoard(board);
		}

		while (true) {
			p_move = getPMove(board);
			board[p_move] = "O";
			System.out.println();
			showBoard(board);

			checkIfGameOver(board);

			System.out.println("CPU move:\n\n");
			int cpu_move = cpuStrategicMove(board);
			board[cpu_move] = "X";
			System.out.println();
			showBoard(board);

			checkIfGameOver(board);			
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

	public static boolean whoGoesFirst() {
		while (true) {
			Scanner getUserPreference = new Scanner(System.in);
			System.out.println("Who should go first? (C)PU or (P)layer: ");
			String preference = getUserPreference.nextString();

			String bigC = "C";
			String smC = "c";
			String bigP = "P";
			String smP = "p";

			if !(preference.equals(bigC) || preference.equals(smC) || preference.equals(bigP) || preference.equals(smP)) {
				System.out.println("Invalid entry.");
				continue;
			} else {
				break;
			}
		}

		if (preference.equals(bigC) || preference.equals(smC)) {
			return true;
		} else {
			return false;
		}
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

	public static void checkIfGameOver(String[] board) {
		int spam = checkForWin(board);

		if (spam.equals("X")) {
			System.out.println("CPU WINS!");
			System.exit(0);
		}
		if (spam.equals("O")) {
			System.out.println("YOU WIN!");
			System.exit(0);
		}

		checkForTie(board);
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
	
	public static String checkForWin(String[] board) {
		if (board[0] == board[1] == board[2])
			return board[0];
		else if (board[3] == board[4] == board[5])
			return board[3];
		else if (board[6] == board[7] == board[8])
			return board[6];
		else if (board[0] == board[3] == board[6])
			return board[0];
		else if (board[1] == board[4] == board[7])
			return board[1];
		else if (board[2] == board[5] == board[8])
			return board[2];
		else if (board[0] == board[4] == board[8])
			return board[0];
		else if (board[2] == board[4] == board[6])
			return board[2];
		else
			return null;
	}

	public static int cpuStrategicMove(String[] board) {
	    ArrayList<Integer> possible_moves = new ArrayList<Integer>();

	    for (int spot = 0; spot <= board.length; spot++) {
			if !(board[spot] == "X" || board[i] == "O")
				available.add(spot);
		}

		String[] options = {"X", "O"};

		for (String i : options) {
			for (int j = 0; j < possible_moves.size(); j++) {
				int[] board_copy = board.clone();
				board_copy[move] = options[i];
				if checkForWin(board_copy)
					return board[move];
			}
		}

		ArrayList<Integer> good_spots = new ArrayList<Integer>();
		int[] good_options = {0, 2, 4, 6, 8};

		for (int k = 0; k < possible_moves.size(); k++) {
			if (Arrays.asList(possible_moves).contains(possible_moves[k]))
				good_spots.add(possible_moves[k]);
		}

		if (good_spots.contains(4))
			return 4;

		if (good_spots.size() > 0) {
			Random rand = new Random();
			int choice = rand.nextInt(available.length);
			return board[choice];
		}

		ArrayList<Integer> edge_spots = new ArrayList<Integer>();
		int[] edge_options = {0, 2, 4, 6, 8};

		for (int m = 0; m < possible_moves.size(); m++) {
			if (Arrays.asList(possible_moves).contains(possible_moves[m]))
				edge_spots.add(possible_moves[m]);
		}

		if (edge_spots.size() > 0) {
			Random rand = new Random();
			int choice = rand.nextInt(available.length);
			return board[choice];
		}
	}

}
