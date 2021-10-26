# AI Agents

This project implements 2 simple AI agents -

-   1 Dimensional vacuuum bot
-   Pile game bot

## 1 Dimensional Vacuum Bot

In this scenario, there is a vacuum bot that cleans dust.

-   The environment is a single dimensional row of cells. Each cell can either be
    dirty or clean.
-   The bot can start at any cell of the environment
-   On each step, the bot can do one of these 3 actions:
    -   `SUCK` - Clean the dust on the current cell
    -   `LEFT` - Move to the cell on the left. Stay on the cell if no cell on the left
    -   `RIGHT` - Move to the cell on the right. Stay on the cell if no cell on the right
-   Each time the bot execute `SUCK` and cleans the cell, the score of the bot
    increases by 1.
-   Final score of the bot is the number of cells it has cleaned

The following is the state space search graph of the given scenario:
![Vacuum State Space Graph][vacuum-state-space]

The following shows the output of 2 simulations run separately:
![Vacuum Simulation Screenhot][vacuum-ss]

## Pile Game Bot

In this scenario, there are 2 piles of stones and 2 players.

-   A player can remove any number of stones from one pile
-   The game is turn based
-   A player loses if there are no more stones left on their turn
-   The initial number of stones is taken as input

### The Bot

The bot uses a MiniMax algorithm to decide the best move on each turn. The bot
can play against another bot or a human player.

The end states (leaf nodes) are evaluated as:

-   `1` - If player 1 wins
-   `-1` - If player 2 wins

The minimax algorithm is run based on this evaluation. Player 1 tries to get the
maximum score and Player 2 tries to get the minimum score.

Following images shows a bot vs bot match:

![Bot vs Bot][pile-bot-ss]

### The human player

The human player may input his action as:

-   `n 0` - Remove `n` stones from first pile
-   `0 n` - Remove `n` stones from second pile

Following image shows a bot vs human match:

![Bot vs Human][pile-human-ss]

[vacuum-state-space]: images/VacuumAgentStateSpace.svg
[vacuum-ss]: images/vacuuum-ss.png
[pile-bot-ss]: images/pile-bot-ss.png
[pile-human-ss]: images/pile-human-ss.png
