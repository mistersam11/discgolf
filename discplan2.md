# The next iteration of the Disc Game (planning will be better)
- Parsing will be cleaner
- Game logic will be separate from display (output) logic
- That way, the output logic could be changed to something visual at some point

## Parsing
*Get a string from the player. Remove punctuation. Remove articles. Separate into list of remaining words. If the remaining words match the words in predefined lists of throws and disc types, the command is valid. If not, the command is invalid. If the command is valid, return the throw type and the disc type. If the command is invalid, return None and None.*


## Calculate Shot accuracy.
*Run with the throw type, the disc type, and the current zone. Each throw type and disc type will have its own accuracy. Then, the current zone will either do nothing (fairway) or have an accuracy penalty (rough). Calculate if the shot was a success with the logic: IF the throw/disc accuracy, divided by 100 + the penalty, is greater than a random number between 0 and 1, the throw is a success (return true). ELSE, it is a failure (return false) 

## Calculate shot distance.
*Run throw with the throw type, disc type, accuracy, and current zone (more on that later). All the throw does is calculate the potential distance of the shot. If the shot was a success (calculated earlier), the disc flies the full distance that it can, plus or minus a random small amount. "Flying" is just a simple calculation. Current distance = current distance - throw distance. If the shot was a failure, there are two potential outcomes. 1: the distance is cut in half. 2: the distance is cut in an eighth and the next zone is the rough. Return the current distance and zone (None if not the worst outcome)* If the updated current distance is negative, make it positive, and also return a "passed the basket" variable either true or false, to enable more custom messaging.

### Handing putting
If the current zone is circle 2 or circle 1, and the player throws a putt (not a backhand or forehand) DO NOT calculate the shot accuracy or shot distance. Instead, calculate the putt accuracy and putt distance.

### Calculate Putt Accuracy
From circle 2, there is a 40% chance of making the putt. From circle 1, there is a 89% chance of making a putt. Simple equation again: Circle2: If .4 > random number between 0 and 1, return True. Else, return False. Circle 1: If .89 > random number between 0 and 1, return True. Else, return False.

### Calculate Putt Distance
Return the current distance that's the current distance - the current distance +/- a random number between 1 and 20. If it's greater than 5, return a "passed the basket" variable either true. If it's less than five, return it false.

## Determine the next zone
*Run with the current distance and the next_zone (from shot distance). If the zone is None, determine the next zone based on the current distance. If the current distance falls within the range of a zone, return that zone. If the zone is something other than None, return whatever zone it is (probably needs a match case statement to match strings).

## Print out the results
This will be a pretty robust function. It should take throw type, disc type, current distance, current zone, odd choice, is accurate, and made basket and return a random line from the appropriate setof lines for that action/result. It can print out more than one line. So there can be a line that uses the throw type, disc type, current distance, and current zone. Therewill be a line that states whether or not it was accurate. There will be a line that only prints if it was an odd choice. There will be a line that only prints if the basket was made.


# Declare wide-scope variables so that the print function can access them at the end
throw type = None
disc type = None
current zone = None
current distance = None
made putt = False
is accurate = None
odd choice = False

# Main game loop

while True: (this is how python loops can be made)
    
    If it's the start of a hole:
        print the hole, par, and distance
        set hole start to false

    # Get the user input
    throw type, disc type = parse(input(">"))

    if the current zone is not circle 1 or circle 2:
        is_accurate = get accuracy(throw type, disc type, zone)
        current distance, potential zone, past the basket = throw_shot(throw type, disc type, is_accurate)
        current zone = next_zone(current distance, potential zone)
        odd_choice = False
    if it's circle 1 or 2:
        if throw type is putt:
            made_basket = putt accuracy(current_zone)
            if made_basket:
                add one to hole_number
                set current distance to the next hole's distance
                set start of hole to true
            else:
                current_distance, past the basket = throw putt(current_distance)
        else:
            run the exact same stuff as a non-circle throw. 
            odd choice = true

    print results





