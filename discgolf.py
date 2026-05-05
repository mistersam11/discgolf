import random
import os
import string
import re

# Hole library
class Hole1():
    def __init__(self):
        self.length = 412
        self.par = 3

class Hole2():
    def __init__(self):
        self.length = 251
        self.par = 3

class Hole3():
    def __init__(self):
        self.length = 512
        self.par = 4

class Hole4():
    def __init__(self):
        self.length = 310
        self.par = 3

class Hole5():
    def __init__(self):
        self.length = 950
        self.par = 5

class Hole6():
    def __init__(self):
        self.length = 230
        self.par = 3

class Hole7():
    def __init__(self):
        self.length = 750
        self.par = 4

class Hole8():
    def __init__(self):
        self.length = 460
        self.par = 4

class Hole9():
    def __init__(self):
        self.length = 1000
        self.par = 5
    

# Disc library with accuracy and distance values for each disc type and throw type
class Driver:
    def __init__(self, throw_type):
        if throw_type == "backhand":
            self.accuracy = 60
            self.distance = 375
        elif throw_type == "forehand":
            self.accuracy = 80
            self.distance = 325
        else:
            self.accuracy = 100
            self.distance = 50

class Midrange:
    def __init__(self, throw_type):
        if throw_type == "backhand":
            self.accuracy = 85
            self.distance = 275
        elif throw_type == "forehand":
            self.accuracy = 90
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

# Parser function to extract throw type and disc type from user input
def parse_text(player_input: str):
    """Parse the input and return (throw_type, disc_type) or (None, None)."""
    throw_types = ['backhand', 'forehand', 'putt']
    disc_types = ['driver', 'midrange', 'putter']
    unwanted_words = ['a', 'the', 'an', 'at', 'to', 'with', 'throw', 'want', 'i']
    exit_words = ['quit','exit','q','stop']

    if player_input in exit_words: return "exit", "exit"

    # Normalize input
    normal_text = player_input.lower()
    translator = str.maketrans('', '', string.punctuation)
    normal_text = normal_text.translate(translator)
    split_text = normal_text.split()

    # Filter out filler words
    filtered_list = [word for word in split_text if word not in unwanted_words]

    if len(filtered_list) > 1 and filtered_list[0] in throw_types and filtered_list[1] in disc_types:
        return filtered_list[0], filtered_list[1]

    return None, None

# Get the accuracy for a regular shot
def shot_accuracy_check(throw_type, disc_type, current_zone):
    if disc_type == "driver":
        disc = Driver(throw_type)
    elif disc_type == "midrange":
        disc = Midrange(throw_type)
    else:
        disc = Putter(throw_type)

    # Adjust accuracy based on current zone
    if current_zone == "fairway":
        accuracy = disc.accuracy
    elif current_zone == "rough_shallow":
        accuracy = disc.accuracy - 20
    elif current_zone == "rough_deep":
        accuracy = disc.accuracy - 30
    else:  # hazard
        accuracy = disc.accuracy - 20

    # Simulate the throw and determine if it's accurate
    roll = random.randint(1, 100)
    return roll <= accuracy


# Returns throw_distance and potential_zone (either one of the roughs or None) and is_accurate
def get_shot_distance(throw_type, disc_type, current_zone, is_accurate):
    if disc_type == "driver":
        disc = Driver(throw_type)
    elif disc_type == "midrange":
        disc = Midrange(throw_type)
    else:
        disc = Putter(throw_type)

    if is_accurate:
        return int(disc.distance + ((random.random() + 0.1) * 50)), None
    else:
        if random.random() > 0.5:
            return int((disc.distance + ((random.random() + 0.1) * 50)) / 2), None
        else:
            if random.random() > 0.5:
                return int((disc.distance + ((random.random() + 0.1) * 50)) / 4), "rough_shallow"
            else:
                return int((disc.distance + ((random.random() + 0.1) * 50)) / 8), "rough_deep"

# Calculate putt accuracy (used when in circle 1 or 2). Returns True or False
def putt_accuracy_check(current_zone):
    if current_zone == "circle2":
        return random.random() <= 0.4
    else:
        return random.random() <= 0.89
        
