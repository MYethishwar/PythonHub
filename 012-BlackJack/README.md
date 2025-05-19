## Blackjack Project

This project is a simple implementation of the Blackjack card game. In Blackjack, the goal is to get cards with a total value as close to 21 as possible without going over. Here's a breakdown of how the project works:

### Deck of Cards

The game uses a standard deck of cards without jokers. Each card has a value: numbered cards are worth their face value, face cards (Jack, Queen, King) are worth 10, and Aces can be worth 11 or 1, whichever is more advantageous to the player.

### Gameplay

- The game starts by dealing two cards to the player and two cards to the dealer (computer).
- The player can see one of the dealer's cards but not the other.
- The player then decides whether to take additional cards ('hit') to improve their hand or stick with what they have ('stand').
- If the player's total exceeds 21, they bust and lose the game.
- After the player's turn, the dealer reveals their hidden card and draws additional cards if their total is below 17.
- If the dealer's total exceeds 21, they bust, and the player wins.
- The winner is determined based on who has the highest score without exceeding 21.

### Functions

- `deal_card()`: Returns a random card from the deck. This function is used to deal cards to both the player and the dealer.
- `calculate_score(cards)`: Takes a list of cards and returns the total score. Handles special cases like Blackjack and Aces. This function calculates the score for both the player and the dealer.
- `compare(user_score, computer_score)`: Compares the scores of the player and the dealer to determine the winner. It considers different scenarios like Blackjack, busting, and having the highest score.
- `play_game()`: Implements the main game loop, dealing cards, allowing the player to decide whether to hit or stand, and controlling the dealer's actions. This function orchestrates the entire game flow.
- `clear()`: Clears the console screen for a cleaner display. This function helps in maintaining a neat interface between game sessions.

### Restart Option

After each game, the player is asked if they want to play again. If they agree, the console is cleared, and a new game starts.

This project provides a basic but functional version of Blackjack that allows users to play against a computer dealer.
### Sample Output:
```plaintext

.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |
      `------'                           |__/

   Your cards: [6, 6], current score: 12
   Computer's first card: 10
Type 'y' to get another card, type 'n' to pass: y
   Your cards: [6, 6, 2], current score: 14
   Computer's first card: 10
Type 'y' to get another card, type 'n' to pass: y
   Your cards: [6, 6, 2, 1], current score: 15
   Computer's first card: 10
Type 'y' to get another card, type 'n' to pass: y
   Your cards: [6, 6, 2, 1, 8], current score: 23
   Computer's first card: 10
   Your final hand: [6, 6, 2, 1, 8], final score: 23
   Computer's final hand: [10, 10], final score: 20
You went over. You lose 😭
Do you want to play a game of Blackjack? Type 'y' or 'n': y-> Clears console screen and starts a nre game, n -> exit.
