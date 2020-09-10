#Text based Rpg
#By KamiDomi

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

#Player 1#
class player:
      def __init__ (self):
          self.name = ""
          self.hp = 0
          self.mp = 0
          self.status_effects = []
          self.location = ""
player1 = player()

#Title Screen#
def title_screen_selections():
    option =input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ("play", "help", "quit"):
        print("please enter a vailed command")
        option = input("> ")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system("clear")
    print("########################################")
    print("# Welcome To This fun and exciting rpg #")
    print("########################################")
    print("               -play-                   ")
    print("               -help-                   ")
    print("               -quit-                   ")
    title_screen_selections()

def help_menu():
    print("########################################")
    print("######### How can i help you? #########")
    print("########################################")
    print("               -play-                   ")
    print("               -help-                   ")
    print("               -quit-                   ")
    title_screen_selections()

def start_game():
