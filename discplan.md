# Abstract

A text-based game (interactive novel) in which the player must complete a disc golf course in the fewest throws possible. The game is controlled via text (ex. "Throw a backhand with a destroyer"). Each shot is calculated based on the distance to the basket/out-of-bounds, the disc selected, and a random dose of accuracy which can influence the result. 

# Pseudocode

## Text Parsing
*The main mechanic of the game is entering text prompts. They should be interpreted as follows: Type of Shot | Type of Disc. Some examples would be "Throw a backhand with the destroyer" or "Putt with the aviar". Verbs like "Throw" can be ignored, since that's what the action will always be. Articles like "the" or "a" can be ignored safely as well. Prepositions like "with" should be ignored, at least for now, as the Type of Shot will always be thrown with the Type of Disc. There is potential for later implementation of prepositions, allowing for shots that go "to the left" or "above" obstacles.*

DEFINE a class for parsed text/commands. 
    Initialize the class with
        list of actions/types of throws
        list of discs
    normalize the text
        make lowercase and remove punctuation
        tokenize (turn the sentence into a list of words)
    remove articles and prepositions from the list
    return the list with the Type of Shot and Type of Disc

## Hole Layouts and Disc Positions
*The basic idea is that each hole has a certain distance and shape, and maybe some obstacles. The hole will act like the player is free to land wherever, but in reality, each shot will place the player in a "room", like how you can navigate in Zork or Planetfall. The distance can still vary, even if you end up in the same room each time, and that will impact the accuracy (and success) of the next shot. So each hole is a series of rooms, and each room has a unique description and potential challenges, that should influence the player's next choice. 
Room object concept:
    rough_left_deep:
        Description: "Your disc lands in the deep, dark bushes to the left of the fairway. There is not much to do besid        es pitch out to the fairway."
        Type: rough
        Possible next zones: fairway_200, fairway_100, circle2, rough_left_deep, rough_left_shallow
Hole object concept:
    Hole 1:
        Description: "Hole 1: 325 feet. Par 3. A challenging shot through the woods with a narrow fairway and thick roug        h on both sides.
        Distance to basket: 325 feet.
        Zones: fairway_200, fairway_100, circle2, circle1, rough_left_shallow, rough_left_deep, rough_right_shallow, rou        gh_right_deep

DEFINE a variable that stores the player's current hole.
DEFINE a variable that stores the player's current zone.
DEFINE a variable that stores the player's current distance from the basket.

## Mechanic for throwing
*When the player throws, first calculate the potential distance of the shot (backhand driver, midrange, putter etc. all have separate base distance, plus/minus a random range. Calculate if it stays on the fairway, with a random accuracy multiplied by the accuracy of backhand driver, midrange, putter etc.. Then, determine which zone it will land in, based on the distance and accuracy, and which zones are available. Print the zone's description, as well as the new distance to the basket, and the current shot.

