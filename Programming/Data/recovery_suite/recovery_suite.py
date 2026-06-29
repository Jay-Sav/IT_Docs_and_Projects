from get_time import get_current_time
from clear_screen import clear_screen
from loading_screen import progress_bar
from title_screen import print_title
from dash_line import print_dash_line

#Gather User Weight

def get_user_weight():
    try:
        weight = float(input(r"Enter your weight in pounds(lbs): ").strip())
        return weight
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_user_weight()


#Present and return Training Options
def list_training_options():
    training_options= {
        "1": "Resistance Training",
        "2": "High-Intensity Interval Training (HIIT)",
        "3": "Endurance Training",
        "4": "Hybrid Training",
        "5": "Active Recovery"
}
    return training_options

#Present and return Sub-Options based on Training Option Selected
def get_training_sub_option(training_option_selected):
    print(f"\nWhat kind of {training_option_selected} did you do?")
    if training_option_selected == "Resistance Training":
        sub_options = {
            "1": "Hypertrophy (Muscle Growth) (8-12 reps)",
            "2": "Strength Training (1-6 reps)",
            "3": "Power Training (1-5 reps with explosive movements)"
        }
        for counter, option in enumerate(sub_options.values(), 1):
            print(f"{counter}: {option}")
        sub_option_selected = input("\nSelect the type of resistance training you performed (Enter the corresponding number): ").strip()
        while sub_option_selected not in sub_options:
            print("Invalid input. Please enter a valid number corresponding to the resistance training type.")
            sub_option_selected = input("Select the type of resistance training you performed (Enter the corresponding number): ").strip()
        return sub_options[sub_option_selected]
    
    elif training_option_selected == "High-Intensity Interval Training (HIIT)":
        sub_options = {
            "1": "Short Intervals (20-30 seconds work, 10-15 seconds rest)",
            "2": "Long Intervals (1-4 minutes work, equal rest)",
            "3": "Tabata (20 seconds work, 10 seconds rest for 4 minutes)"
        }
        print("\nSelect the type of HIIT you performed:")
        for counter, option in enumerate(sub_options.values(), 1):
            print(f"{counter}: {option}")
        sub_option_selected = input("\nSelect the type of HIIT you performed (Enter the corresponding number): ").strip()
        while sub_option_selected not in sub_options:
            print("Invalid input. Please enter a valid number corresponding to the HIIT type.")
            sub_option_selected = input("\nSelect the type of HIIT you performed (Enter the corresponding number): ").strip()
        return sub_options[sub_option_selected]
    
    elif training_option_selected == "Endurance Training":
        sub_options = {
            "1": "Long Slow Distance (LSD) (steady pace for 60+ minutes)",
            "2": "Tempo Runs (comfortably hard pace for 20-40 minutes)",
            "3": "Moderate Intensity Steady State (MISS) (jogging or cycling at a steady pace)"
        }
        print("\nSelect the type of Endurance Training you performed:")
        for counter, option in enumerate(sub_options.values(), 1):
            print(f"{counter}: {option}")
        sub_option_selected = input("\nSelect the type of endurance training you performed (Enter the corresponding number): ").strip()
        while sub_option_selected not in sub_options:
            print("Invalid input. Please enter a valid number corresponding to the endurance training type.")
            sub_option_selected = input("\nSelect the type of endurance training you performed (Enter the corresponding number): ").strip()
        return sub_options[sub_option_selected]
    
    elif training_option_selected == "Hybrid Training":
        sub_options = {
            "1": "CrossFit (varied functional movements performed at high intensity)",
            "2": "Circuit Training (series of exercises performed in sequence with minimal rest)",
            "3": "Mixed Modal Training (combination of strength, endurance, and cardio exercises)"
        }
        print("\nSelect the type of Hybrid Training you performed:")
        for counter, option in enumerate(sub_options.values(), 1):
            print(f"{counter}: {option}")
        sub_option_selected = input("\nSelect the type of hybrid training you performed (Enter the corresponding number): ").strip()
        while sub_option_selected not in sub_options:
            print("Invalid input. Please enter a valid number corresponding to the hybrid training type.")
            sub_option_selected = input("\nSelect the type of hybrid training you performed (Enter the corresponding number): ").strip()
        return sub_options[sub_option_selected]
    
    elif training_option_selected == "Active Recovery":
        sub_options = {
            "1": "Yoga (gentle stretching and breathing exercises)",
            "2": "Light Walking (easy pace for 20-30 minutes)",
            "3": "Foam Rolling (self-myofascial release to improve mobility)"
        }
        print("\nSelect the type of Active Recovery you performed:")
        for counter, option in enumerate(sub_options.values(), 1):
            print(f"{counter}: {option}")
        sub_option_selected = input("\nSelect the type of active recovery you performed (Enter the corresponding number): ").strip()
        while sub_option_selected not in sub_options:
            print("Invalid input. Please enter a valid number corresponding to the active recovery type.")
            sub_option_selected = input("Select the type of active recovery you performed (Enter the corresponding number): ").strip()
        return sub_options[sub_option_selected]

#Print Training Options
def print_training_options(training_options):
    for counter,option in enumerate(training_options.values(), 1):
        print(f"{counter}:{option}")

#Get Training Duration
def get_training_duration():
    try:
        duration = float(input("\nEnter the duration of your training session in minutes: ").strip())
        return duration
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_training_duration()




#Main 
if __name__ == "__main__":

#Screen 1 - Title Screen and Loading Screen
    print_title()
    progress_bar(1)
    clear_screen()

#Screen 2 - Title Screen and Time 
    print_title()
    print_dash_line()
    print("\n")
    current_time = get_current_time()
    continue_prompt = input("\nPress [ENTER] to continue...")
    clear_screen()
    print_title()
    print(f"Current date and time: {current_time}\n")

#Screen 3 - Gather User Weight, Training Option, Sub-Option, and Duration
    weight = get_user_weight()    
    print(f"\nYour weight is: {weight} lbs\n")
    print_dash_line()
    options_data = list_training_options()
    print_training_options(options_data)
    training_option_selected = input("\nHow did you you train today (Enter the corresponding number): ").strip()
    ###Validate user input for training option selection
    while training_option_selected not in options_data:
        print("Invalid input. Please enter a valid number corresponding to the training option.")
        training_option_selected = input("How did you you train today (Enter the corresponding number): \n").strip()
    ############################
    chosen_sub_option = get_training_sub_option(options_data[training_option_selected])
    print(f"\nYou selected: {options_data[training_option_selected]} - {chosen_sub_option}")
    print_dash_line()
    training_duration = get_training_duration()
    print(f"\nYour training duration was: {training_duration} minutes")
    input("\nSession complete. Press [ENTER] to close this window...")
  




#print(weight)
#print(current_utc_time)

