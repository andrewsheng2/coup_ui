import pygame

class Player(object):
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.coins = 0
        self.status = ""
    
    #List of character-specific actions that the players can take:
    def assassinate(self, otherPlayer):
        #spend 3 coins
        #target otherPlayer
        #assassin's action
        pass
        
    def swap(self, deck):
        #draw two cards from deck
        #choose two cards to put back in deck
        #ambassador's action
        
        pass
        
    def steal(self, otherPlayer):
        #target otherPlayer
        #take two coins from otherPlayer
        #captain's action
        
        pass
        
    def take3Coins(self):
        #duke's action
        pass
        
    #List of actions that everyone can take
        
    def take1Coin(self):
        pass
        
    def take2Coins(self):
        pass
        
    def launchCoup(self, otherPlayer):
        #target otherPlayer
        #spend 10 coins
        #kill a character from otherPlayer
        #cannot be challenged or blocked
        
        pass

    #reactions
    
    #in these cases, action is the message received
    def challenge(self, action):
        pass
        
    def block(self, action):
        pass
    
            
        