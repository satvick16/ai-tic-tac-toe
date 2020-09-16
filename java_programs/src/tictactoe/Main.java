/**
 * 
 */
package tictactoe;

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
		for (int i: options) {
			
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

}
