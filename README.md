# tic-tac-toe-py
A simple command-line game of Tic Tac Toe

## How to Play

Just run `python tic_tac_toe.py` and the game will begin!
_Player X_ and _Player O_ will alternate turns until the game is done!

### What are the actions?

Each player will take turns typing in the coordinates of the position they want to take.
Because we are just using a matrix as the underlying data structure, we just pass in the indices of the matrix.


## Example Game Play
```
    $ python tic_tac_toe.py
    Let's play Tic Tac Toe!
    [0,0]   [0,1]   [0,2]
    [1,0]   [1,1]   [1,2]
    [2,0]   [2,1]   [2,2]
    Player X, select a square: row,col:1,1
    [0,0]   [0,1]   [0,2]
    [1,0]   [X]     [1,2]
    [2,0]   [2,1]   [2,2]
    Player O, select a square: row,col:0,0
    [O]     [0,1]   [0,2]
    [1,0]   [X]     [1,2]
    [2,0]   [2,1]   [2,2]
    Player X, select a square: row,col:2,0
    [O]     [0,1]   [0,2]
    [1,0]   [X]     [1,2]
    [X]     [2,1]   [2,2]
    Player O, select a square: row,col:0,2
    [O]     [0,1]   [O]
    [1,0]   [X]     [1,2]
    [X]     [2,1]   [2,2]
    Player X, select a square: row,col:0,1
    [O]     [X]     [O]
    [1,0]   [X]     [1,2]
    [X]     [2,1]   [2,2]
    Player O, select a square: row,col:2,1
    [O]     [X]     [O]
    [1,0]   [X]     [1,2]
    [X]     [O]     [2,2]
    Player X, select a square: row,col:1,2
    [O]     [X]     [O]
    [1,0]   [X]     [X]
    [X]     [O]     [2,2]
    Player O, select a square: row,col:1,0
    [O]     [X]     [O]
    [O]     [X]     [X]
    [X]     [O]     [2,2]
    Player X, select a square: row,col:2,2
    Stalemate there is no winner.
    [O]     [X]     [O]
    [O]     [X]     [X]
    [X]     [O]     [X]
``` 