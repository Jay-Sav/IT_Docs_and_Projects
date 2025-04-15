#Import External Files
from Title_Screen import title_screen
from Clear_Screen import clear_screen
from Loading_Screen import progress_bar

# Variables and list for get_player_names
players = []
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
        while Course_num < 4:
            Course_par = input(f'What is Par for Course:{Course_num}:')
            Current_Stroke = 1
            for player in players:
                print(f'Course Par is: {Course_par}\n')
                input(f'Player {player} is up! {player} Stroke:{Current_Stroke}\n')
            Current_Stroke +=1
            Course_num +=1

            
    




def determine_golf_performance(par, strokes):
    if par-3 == strokes:
        return 'Albatross'
    elif par-2 == strokes:
        return 'Eagle'
    elif par-1 == strokes:
        return 'Birdie'
    elif par == strokes:
        return 'Par'
    elif par+1 == strokes:
        return 'Bogey'
    elif par+2 == strokes:
        return 'Double Bogey'
    elif par+3 == strokes:
        return 'Triple Bogey'
    else:    
        return '+' + str(strokes - par)
    
def iterate_through_holes():
    hole = 1 
    while hole <= 18:
        par = int(input("What par was the hole?\n"))
        strokes = int(input("How many strokes did you use:\n"))
        result = determine_golf_performance(par, strokes)
        print ("Hole", hole, "performance is", result)
        hole +=1

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


