########################################
# Name: Jacob Rosales
# Collaborators (if any):
# GenAI Transcript (if any):
# Estimated time spent (hr):
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.

    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        gw.show_message("You need to implement this method")

        if word_to_row in ENGLISH_WORDS:  
            gw.show_message("confirmed")
        else:
            gw.show_message("not in word list")

        
    def word_to_row(row:int, word:str):
        gw.show_message("words")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    gw.set_square_letter(0,0,'q')
    gw.set_square_letter(0,1,'u')
    gw.set_square_letter(0,2,'a')
    gw.set_square_letter(0,3,'k')
    gw.set_square_letter(0,4,'e')
    

    




# Startup boilerplate
if __name__ == "__main__":
    wordle()
