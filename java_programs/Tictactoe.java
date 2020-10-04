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
	
	public static void checkForWin(String[] board) {
		//TODO: '==' operator does not work for String data type
		
		if (board[0].equals(board[1]).equals(board[2]).equals("X")) {
	        System.out.println("CPU WINS!");
	        System.exit(0);
		} else if (board[3] == board[4] == board[5] == "X") {
	        System.out.println("CPU WINS!");
	        System.exit(0);
		} else if (board[6] == board[7] == board[8] == "X") {
	        System.out.println("CPU WINS!");
	        System.exit(0);
		} else if (board[0] == board[3] == board[6] == "X") {
	        System.out.println("CPU WINS!");
	        System.exit();
		} else if (board[1] == board[4] == board[7] == "X") {
	        System.out.println("CPU WINS!");
	        System.exit(0);
		} else if (board[2] == board[5] == board[8] == "X") {
	        System.out.println("CPU WINS!");
	        System.exit(0);
		} else if (board[0] == board[4] == board[8] == "X") {
	        System.out.println("CPU WINS!");
	        System.exit(0);
	    	} else if (board[2] == board[4] == board[6] == "X") {
	        System.out.println("CPU WINS!");
	        System.exit(0);
		}
	}

}
