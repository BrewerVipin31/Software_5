## Overview
This project implements a grid navigation algorithm to determine the number of possible locations that can be accessed from a starting point within a given number of steps. The program reads a grid from an input file, marks accessible cells, and counts the total number of accessible locations.

## Features
- Reads a grid from an input file.
- Marks cells as accessible if they can be reached within the specified number of steps.
- Outputs the total number of accessible locations.

## Files
- `main.py`: Main script that executes the grid navigation algorithm.
- `puzzle.txt`: Input file containing the grid.

## Input File Format
The input file should contain a grid where:
- `S` represents the starting position.
- `.` represents empty cells.
- '#' represents obstacles or walls.

## Code Explanation
- def file_input(file_path) :
- Reads the input file and converts its content into a 2D array of characters.
- def moving(row, column, grid, steps, visited) :
- Recursively explores the grid from the current position.
- Marks cells as accessible ('0') if they can be reached within the specified number of steps.
- Uses a set to track visited states to avoid redundant work.
- Main Function :
- Reads the input file and creates the grid.
- Identifies the starting position.
- Initiates the movement from the starting position.
- Counts and prints the number of accessible locations.

