from art import logo
import random

def play_game(): #main function

    print(logo)

    def deal_card(): #function that distributes card
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

    user_cards = []
    computer_cards = []

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #dealing 2 cards to both user_cards and computer_cards

    print("Your cards are below:")
    print(user_cards)
    print("Computer cards are below:")
    print(computer_cards)

    def calculate_score(list_of_cards): #function that calculates score by sum of cards
        sum_of_list = sum(list_of_cards)
        if sum_of_list == 21: #check for the blackjack at the first 2 cards
            sum_of_list = 0 # 0 will represent blackjack at our game
        if sum_of_list > 21:
            if 11 in list_of_cards:
                list_of_cards.remove(11)
                list_of_cards.append(1) #removing [11,11] situation by fixing to [1,11]
        return sum_of_list

    calculate_score(user_cards) #calculating users score
    calculate_score(computer_cards) #calculating computers score

    print("Your Score is below:")
    print(calculate_score(user_cards))
    print("Computer's Score is below:")
    print(calculate_score(computer_cards))

    check_game = True #checking the conditions for the game rules
    while check_game:
        answer = input("Game Continues... Would you like to draw a extra card ?").lower()
        if answer == "yes":
            user_cards.append(deal_card())
            print("Your new deck is below:")
            print(user_cards)
            calculate_score(user_cards)
            print("Your new score is below:")
            print(calculate_score(user_cards))
            if calculate_score(user_cards) == 0:
                check_game = False
            elif calculate_score(user_cards) > 21:
                check_game = False

        elif answer == "no":
            print("You choose not to draw card!")
            check_game = False

    while calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())
        calculate_score(computer_cards)
        print("Computer chooses to draw card. Computer's new deck is below:")
        print(computer_cards)
        print("Computer's new score is below:")
        print(calculate_score(computer_cards))

    def compare (user_score, computer_score):
        if user_score == computer_score:
            print("It's a Draw! Game Over!")
        elif computer_score == 0:
            print("Computer has a BlackJack! You Lost!")
        elif user_score == 0:
            print("You have a BlackJack! You Won!")
        elif computer_score > 21:
            print("Computer exceeded 21! You Won!")
        else:
            if user_score > computer_score:
                print("You have a Higher Score! You Won!")
            else:
                print("You have a Smaller Score! You Lost!")

    compare(calculate_score(user_cards),calculate_score(computer_cards))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()