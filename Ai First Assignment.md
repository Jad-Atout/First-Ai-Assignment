# Assignment- Explanation


## Code 

### 1. Constants and Initial Setup

- **BOARD_SIZE**: Defines the size of the chessboard, which is 8x8.
- **KNIGHT_MOVES**: A list of all possible knight moves on the chessboard.
- **LETTERS**: a list of letters in the game (`'J', 'A', 'D', 'T', 'O', 'U'`).
- **state_1, state_2, state_3**: Different initial state examples.

### 2. Functions

#### `is_knight_move(start, end)`
This function checks if a knight can move from the `start` position to the `end` position.

#### `find_knight_path(state, current_position, visited)`
This recursive function find a valid path by checking if a knight can reach every other pieces. It returns `True`  or `False`.

#### `is_goal(state, start_letter)`
This function checks if the state has reached the goal where the knight starts from the position of the `start_letter`, can visit all the other pieces.

#### `get_new_states(current_state)`
This function gets all the possible new states from the current state. It computes valid moves for each piece on the board, where no piece occupies the same position as another. It returns a list of possible new states and their move descriptions.

#### `dfs(initial_state, start_letter)`
This function implements Depth First Search (DFS).

#### `bfs(initial_state, start_letter)`
This function implements Breadth First Search (BFS).

### 3. Main Program Flow

In the `main` function:

1. **User input**: The user enters the starting letter.
2. **DFS and BFS Execution**: The program runs both DFS and BFS algorithms to find the solution and prints out the results, including:
   - The final positions of the letters.
   - The sequence of moves made.
   - The number of expanded states during the search.

### 4. Example Output

Once the user selects a starting letter, the program will output the goal state, the path taken by each knight, and the number of expanded states.

#### Sample DFS Output:
    Now, let's try Breadth First Search (BFS)...

    Success! We found the goal using BFS!
    Goal State (final positions):
    A is at (3, 2)
    D is at (4, 3)
    J is at (1, 1)
    O is at (5, 5)
    T is at (2, 4)
    U is at (6, 7)

    Here's the sequence of moves in BFS:
    A moves from (2,2) to (3,2)
    D moves from (4,1) to (4,2)
    D moves from (4,2) to (4,3)
    O moves from (5,4) to (5,5)

    In BFS, we expanded 3002 states.


## Visualizing States

The following console outputs show the different states and their results:

1. **First state**:
   1. #### Initial State:
            ('J', (1, 1)),
            ('A', (2, 2)),
            ('D', (4, 1)),
            ('T', (2, 4)),
            ('O', (5, 4)),
            ('U', (6, 7))
     2. #### DFS Output:
              Goal State (final positions):
                  A is at (2, 2)
                  D is at (4, 1)
                  J is at (1, 1)
                  O is at (5, 4)
                  T is at (3, 3)
                  U is at (3, 0)
      
               Here's the sequence of moves in DFS:
      
                  U moves from (6,7) to (6,6)
                  U moves from (6,6) to (6,5)
                  U moves from (6,5) to (6,4)
                  U moves from (6,4) to (6,3)
                  U moves from (6,3) to (6,2)
                  U moves from (6,2) to (6,1)
                  U moves from (6,1) to (6,0)
                  U moves from (6,0) to (5,0).....
    
              In DFS, we expanded 121 states.
          
     3. #### BFS Output:
       Success! We found the goal using BFS!
       Goal State (final positions):
          A is at (3, 2)
          D is at (4, 3)
          J is at (1, 1)
          O is at (5, 5)
          T is at (2, 4)
          U is at (6, 7)

       Here's the sequence of moves in BFS:
         A moves from (2,2) to (3,2)
         D moves from (4,1) to (4,2)
         D moves from (4,2) to (4,3)
         O moves from (5,4) to (5,5)
          
       In BFS, we expanded 3002 states. 

  2. **Second state**:
     1. #### Initial State:
                 ('J', (3, 2)),
                 ('A', (4, 3)),
                 ('D', (5, 3)),
                 ('T', (4, 5)),
                 ('O', (6, 5)),
                 ('U', (4, 6))
     2. #### DFS Output:
            Goal State (final positions):
                A is at (4, 3)
                D is at (5, 3)
                J is at (3, 2)
                O is at (6, 2)
                T is at (2, 4)
                U is at (5, 0)
     
             Here's the sequence of moves in DFS:
     
                U moves from (3,0) to (4,0)
                U moves from (4,0) to (4,1)
                U moves from (4,1) to (4,2)
                U moves from (4,2) to (5,2)
                T moves from (2,5) to (2,4)
                U moves from (5,2) to (5,1)
                U moves from (5,1) to (5,0).....
  
            In DFS, we expanded 364 states.
     
     3. #### BFS Output:
            Success! We found the goal using BFS!
     
            Goal State (final positions):
                A is at (4, 4)
                D is at (5, 3)
                J is at (3, 2)
                O is at (6, 5)
                T is at (4, 5)
                U is at (4, 6)
     
            Here's the sequence of moves in BFS:
                A moves from (4,3) to (4,4)

            In BFS, we expanded 3 states. 

3. **Third state**:
   1. #### Initial State:
            ('J', (2, 3)),
            ('A', (3, 4)),
            ('D', (6, 2)),
            ('T', (1, 3)),
            ('O', (7, 3)),
            ('U', (8, 6))
   2. #### DFS Output:
          Goal State (final positions):
              A is at (3, 4)
              D is at (6, 2)
              J is at (2, 2)
              O is at (3, 3)
              T is at (4, 1)
              U is at (4, 3)
         
          Here's the sequence of moves in DFS:
       
            T moves from (1,2) to (1,1)
            U moves from (4,1) to (4,0)
            U moves from (4,0) to (3,0)
            U moves from (3,0) to (2,0)
            U moves from (2,0) to (2,1)
            U moves from (2,1) to (2,2)).....
    
        In DFS, we expanded 2352 states.
     
   3. #### BFS Output:
          Success! We found the goal using BFS!
          Goal State (final positions):
            A is at (4, 4)
            D is at (5, 2)
            J is at (3, 3)
            O is at (7, 3)
            T is at (1, 4)
            U is at (6, 5)
    
          Here's the sequence of moves in BFS:
            A moves from (3,4) to (4,4)
            D moves from (6,2) to (5,2)
            J moves from (2,3) to (3,3)
            T moves from (1,3) to (1,4)
            U moves from (8,6) to (7,6)
            U moves from (7,6) to (6,6)
            U moves from (6,6) to (6,5)
               
          In BFS, we expanded 159599 states. 

## How to Run the Code

1. Clone this repository to your local machine.
2. Install Python 3.10.
3. Run the Python script:
   ```bash
   python knight_move_game.py
