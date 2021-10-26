# AIAgents

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

