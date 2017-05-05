import random

class Card(Object):
    def __init__(self,rank,color,suit,special="Not"):
        self.rank=rank
        self.color=color
        self.suit=suit
        self.special=special
    def cards(self,card):
         suit_name= ['The suit of Spades','The suit of Hearts', 'The suit of Diamonds','Clubs']
         rank_name=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']Special related special card e.g. Joker

    def removed(self):



class Deck(Card):
    def __init__(self,*Card):
        self.deck_card_list=card

    def shuffle(self):
        self.deck_card_list=random.shuffle(self.deck_card_list)

    def deal(self,*Card):
        self.deck_card_list=self.deck_card_list.pop()


    def reset(self,player_card):
        self.card_list.insert(0,player_card)

class Player(Card):
    def __init__(self,*Card):
        self.player_card_list=card

    def fold(self):
        self.player_card_list=[]

    def show(self):
        self.player_card_list=[]



    def passdeal(self):
        self.player_card_list=self.player_card_list

    def receivedeal(self,*Card):
        self.player_card_list=card
    ### new round of cards

    def bustdeal(self):
        self.player_card_list=[]
