# Description: This file contains the settings for the blackjack game.
# Constants

# Card dimensions
CARD_WIDTH = 166
CARD_HEIGHT = 242

# Card gap between each other (0.75 means 3/4 of the card width so there is a 1/4 of the card width gap)
CARD_GAP_SCALE = 0.75

# Gap between cards and the screen border
HEIGHT_GAP_SCALE = 0.025

# Background color
BG_COLOR = (0, 128, 0)

# Text color and size
TEXT_COLOR = (0, 0, 0)
TEXT_FONT_SIZE = 36

# Game info
BLACKJACK = 21
STARTING_HAND_SIZE = 2
DEALER_STAND = 17

# Game statuses message
BLACKJACK_WIN = "That's a blackjack, you win"
DEALER_BUST = "Dealer busts, you win"
DEALER_WIN = "Dealer wins"
PUSH = "Game is a push"
BUST = "Bust, you lose"
WIN = "You win"

# Game statuses
WIN_STATUS = "win"
LOSE_STATUS = "lose"
PUSH_STATUS = "push"
QUIT_STATUS = "confirm_quit"
INIT_STATUS = "initial"
PLAYER_TURN_STATUS = "player_turn"
DEALER_TURN_STATUS = "dealer_turn"
END_GAME_STATUSES = [WIN_STATUS, LOSE_STATUS, PUSH_STATUS]