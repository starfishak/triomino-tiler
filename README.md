# L-Shaped Triomino Tiler
COMP 361: Victoria University of Wellington. Assignment 1 Question 5.1 and 5.2.

This algorithm can graph any 2^n board with a time complexity of between n^2 and n*log(n). 

# Running
Clone the repo and access the folder. Make modifications to the results file path at line 197.
Run the Python code in your command line. The program can either create 1 2^n board and print the output or run a time complexity analysis on 0 to n boards, where n^2 is the board size.
Choose option 1 or 2 and select a maximum N to tile the board. A 2^9 Board will take < 10 seconds while a 2^15 board will take > 6 minutes. Keep this in mind.
NB! This project was not developed with UX in mind. All interactions with the tiler are done in command line.

# Output
Single Board output will consist of points with tile type and a full graphically printed board. The points and the tile types are of the inner coordinate of the L with respect to the Cartesian Plane.

# Analysis
See the "Analysis.pdf" file for full overview of time complexity of algorithm.