# Calculate putt distance (used when in circle 1 or 2 and putt is inaccurate). Returns the updated current_distance and a past_basket variable to use for messages
def get_putt_distance(current_distance):
    updated_distance = int(current_distance * random.uniform(0.1, 1.0))
    if updated_distance <= 5:
        return updated_distance, False
    else:
        return updated_distance, True
    
# Determine the new current zone based on the shot results ()
def get_next_zone(current_distance, potential_zone):
    if potential_zone == None:
        if current_distance <= 30:
            return "circle1"
        elif current_distance <= 60:
            return "circle2"
        else:
            return "fairway"
    else: return potential_zone

def set_this_hole(current_hole):
    match current_hole:
        case 1: return Hole1()
        case 2: return Hole2()
        case 3: return Hole3()
        case 4: return Hole4()
        case 5: return Hole5()
        case 6: return Hole6()
        case 7: return Hole7()
        case 8: return Hole8()
        case 9: return Hole9()

# Little function to calculate the score to add to the running score
def get_score(strokes, par):
    return strokes - par

def output_results(throw_type, disc_type, current_distance, current_zone, is_accurate, made_basket, odd_choice, past_basket, strokes):
    print()

# Declare wide-scope variables to be updated through game loop
current_hole = 1
this_hole = Hole1() 
current_par = this_hole.par
current_distance = this_hole.length
current_zone = None
is_accurate = None
odd_choice = False
past_basket = False
hole_start = True
strokes = 0
score = 0

while True:

    if hole_start:
        print(f"Hole: {current_hole}, Par: {current_par}, Distance: {current_distance} feet.")
        print(f"Current score: {score}")
        hole_start = False
        odd_choice = False
        strokes = 0
        current_zone = "fairway"


    text1, text2 = parse_text(input("> "))
    if text1 == "exit":
        break
    else:
        throw_type, disc_type = text1, text2

    strokes += 1

    if current_zone not in ("circle1", "circle2"):
            
        #Get accuracy
        is_accurate = shot_accuracy_check(throw_type, disc_type, current_zone)

        #Calculate the shot distance
        throw_distance, potential_zone = get_shot_distance(throw_type, disc_type, current_zone, is_accurate)
        current_distance -= throw_distance
        if current_distance < 0:
            current_distance *= -1
            past_basket = True
        else:
            past_basket = False
        
        #Calculate the next zone
        current_zone = get_next_zone(current_distance, potential_zone)

        #Set leftover variables necessary for output
        odd_choice = False
        made_basket = False

        #Output
        output_results(throw_type, disc_type, current_distance, current_zone, is_accurate, made_basket, odd_choice, past_basket, strokes)
        
    else:
        if throw_type == "putt":
            disc_type = "putter"
            made_basket = putt_accuracy_check(current_zone)
            if made_basket:
                current_hole += 1
                score += get_score(strokes, this_hole.par)
                this_hole = set_this_hole(current_hole)
                current_distance = this_hole.length
                current_par = this_hole.par
                hole_start = True
                current_zone = "fairway" 
                output_results(throw_type, disc_type, current_distance, current_zone, is_accurate, made_basket, odd_choice, past_basket, strokes)
            else:
                current_distance, past_basket = get_putt_distance(current_distance)
                is_accurate = False
                output_results(throw_type, disc_type, current_distance, current_zone, is_accurate, made_basket, odd_choice, past_basket, strokes)
        else:
            # Throw a regular shot, but include the odd choice message in output
            odd_choice = True

            #Get accuracy
            is_accurate = shot_accuracy_check(throw_type, disc_type, current_zone)

            #Calculate the shot distance
            throw_distance, potential_zone = get_shot_distance(throw_type, disc_type, current_zone, is_accurate)
            current_distance -= throw_distance
            if current_distance < 0:
                current_distance *= -1
                past_basket = True
            else:
                past_basket = False
        
            #Calculate the next zone
            current_zone = get_next_zone(current_distance, potential_zone)

            # Leftover variables
            made_basket = False
            
            #Print results
            output_results(throw_type, disc_type, current_distance, current_zone, is_accurate, made_basket, odd_choice, past_basket, strokes)
