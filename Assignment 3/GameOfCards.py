# ITI 1120
# 300042722
# Qiguang Chu

# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]
     for i  in range (51):
         if (i%2) == 0:
             dealer.append(deck[i])
         else:
             other.append(deck[i])

     return (dealer, other)
 

def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]


    for i in ('2','3','4','5','6','7','8','9','10','J','Q','K','A'):
        n = []
        for j in range(len(l)):
            if l[j].find(i) != -1:
                n.append(l[j])
        if len(n) == 2 or len(n) == 3:
            l.remove(n[0])
            l.remove(n[1])
        elif len(n) == 4:
            l = [x for x in l if x not in n]
    no_pairs = l

    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    for i in range (len(deck)):
        print(deck[i], end = ' ')

def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''
     print("Give me an integer between 1 and", n, ": ", end="")
     a = input()
     while ((a.isdigit() == False) or (int(a) < 1 and int(a) > n)):
         print("Invalid number. Please enter integer between 1 and ", n, ": ")
         a = input()
     return int(a)

def play_game():
     '''()->None
     This function plays the game'''

     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("\nDo not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")

     i = 0
     m = 0
     while len(dealer+human) != 1:
         wait_for_player()
         print("***********************************************************")
         dealer = remove_pairs(dealer)
         human = remove_pairs(human)
         if i%2 == 0:
             print("\nYour turn.\n")
             print_deck(human)
             print("\nI have ",len(dealer)," cards. If 1 stands for my first card and "
, len(dealer), " for my last card, which of my cards would you like?\n")

             a = get_valid_input(len(dealer))

             print("You asked for my No.",a,"card.")
             print("Here it is. It is ", dealer[a-1], "\n")
             print("With ",dealer[a-1]," added, your current deck of cards is:\n")
             human.append(dealer[a-1])
             dealer.remove(dealer[a-1])
             print_deck(human)
             print("\n")
             print("And after discarding pairs and shuffling, your deck is:\n")
             remove_pairs(human)
             print_deck(human)
             if dealer == []:
                 m = 0
                 break
             if human == []:
                 m = 1
                 break
             wait_for_player()
             i = i + 1
         if i%2 == 1:
             print("***********************************************************")
             print("My turn.\n")
             c = random.randint(1,len(human))
             print("I took your No.", c, " card.")
             dealer.append(human[c-1])
             human.remove(human[c-1])
             if dealer == []:
                 m = 0
                 break
             if human == []:
                 m = 1
                 break
             i = i + 1

     if m == 1:
         print("Ups. You do not have any more cards\n Congratulations! You, Human, win")
     if m == 0:
         print("Ups. I do not have any more cards\nYou lost! I, Robot, win")
     print("\n")


# main
play_game()
