# Rock, Paper, Scissors Game

## Overview
This is a two-player Rock, Paper, Scissors game implemented in Python. The game allows two players to compete against each other in a best-of-5 format, where the first player to reach 5 wins becomes the overall winner.

## File Information
- **File**: `def_r_p_s.py`
- **Location**: `Practice/` folder
- **Language**: Python 3

## Features
- **Two-player gameplay**: Players take turns making their choices
- **Secure input**: Uses `getpass` module to hide player inputs during gameplay
- **Score tracking**: Keeps track of each player's wins
- **Input validation**: Ensures only valid choices (r, p, s) are accepted
- **Best-of-5 format**: First player to reach 5 wins is declared the winner
- **Real-time feedback**: Shows round results and current scores

## How to Play

### Game Rules
1. **Rock (r)** beats **Scissors (s)**
2. **Paper (p)** beats **Rock (r)**
3. **Scissors (s)** beats **Paper (p)**
4. **Ties** occur when both players choose the same option
5. **First to 5 wins** becomes the overall winner

### Input Commands
- `r` - Rock
- `p` - Paper  
- `s` - Scissors

### Gameplay Flow
1. Player 1 enters their choice (input is hidden)
2. Player 2 enters their choice (input is hidden)
3. Round result is displayed with updated scores
4. Game continues until one player reaches 5 wins
5. Final scores and winner are announced

## Code Structure

### Main Function: `rock_paper(rock, paper, scissors)`
- **Parameters**: 
  - `rock`: Character representing rock (default: 'r')
  - `paper`: Character representing paper (default: 'p')
  - `scissors`: Character representing scissors (default: 's')
- **Purpose**: Handles the main game logic and scoring

### Game Function: `game()`
- **Purpose**: Entry point for the game (currently has a minor implementation issue)

## Dependencies
- **Python Standard Library**: `getpass` module
  - Used for secure input handling to hide player choices during gameplay

## Usage

### Running the Game
```bash
cd Practice
python def_r_p_s.py
```

### Example Game Session
```
Player 1's turn: input r for rock, p for paper and s for scissors: 
Player 2's turn: input r for rock, p for paper and s for scissors: 

Player 1 won the round, the score is 1

Player 1's turn: input r for rock, p for paper and s for scissors: 
Player 2's turn: input r for rock, p for paper and s for scissors: 

Its a tie!!!

... (game continues until someone reaches 5 wins)
```

## Technical Notes

### Input Security
The game uses `getpass.getpass()` which:
- Hides player input during gameplay
- Prevents other players from seeing choices
- Enhances fair play and game integrity

### Score System
- Each round win adds 1 point to the winning player's score
- Ties result in no points awarded
- Game ends when either player reaches exactly 5 points

### Input Validation
- Only accepts 'r', 'p', or 's' as valid inputs
- Invalid inputs prompt an error message and allow retry
- Input is automatically converted to lowercase for consistency

## Known Issues
- The `game()` function has a minor implementation issue in the `if __name__ == '__main__':` block
- The main game function is called directly at module level

## Future Improvements
- Add a menu system for game options
- Implement single-player mode against computer
- Add statistics tracking across multiple games
- Include sound effects or visual enhancements
- Add option to customize winning score threshold

## Author
This game was created as a Python practice exercise focusing on:
- Function definitions and parameters
- Control flow with loops and conditionals
- User input handling
- Score tracking and game state management
- Basic game logic implementation
