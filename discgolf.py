import random
import os
import string
import re

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
def get_shot_distance(throw_type, disc_type, current_zone):
    if disc_type == "driver":
        disc = Driver(throw_type)
    elif disc_type == "midrange":
        disc = Midrange(throw_type)
    else:
        disc = Putter(throw_type)

    if shot_accuracy_check(throw_type, disc_type, current_zone):
        return int(disc.distance + ((random.random() + 0.1) * 50)), None, True
    else:
        if random.random() > 0.5:
            return int((disc.distance + ((random.random() + 0.1) * 50)) / 2), None, False
        else:
            if random.random() > 0.5:
                return int((disc.distance + ((random.random() + 0.1) * 50)) / 4), "rough_shallow", False
            else:
                return int((disc.distance + ((random.random() + 0.1) * 50)) / 8), "rough_deep", False

# Calculate putt accuracy (used when in circle 1 or 2). Returns True or False
def putt_accuracy_check(current_zone):
    if current_zone == "circle2":
        return random.random() <= 0.4
    else:
        return random.random() <= 0.89
        
# Calculate putt distance (used when in circle 1 or 2 and putt is inaccurate). Returns the updated current_distance and a past_basket variable to use for messages
def get_putt_distance(current_distance):
    updated_distance = current_distance - current_distance + random.randint(1, 20)
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

# Declare wide-scope variables to be updated through game loop
throw_type = None
disc_type = None
current_hole = 1
current_par = 3
current_distance = 410
current_zone = None
made_putt = False
is_accurate = None
odd_choice = False
hole_start = True

while True:

    if hole_start:
        print(f"Hole: {current_hole}, Par: {current_par}, Distance: {current_distance} feet.")
        hole_start = False
        current_zone = "fairway"

    throw_type, disc_type = parse_text(input("> "))

    #Quitting the program if anything other than a correct command is entered (for now)
    if disc_type == None: break

    if current_zone != "circle1" or "circle2":
        throw_distance, potential_zone, is_accurate = get_shot_distance(throw_type, disc_type, current_zone)