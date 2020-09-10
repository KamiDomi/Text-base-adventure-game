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
player1 = player()

