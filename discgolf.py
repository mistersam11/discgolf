import re
import string
import random

# Create a parsing class that takes user input and compares it with a set of actions and discs -----------------
class Parser:
    def __init__(self, player_input):
        # Initialize the objects/variables
        self.throw_types = ['backhand','forehand','putt']
        self.disc_types = ['driver','midrange','putter']
        self.unwanted_words = ['a','the','an','at','to','with','throw']
        self.player_input = player_input
        self.normalized_input = self.normalize(player_input)

    def normalize(self, player_input):
        # Remove capitalization and punctuation
        normal_text = player_input.lower()
        translator = str.maketrans('', '', string.punctuation)
        normal_text = normal_text.translate(translator)
        
        # Convert string into a list of words
        split_text = normal_text.split()

        # Filter out all words but Type of Throw and Type of Disc
        filtered_list = [word for word in split_text if word not in self.unwanted_words]

        # If remaining words aren't in [0] throw_types and [1] disc_types, return false.
        if len(filtered_list) > 1:
            if filtered_list[0] in self.throw_types and filtered_list[1] in self.disc_types:
               return filtered_list
            else:
                return None
        else:
            return None

# Zone Dictionaries ---------------------------------------------------------------------------

class Circle1:
    def __init__(self, distance, disc_type, throw_type):
        self.desc = f"The {disc_type} glides through the air, landing gracefully inside circle one, {distance} away from the basket!"
        self.type = "fairway"
        self.range = 30

class Circle2:
    def __init__(self, distance, disc_type):
        self.desc = f"The {disc_type} glides through the air, landing gracefully inside circle two, {distance} feet away from the basket!"
        self.type = "fairway"
        self.range = 60

class Fairway:
    def __init__(self, distance, disc_type, throw_type):
        self.desc = f"With a snap of the wrist, the disc follows a gentle S-curve and finds center fairway, {distance} feet away from the basket!"
        self.type = "fairway"
        self.range = 1000

class RoughShallow:
    def __init__(self, distance, disc_type, throw_type):
        self.desc = f"What a bad shot selection! The {disc_type} kareens into a tree and flutters harmlessly down into a bush. Good look throwing from {distance} feet to the basket."
        self.type = "rough_shallow"
        self.range = 1000

class RoughDeep:
    def __init__(self, distance, disc_type, throw_type):
        self.desc = f"DISASTER! WEEEOOOOEEEEEOOOOOEEEEEOOOOOOOOO YOUR DISC IS GONE FOREVER GOSH DANG IT OH MAN GOSH DARNBETTER LUCK NEXT TIME YOU BOZO. {distance} FEET FROM THE BASKET!!!!!!!!"
        self.type = "rough_deep"
        self.range = 1000

# Exit Command List ---------------------------------------------------------------------
exit_phrases = ['q','quit','exit','stop']

#Disc classes ---------------------------------------------------------------------------
class Driver:
    def __init__(self, throw_type):
        if throw_type == "backhand":
            self.accuracy = 75
            self.distance = 400
        elif throw_type == "forehand":
            self.accuracy = 90
            self.distance = 325
        else:
            self.accuracy = 100
            self.distance = 50

class Midrange:
    def __init__(self, throw_type):
        if throw_type == "backhand":
            self.accuracy = 85
            self.distance = 300
        elif throw_type == "forehand":
            self.accuracy = 96
            self.distance = 230
        else:
            self.accuracy = 100
            self.distance = 45

class Putter:
    def __init__(self, throw_type):
        if throw_type == "backhand":
            self.accuracy = 95
            self.distance = 175
        elif throw_type == "forehand":
            self.accuracy = 95
            self.distance = 100
        else:
            self.accuracy = 100
            self.distance = 40

# Hole Dictionary -----------------------------------------------------------------------------------

class Hole1():
    def __init__(self):
        self.distance = 400

