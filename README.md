# Project: Text-Based Blackjack (CPT Milestone 4)

**Author:** SharkieBite
**Date:** January 20, 2023  
**Language:** Python  

---------------------------------------------------------

This program is a fully functional, text-based simulation of the worldwide card game "Blackjack." Developed as a Culminating Performance Task (CPT), this project demonstrates the use of Python to create an interactive game loop, manage a virtual economy, and handle user inputs via keyboard events without the need for a graphical user interface.

## Functionality & Features

### Virtual Economy
* **Starting Balance:** Players begin with **$1500**.
* **Betting:** Users can choose from preset bet amounts ($25, $50, $100, etc.) or input a **custom wager**.
* **Winning/Losing:** Balances update automatically based on game outcomes (1.5x payout for natural Blackjack).

### Game Mechanics
* **Round Selection:** Play a specific set of rounds (5, 10, 25, 50) or a custom number.
* **Hit:** Request another card to get closer to 21.
* **Stand:** Lock in your score and let the dealer play.
* **Dealer AI:** The dealer automatically draws cards until they reach a total of 16 or higher.
* **Ace Handling:** The logic automatically calculates Aces as 1 or 11 to give the best possible score.

### Statistics & Data
* **Session Tracking:** The program tracks total rounds played, total wins, total losses, and total money won/lost.
* **Menus:** Includes a Credits screen and a dedicated Statistics view.

## Dependencies & Installation

This program requires the **`readchar`** module to detect key presses instantly (allowing for a smoother menu experience without pressing "Enter").

### 1. Install Dependencies
Open your terminal or command prompt and run:
```bash
pip install readchar
