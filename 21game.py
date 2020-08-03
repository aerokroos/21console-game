import random

deck = [('A','♥'),('2','♥'),('3','♥'),('4','♥'),\
		('5','♥'),('6','♥'),('7','♥'),('8','♥'),\
		('9','♥'),('10','♥'),('J','♥'),('Q','♥'),\
		('K','♥'),\
		('A','♦'),('2','♦'),('3','♦'),('4','♦'),\
		('5','♦'),('6','♦'),('7','♦'),('8','♦'),\
		('9','♦'),('10','♦'),('J','♦'),('Q','♦'),\
		('K','♦'),\
		('A','♣'),('2','♣'),('3','♣'),\
		('4','♣'),('5','♣'),('6','♣'),\
		('7','♣'),('8','♣'),('9','♣'),\
		('10','♣'),('J','♣'),('Q','♣'),\
		('K','♣'),
		('A','♠'),('2','♠'),('3','♠'),\
		('4','♠'),('5','♠'),('6','♠'),\
		('7','♠'),('8','♠'),('9','♠'),\
		('10','♠'),('J','♠'),('Q','♠'),\
		('K','♠')]

my_cards, bob_cards = [], []
my_total, bobs_total = 0, 0
prompt = "\nWelcome to 21 Game(Similar to 21 Black Jack)"
prompt += "\nINSTRUCTIONS: The winner will win when the value of your cards"
prompt += "\nare 21 or when the player have more value than Bob"
prompt += "\nWho is Bob?, Bob, is your rival and he seeks to win you"
prompt += "\nI´m Bob (enter 'Y' key to continue)"
answer = None
game_status = True
first_rond = True
continue_g = False

def random_card(deck, list_cards):
    result = random.choice(deck)
    list_cards.append(result)
    deck.remove(result)
    return list_cards

def generate_bob_cards(bob_cards):
    bob_cards = random_card(deck, bob_cards)
    return bob_cards

def generate_my_cards(my_cards):
    my_cards = random_card(deck, my_cards)
    return my_cards

def ask_contains_as(name):
    prompt = "HEY: " + name.title() + " \
    How do you want to use the As? value 1? or value 11:"
    new_value = input(prompt)
    if new_value == 1:
        new_value = 1
    if new_value == 11:
        new_value = 1
    return new_value

def bob_dicede():
    new_value = None
    if new_value < 20 or new_value > 10:
        new_value+=11
    if new_value == 20:
        new_value+=1
    return new_value
        
def get_score(list_cards, total, name):
    val = [idx[0] for idx in list_cards]
    for v in val:
        if v !='J' and v !='Q' and v !='K' and v !='A':
            new = int(float(v))
            total+=new
        elif v == 'J' or v == 'Q' or v == 'K':
            total+=10
        elif v ==  'A' and name == 'bob':
            new_value = bob_dicede()
            total+=int(new_value)
        elif v == 'A' and name =='alberto':
            new_value = ask_contains_as(name)
            total+=int(new_value)
    return total

def check_who_won(bobs_total, my_total):
    if bobs_total > 21:
        print("\nBob Lose!!!")
        print("You win!!!")
    elif my_total > 21:
        print("\nYou Lose!!!")
        print("Bob win!!!")
    elif bobs_total <= 21 and bobs_total > my_total:
        print("\nBob win!!!")
        print("You Lose!!!")
    elif my_total <= 21 and my_total > bobs_total:
        print("\nYou win!!!")
        print("Bob Lose!!!")

answer = input(prompt)

while game_status:

    if first_rond:
        if answer == 'Y' or answer == 'y':
            print("\nHere we go!!!")
            print("\nBob´s card(just you can see a one card by him)")
            bob_cards = generate_bob_cards(bob_cards)
            bob_cards = generate_bob_cards(bob_cards)
            print(bob_cards[0])
            
            print("\nThese is your cards...")
            my_cards = generate_my_cards(my_cards)
            my_cards = generate_my_cards(my_cards)
            print(my_cards)
            first_rond = False

    answer = input("\nDo you want one more card?(Y/N):")
    if answer == 'Y' or answer == 'y':
        my_cards = generate_my_cards(my_cards)
        print(my_cards)
    elif answer == 'N' or answer == 'n':
        my_total = get_score(my_cards, my_total, "alberto")
        bobs_total = get_score(bob_cards, bobs_total, "bob")
            
        print("\n----- RESULTS -----")
        print("\nBob´s Score:" + str(bobs_total))
        print("Your Score:" + str(my_total))
        print("\nBob´s Cards")
        print(bob_cards)
        print("\nYour cards")
        print(my_cards)
        check_who_won(bobs_total, my_total)
        game_status = False
        
    
    
