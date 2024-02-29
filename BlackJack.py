import pygame
from Hand import *
from Deck import *
from Card import *
from settings import *

"""
BlackjackGame class

This class represents a game of Blackjack. It has methods to deal initial cards, handle the player's turn, dealer's turn, and determine the winner.
"""
class BlackjackGame:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.card_images, self.cover = self.load_card_images()
        self.status = "initial"
        self.prev_status = None
        self.message = None

    def change_status(self, new_status):
        self.prev_status = self.status
        self.status = new_status

    def load_card_images(self):
        card_images = {}
        cover = pygame.transform.scale(pygame.image.load("images/cover.png"), (CARD_WIDTH, CARD_HEIGHT))
        for suit in Card.suits:
            for rank in Card.ranks:
                card_name = f"{rank}_of_{suit.lower()}.png"
                card_images[(rank, suit)] = pygame.transform.scale(pygame.image.load(f"images/{card_name}"), (CARD_WIDTH, CARD_HEIGHT))
        return card_images, cover

    def draw_card(self, card: Card, x, y):
        if card is None:
            image = self.cover
        else:
            image = self.card_images[(card.rank, card.suit)]
        self.screen.blit(image, (x, y))

    def deal_cards(self):
        self.player_hand.add_card(self.deck.draw())
        self.dealer_hand.add_card(self.deck.draw())
        self.player_hand.add_card(self.deck.draw())
        self.dealer_hand.add_card(self.deck.draw())

    def reset(self, game_id):
        if game_id == 1:
            self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.deal_cards()
        self.status = PLAYER_TURN_STATUS
        
    def update(self, game_id, running):
        if self.status == INIT_STATUS:
            game_id += 1
            self.reset(game_id)
        elif self.status == PLAYER_TURN_STATUS:
            if self.player_hand.get_value() == BLACKJACK and len(self.player_hand.cards) == STARTING_HAND_SIZE:
                self.status = WIN_STATUS
                self.message = BLACKJACK_WIN
        elif self.status == DEALER_TURN_STATUS:
            d_hand = self.dealer_hand.get_value()
            p_hand = self.player_hand.get_value()
            while d_hand < DEALER_STAND:
                self.dealer_hand.add_card(self.deck.draw())
                d_hand = self.dealer_hand.get_value()
            if d_hand > BLACKJACK:
                self.status = WIN_STATUS
                self.message = DEALER_BUST
            elif d_hand > p_hand:
                self.status = LOSE_STATUS
                self.message = DEALER_WIN
            elif d_hand == p_hand:
                self.status = PUSH_STATUS
                self.message = PUSH
            else:
                self.status = WIN_STATUS
                self.message = WIN

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.change_status(QUIT_STATUS)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and self.status != QUIT_STATUS:
                    self.change_status(QUIT_STATUS)
                elif self.status == PLAYER_TURN_STATUS:
                    if event.key == pygame.K_h:
                        self.hit()
                        if self.player_hand.get_value() > BLACKJACK:
                            self.status = LOSE_STATUS
                            self.message = BUST
                    elif event.key == pygame.K_s:
                        self.status = DEALER_TURN_STATUS
                elif self.status == QUIT_STATUS:
                    if event.key == pygame.K_y:
                        running = False
                    elif event.key == pygame.K_n:
                        self.status = self.prev_status
                elif self.status in END_GAME_STATUSES:
                    if event.key == pygame.K_q:
                        running = False
                    elif event.key == pygame.K_r:
                        self.status = INIT_STATUS
                        game_id = 0
                    elif event.key == pygame.K_c:
                        self.status = INIT_STATUS
        return game_id, running

    def render(self):
        self.screen.fill(BG_COLOR)
        for i, card in enumerate(self.player_hand.cards):
            self.draw_card(card, int(self.screen.get_width() / 2 - CARD_WIDTH / 2) + i * CARD_WIDTH * CARD_GAP_SCALE, 
                                 int(self.screen.get_height() - CARD_HEIGHT - self.screen.get_height() * HEIGHT_GAP_SCALE))
        for i, card in enumerate(self.dealer_hand.cards):
            if i == 0 and (self.status == PLAYER_TURN_STATUS or (self.status == QUIT_STATUS and self.prev_status == PLAYER_TURN_STATUS)):
                self.draw_card(None, int(self.screen.get_width() / 2 - CARD_WIDTH / 2) + i * CARD_WIDTH * CARD_GAP_SCALE, 
                                     int(self.screen.get_height() * HEIGHT_GAP_SCALE))
            else:
                self.draw_card(card, int(self.screen.get_width() / 2 - CARD_WIDTH / 2) + i * CARD_WIDTH * CARD_GAP_SCALE, 
                                     int(self.screen.get_height() * HEIGHT_GAP_SCALE))

        if self.status in END_GAME_STATUSES:
            self.display_message(f"{self.message}!  -->  Press Q to quit, R to restart, C to continue playing...")
        elif self.status == QUIT_STATUS:
            self.display_message("Are you sure you want to quit? (Y/N)")

    def display_message(self, message):
        font = pygame.font.Font(None, TEXT_FONT_SIZE)
        text = font.render(message, True, TEXT_COLOR)
        text_rect = text.get_rect(center=(400, 300))
        self.screen.blit(text, text_rect)

    def hit(self):
        self.player_hand.add_card(self.deck.draw())

    def run(self):
        running = True
        game_id = 0
        while running:
            game_id, running = self.update(game_id, running)
            self.render()
            pygame.display.flip()