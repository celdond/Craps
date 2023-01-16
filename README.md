# Craps

Craps is a dice game where players bet on the outcomes of the roll.
This program simulates a game of craps controlled by the terminal.

## Rules of the Game

To ensure clarity, the rules of the game are as follows:
- One player, in this case simply the user, is the shooter who throws
the pair of dice.
- Bets are placed before the dice are cast.
- If the first roll is a 2, 3, 7, 11, or 12, the round ends, and the
shooting restarts.  Otherwise, the number that was rolled is the point,
and the shooter will reroll until they reroll the point or a 7.

House rules ordain the kind of bets that can be made in this implementation.
Only one such bet is accepted, for the sake of simplicity:
- Pass Line Bet:  Made before the first roll, bets the dice will land on a 
7 or 11 first roll, or the point on the subsequent rolls.

## How to Run

As the program requires a terminal, the game needs a Python distribution to run.
Only standard libraries were used on Python 3.10.7.  Simply clone the repo, and 
run using your prefered environment from game.py.

## Implementation

As stated in the rules section, this version plays under "House Rules" - read as 
"With less rules".  The only time a bet may be made is at the start of a round.

On start up, the program will prompt input from the user with explanatory text.
In the case for a specified input, use integers only.  The number '0' is used to
quit.  With no specified input, enter or any input you want will suffice.  No 
different in result in this case.

A run will go as follows:
- Start up: select how many chips you would like to have at the start.  The value 
of these digital chips is what you give them.  In other words, they are not real.
Entering a non-integer value will terminate the run purposefully.
- Before a round: select how much you bet on your win.  This is a Pass Line Bet, 
and you must bet something or else quit.  You can bet as few or as many as you wish. 
Entering a non-integer number here will just make the game wag it's finger and ask 
again.
- Rolls: Rolling requires user input, so the user is not barraged by the outcome. 
Follows the rules as expect.
- Results:  Winning will add the chips to your total, while losing will lose you chips. 
If you run out of chips, the game will end.  If you still have chips, the game will 
keep going.

## Extra Functionality

Within craps.py is functionality for the game to play itself as well as statistical 
functions to display the chances of successful bets utilizing specific methods. 
None of these are attached to the game.py main function, and will need to be set-up 
in order to operate.