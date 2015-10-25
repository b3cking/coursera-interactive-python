# Implementation of card game BlackJack
# Istvan Kis - Interactive programming in Python - homework @ Rice University
# http://istvankis.net

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = mesage = ""
score = 0
deck = 0
player_hand = 0
dealer_hand = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = []
        self.has_aces = False

    def __str__(self):
        # return a string representation of a hand
        i = 0
        handstr = "Hand contains "
        while i < len(self.cards):
            handstr = handstr + str(self.cards[i]) + " "
            i += 1
        return handstr
    
    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0 
        for card in self.cards:
            card_rank = card.get_rank()
            if (card_rank == "A"):
                self.has_aces = True
                value += 1
            elif card_rank in ['J', 'Q', 'K', 'T']:
                value += 10
            else:
                value += int(card_rank)
            
        if (self.has_aces == False):
            return value
        elif value + 10 <= 21:
            return value + 10
        else:
            return value
        return value
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        i = 0
        for card in self.cards:
            card.draw(canvas, [pos[0] + i * CARD_SIZE[0], pos[1]])
            i += 1
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))
                
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            print "DEBUG: No card."
            return None
    
    def __str__(self):
        # return a string representing the deck
        i = 0
        deckstr = "Deck contains "
        while i < len(self.cards):
            deckstr = deckstr + str(self.cards[i]) + " "
            i += 1
        return deckstr    

#define event handlers for buttons
def deal():
    global outcome, message, in_play, deck, player_hand, dealer_hand, score
    outcome = ""
    message = "Hit or Stand?"
    if in_play:
        outcome = "You lost last round."
        score -= 1
    player_hand = Hand()
    dealer_hand = Hand()
    deck = Deck()
    deck.shuffle()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    print "Player -", player_hand
    print "Dealer -", dealer_hand
    in_play = True

def hit():
    global player_hand, in_play, score, outcome, message
    # if the hand is in play, hit the player
    if in_play:
        outcome = ""
        player_hand.add_card(deck.deal_card())        
    # if busted
        if player_hand.get_value() > 21:
            in_play = False
            score -= 1
            outcome = "You went bust and lose"
            message = "New deal?"
            
def stand():
    global dealer_hand, score, in_play, outcome, message
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        in_play = False
        while dealer_hand.get_value() <= 17:
            dealer_hand.add_card(deck.deal_card())        
        if dealer_hand.get_value() >=  player_hand.get_value() and dealer_hand.get_value() <= 21:
            score -= 1
            outcome = "You lose!"
        else:
            score += 1
            outcome = "You won!"
        message = "New deal?"
        
# draw handler    
def draw(canvas):
    canvas.draw_text('Black', (20, 50), 50, 'Black')
    canvas.draw_text('Jack', (140, 50), 50, 'White')
    canvas.draw_text('Dealer', (70, 160), 27, 'Black')
    canvas.draw_text('Score: ' + str(score), (370, 50), 27, 'Black')
    canvas.draw_text('Player', (70, 360), 27, 'Black')
    canvas.draw_text(message, (270, 360), 27, 'White')
    canvas.draw_text(outcome, (270, 160), 27, 'Yellow')
    player_hand.draw(canvas, [50,400])
    dealer_hand.draw(canvas, [50,200])
    if in_play:
        canvas.draw_image(card_back, [CARD_BACK_SIZE[0] / 2, CARD_BACK_SIZE[1] / 2], 
                          CARD_BACK_SIZE, [50 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], 
                          CARD_BACK_SIZE)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