# Function to handle throws and next-zone placement -------------------------------------------------
def throw_shot(throw_type, disc_type, current_distance, current_zone):
    def shot_variance():
        random_number = random.random()
        if random_number > 0.5:
            return -1
        else:
            return 1
    
    # Declare variables
    random_number2 = random.random() + 0.1
    variance = shot_variance()
    thrown_disc = None   

    # Gather class data based on user input
    match disc_type: 
        case "driver":
            thrown_disc = Driver(throw_type)
        case "midrange":
            thrown_disc = Midrange(throw_type)
        case "putter":
            thrown_disc = Putter(throw_type)   
        case _:
            print("It sure wasn't a beaver in the pond...")

    # Calculate throw distance
    throw_distance = round(thrown_disc.distance + (
       thrown_disc.distance * 0.2 * random_number2 * variance
    ))

    # Apply accuracy penalty based on current zone
    penalty = 0
    if current_zone.type == "rough_shallow":
        penalty = 20
    elif current_zone.type == "rough_deep":
        penalty = 40
    else:
        penalty = 0


    # Shot accuracy check (returns True or False)
    def check_accuracy(accuracy_percent):
        return random.random() <= (accuracy_percent / (100 + penalty))
    
    # Calculate the new zone the player ends up in
    def get_zone(current_distance):
        if current_distance > 60:
            return Fairway(current_distance, disc_type, throw_type)
        elif current_distance > 30:
            return Circle2(current_distance, disc_type)
        else:
            return Circle1(current_distance, disc_type, throw_type)

    # Run the actual throw 
    if check_accuracy(thrown_disc.accuracy): 
        current_distance = current_distance - throw_distance
        current_zone = get_zone(current_distance) 
        print("Good throw!")
    else:
        print("Bad throw!")
        random_num = random.random()
        if random_num < 0.5:
            throw_distance = int(throw_distance * 0.5)
            current_distance = current_distance - throw_distance
            current_zone = get_zone(current_distance)
        else:
            random_num2 = random.random()
            if random_num2 < 0.5: 
                current_distance = current_distance - throw_distance
                current_zone = RoughShallow(current_distance, disc_type, throw_type)
            else: 
                current_distance = current_distance - throw_distance
                current_zone = RoughDeep(current_distance, disc_type, throw_type)

    print(f"You threw it {throw_distance} feet!")
    print(current_zone.desc)

    return current_distance, current_zone

# Define the current hole via class --------------------------------------------------------------
def init_hole(current_hole):
    match current_hole:
        case 1:
            return Hole1()
        case 2:
            return Hole2()
        case 3:
            return Hole3()
        case 4:
            return Hole4()
        case 5:
            return Hole5()
        case 6:
            return Hole6()
        case 7:
            return Hole7()
        case 8:
            return Hole8()
        case 9:
            return Hole9()

# Initalize the round --------------------------------------------------------------------------

hole_start = True
this_hole = None
current_hole = 1
current_distance = None
current_par = 3
current_throw = 1
current_zone = Fairway(None, None, None)

print("Welcome to BIG DISC GOLF GAME! To play, just type 'Throw a backhand with a driver', or 'Forehand a putter', etc. and see what happens!")

# Main loop -----------------------------------------------------------------------------------      
while True:
    
    #Initialize the current hole
    if hole_start:
        this_hole = init_hole(current_hole)
        current_distance = this_hole.distance
        print(f"HOLE {current_hole}. Par: {current_par}. Distance: {current_distance}.")
        hole_start = False

    # Process the parsed user command, execute the throw, and print the result
    user_cmd = input(">")
    cmd_output = Parser(user_cmd)
    if user_cmd in exit_phrases:
        break
    elif cmd_output.normalized_input is None:
        print("Make sure to include the throw type and disc name! Try again.")
    else:
        throw_type = cmd_output.normalized_input[0]
        disc_type = cmd_output.normalized_input[1]
        current_distance, current_zone = throw_shot(throw_type, disc_type, current_distance, current_zone)



