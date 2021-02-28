
user_choice = input('Please enter a letter: r for rock, p for paper or s for scissors ')

def users_selection():
    if user_choice == ('r' or 'R'):
        user_choice = 'Rock')
    elif user_choice == ('p' or 'P'):
        print('Paper')
    elif user_choice == ('s' or 'S'):
        print('Scissors')
    else:
        print('That is not a valid choice. Please try again.')

print(f"Player's choice is {users_choice}")



#def options():
#    opponent_choice = random.randint(0, 2)
#    if opponent_choice == 0:
#        print('Rock')
#    elif opponent_choice == 1:
#         print('Paper')
#     else:
#         print('Scissors')
#
#     print(options())
#
#     print("User's choice: {} Opponent's choice: {}".format(user_choice, opponent_choice))