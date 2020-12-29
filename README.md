# Unbeatable Tic Tac Toe AI

This repository contains java and python3 implementations of a console tic-tac-toe AI that can only win or tie with the player.

## Getting Started

First clone the entire repository. 

If you want to run the python3 version,
```
cd python_programs/
```
then, run:
```
python main.py
```
or
```
python3 main.py
```

If you want to run the java version (works for Linux or WSL),
```
cd java_programs/
```
then compile:
```
javac Tictactoe.java
```
and run with:
```
java Tictactoe
```

### Downloads

* java_programs/
    * Tictactoe.java: comprehensive java program
* python_programs/
    * evaluate.py: functions that check the board for whether the game has ended, tied or is still going
    * strategy.py: the bulk of the AI - a brute-force method for finding the optimal move for the cpu
    * main.py: the main code and other miscellaneous functions
