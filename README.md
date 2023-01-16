# Craps

Craps is a dice game where players bet on the outcomes of the roll.
This program simulates a game of craps controlled by the terminal.

## Rules of the Game

To ensure clarity, the rules of the game are as follows:
- One player, in this case simply the user, is the shooter who throws
the pair of dice.
- Initial bets are placed before the dice are cast as well as on every
subsequent roll.
- If the first roll is a 2, 3, 7, 11, or 12, the round ends, and the
shooting restarts.  Otherwise, the number that was rolled is the point,
and the shooter will reroll until they reroll the point or a 7.
- Bets can be placed on every roll.

House rules ordain the kind of bets that can be made in this implementation.
Only two such bets are accepted, for the sake of simplicity:
- Pass Line Bet:  Made before the first roll, bets the rolls will land on a 
7 or 11 first roll, or the point on the subsequent rolls.
- Come Bet:  Bets on the point to roll after the first roll is made.