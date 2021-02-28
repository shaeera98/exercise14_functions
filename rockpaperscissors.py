import random
user_choice = input('Please enter a letter: r for rock, p for paper or s for scissors ')

def users_selection():
    if user_choice == ('r' or 'R'):
        choice = ('Rock')
    elif user_choice == ('p' or 'P'):
        choice = ('Paper')
    elif user_choice == ('s' or 'S'):
        choice = ('Scissors')
    else:
        choice = ('That is not a valid choice. Please try again.')
    return choice

player1 = users_selection()
print(users_selection())
# print(f"Player's choice is {users_choice}")


def opponent():
    opponent_selection = random.randint(0, 2)
    if opponent_selection == 0:
        opponent_choice = ('Rock')
    elif opponent_selection == 1:
        opponent_choice = ('Paper')
    else:
        opponent_choice = ('Scissors')
    return opponent_choice

player2 = opponent()
print(opponent())

if player1 =="Rock":
    if player2 == "Rock":
        print("It's a draw ;)")
    elif player2 == "Paper":
        print("Paper wraps rock, you lose ;(")
    else:
        print("Rock smashes scissors, you win!")

if player1 =="Paper":
    if player2 == "Paper":
        print("It's a draw ;)")
    elif player2 == "Scissors":
        print("Scissors cut paper, you lose ;(")
    else:
        print("Paper wraps rock, you win!")

if player1=="Scissors":
    if player2 == "Scissors":
        print("It's a draw ;)")
    elif player2 == "Rock":
        print("Rock smashes scissors, you lose ;(")
    else:
        print("Scissors cut paper, you win!")
#     print("User's choice: {} Opponent's choice: {}".format(user_choice, opponent_choice))