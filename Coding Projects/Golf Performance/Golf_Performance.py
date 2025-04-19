#Import External Files
from Title_Screen import title_screen
from Clear_Screen import clear_screen
from Loading_Screen import progress_bar

# Variables and list for get_player_names
players = []
players_dict = {}
player_count = 1
entry_count = 1


#Get Player Names and Display    
def get_player_names():
    global player_count #Declare Global Variable
    global entry_count   #Declare Global Variable
    user_input = 'player'
    while user_input != '':
        user_input = input(f'Enter Player {entry_count} Name: ')
        if user_input== '':
            break
        else:
            user_input = user_input.split()
            players.append(user_input)
        entry_count +=1
    print('\n')        
    print('Player Entries')
    print('--------------------')
    for player in players:
        player_join = ','.join(player)
        print(f'Player {player_count}:{player_join}\n')
        player_count +=1
    input('Players have been entered. Do you want to continue?(y/n)')



    
def game_start(round):
   if round == 3:
        Course_num = 1
        list_value = 0
        while Course_num < 4:
            Course_par = input(f'What is Par for Course {Course_num}: ')
            for player in players:
                print("\n")
                print(f'Total Strokes for {player[list_value]} on Course {Course_num}: ')
                amount_of_strokes = int(input())
                player.append(amount_of_strokes)
            print('----------------')   
            print(players)
            input()
            Course_num +=1
            clear_screen()
            title_screen()
   elif round == 6:
        Course_num = 1
        list_value = 0
        while Course_num < 7:
            Course_par = input(f'What is Par for Course {Course_num}: ')
            for player in players:
                print("\n")
                print(f'Total Strokes for {player[list_value]} on Course {Course_num}: ')
                amount_of_strokes = int(input())
                player.append(amount_of_strokes)
            print('----------------')   
            print(players)
            input()
            Course_num +=1
            clear_screen()
            title_screen()
   elif round == 9:
        Course_num = 1
        list_value = 0
        while Course_num < 10:
            Course_par = input(f'What is Par for Course {Course_num}: ')
            for player in players:
                print("\n")
                print(f'Total Strokes for {player[list_value]} on Course {Course_num}: ')
                amount_of_strokes = int(input())
                player.append(amount_of_strokes)
            print('----------------')   
            print(players)
            input()
            Course_num +=1
            clear_screen()
            title_screen()


            
    
def main():
    title_screen()
    input(f'press any key to continue\n')
    get_player_names()
    clear_screen()
    title_screen()
    rounds = int(input('How many rounds will be played? (3,6,9 or 12): '))
    progress_bar()
    clear_screen()
    title_screen()
    game_start(rounds)
    input('')
    


if __name__ == '__main__':
    main()


