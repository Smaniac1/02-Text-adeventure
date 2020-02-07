#!/usr/bin/env python3
import sys, os, json
import random
# Check to make sure we are running the correct version of Python
assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

# The game and item description files (in the same folder as this script)
game_file = 'game.json'


# Load the contents of the files into the game and items dictionaries. You can largely ignore this
# Sorry it's messy, I'm trying to account for any potential craziness with the file location
def load_files():
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, game_file)) as json_file: game = json.load(json_file)
        return game
    except:
        print("There was a problem reading either the game or item file.")
        os._exit(1) 
score = {
    "Happiness": 50,
    "Unrest": 50,
    "Economy": 50,
    "Corruption": 50
    }
def render(game,current):
    c = game[current]
    print("\n\nHappiness:", score["Happiness"])
    print("Unrest:", score["Unrest"])
    print("Economy:", score["Economy"])
    print("Corruption:",score["Corruption"])
    print(c["name"])
    print(c["desc"])
    if len(c["exits"]):
        print("\nChoose: ")
        for p in range(len(c["exits"])):
            print("{}. {}".format(p+1, c["exits"][p]["exit"]))

def get_input():
    response = input("\nMake a choice: ")
    response = response.upper().strip()
    return response

def update(game,current,response):
    c = game[current]
    if response.isdigit():
        try:
            p = int(response) - 1
            score["Happiness"] += c["exits"][p]["happiness"]
            score["Unrest"] += c["exits"][p]["unrest"]
            score["Economy"] += c["exits"][p]["economy"]
            score["Corruption"] += c["exits"][p]["corruption"]
            return c["exits"][p]["target"]
        except:
            return current
    return current
    

# The main function for the game
def main():
    current = "INTRO"  # The starting location
    end_game = ['END']  # Any of the end-game locations

    game = load_files()

    while True:
        if score["Happiness"] <= 0:
            print("Your people are unhappy. They won't rise up but instead leave peacefully in search of a new happier life.")
            print("Your final scores were:")
            print("Happiness:", score["Happiness"])
            print("Unrest:", score["Unrest"])
            print("Economy:", score["Economy"])
            print("Corruption:",score["Corruption"])
            break
        elif score["Unrest"] >= 100:
            print("Your people have had enough. You get thrown out of power and goes back into chaos.")
            print("Your final scores were:")
            print("Happiness:", score["Happiness"])
            print("Unrest:", score["Unrest"])
            print("Economy:", score["Economy"])
            print("Corruption:",score["Corruption"])      
            break
        elif score["Economy"] <= 0:
            print("Your people are to poor. While they might like living in your country, they leave in mass in search of a place were they can make a living and not starve.")
            print("Your final scores were:")
            print("Happiness:", score["Happiness"])
            print("Unrest:", score["Unrest"])
            print("Economy:", score["Economy"])
            print("Corruption:",score["Corruption"])
            break
        elif score["Corruption"] >= 100:
            print("You let corruption grow right under your nose, with so much corruption you are thrown out of power and a new, worse goverment takes power.")
            print("Your final scores were:")
            print("Happiness:", score["Happiness"])
            print("Unrest:", score["Unrest"])
            print("Economy:", score["Economy"])
            print("Corruption:",score["Corruption"])
            break
        else:
            render(game,current)
            if current in end_game:
                print("You've made your decisions!")
                print("Your stats ended up looking like this:")
                print("Happiness:", score["Happiness"])
                print("Unrest:", score["Unrest"])
                print("Economy:", score["Economy"])
                print("Corruption:",score["Corruption"])
                total_score = score["Happiness"] + score["Unrest"] + score["Economy"] + score["Corruption"]
                if total_score > 350:
                    print("Through your efforts you have made a near perfect nation and your people have high hopes for the future")
                    print("AMAZING VICTORY")
                elif total_score > 300:
                    print("Through your efforts you have made a great nation and your people believe things will only get better from here")
                    print("GREAT VICTORY")
                elif total_score > 250:
                    print("Through your efforts you have made an good nation but, your people don't fully believe that the nation will become the best")
                    print("GOOD VICTORY")
                elif total_score > 200:
                    print("Through your efforts you have barely squeezed out a nation and your people don't believe you will make it better, but it's better than what was happening before.")
                    print("MINOR VICTORY")
                else:
                    print("Despite your efforts your people aren't happy and eventually your are removed from power.")
                    print("YOU LOSE")
                break #break out of the while loop

        response = get_input()

        if response == "QUIT" or response == "Q":
            break #break out of the while loop

        current = update(game,current,response)

    print("\nThanks for playing!")

# run the main function
if __name__ == '__main__':
	main()