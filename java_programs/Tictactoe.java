/**
 * 
 */

import java.util.Random;
import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;

/**
 * @author Satvick Acharya
 *
 */
public class Tictactoe {

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
			int p_move = getPMove(board);
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
		Scanner getUserPreference = new Scanner(System.in);
		System.out.println("Who should go first? (C)PU or (P)layer: ");
		String preference = getUserPreference.nextLine();

		if (preference.equals("C") || preference.equals("c")) {
			return true;
		} else {
			return false;
		}
	}
	
	public static int getPMove(String[] board) {
		ArrayList<Integer> available = new ArrayList<Integer>();
		
		for (int i = 0; i < board.length; i++) {
			if (!(board[i].equals("X") || board[i].equals("O")))
				available.add(i);
		}
		
		Scanner getPMove = new Scanner(System.in);
		System.out.println("Your move: ");
		int move = getPMove.nextInt();

		int rmove = move - 1;
		return rmove;
	}

	public static void checkIfGameOver(String[] board) {
		String spam = checkForWin(board);

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

		for (String i : board) {
			if (!(i.equals("O") || i.equals("X")))
				available++;
		}

		if (available == 0) {
			System.out.println("IT'S A TIE!");
			System.exit(0);
		}
	}
	
	public static String checkForWin(String[] board) {
		if (board[0].equals(board[1]) && board[0].equals(board[2]))
			return board[0];
		else if (board[3].equals(board[4]) && board[3].equals(board[5]))
			return board[3];
		else if (board[6].equals(board[7]) && board[6].equals(board[8]))
			return board[6];
		else if (board[0].equals(board[3]) && board[0].equals(board[6]))
			return board[0];
		else if (board[1].equals(board[4]) && board[1].equals(board[7]))
			return board[1];
		else if (board[2].equals(board[5]) && board[2].equals(board[8]))
			return board[2];
		else if (board[0].equals(board[4]) && board[0].equals(board[8]))
			return board[0];
		else if (board[2].equals(board[4]) && board[2].equals(board[6]))
			return board[2];
		else
			return "false";
	}

	public static int cpuStrategicMove(String[] board) {
	    ArrayList<Integer> possible_moves = new ArrayList<Integer>();

	    for (int spot = 0; spot < board.length; spot++) {
			if (!(board[spot] == "X" || board[spot] == "O"))
				possible_moves.add(spot);
		}

		String[] options = {"X", "O"};

		for (String letter : options) {
			for (int move : possible_moves) {
				String[] board_copy = board.clone();
				board_copy[move] = letter;
				if (checkForWin(board_copy) != "false")
					return move;
			}
		}

		ArrayList<Integer> good_spots = new ArrayList<Integer>();
		int[] good_options = {0, 2, 4, 6, 8};

		for (int i : possible_moves) {
			if (Arrays.asList(good_options).contains(i))
				good_spots.add(i);
		}

		if (good_spots.contains(4))
			return 4;

		if (good_spots.size() > 0) {
			Random rand = new Random();
			int choice = rand.nextInt(good_spots.size());
			return good_spots.get(choice);
		}

		ArrayList<Integer> edge_spots = new ArrayList<Integer>();
		int[] edge_options = {1, 3, 5, 7};

		for (int i : possible_moves) {
			if (Arrays.asList(edge_options).contains(i))
				edge_spots.add(i);
		}

		if (edge_spots.size() > 0) {
			Random rand = new Random();
			int choice = rand.nextInt(edge_spots.size());
			return edge_spots.get(choice);
		}

		return 0;
	}

}
