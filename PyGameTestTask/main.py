from pyunity.pyunity import *
from scenes import *

import config
import database


#config.player_name = input("Введите ваше имя: ")
config.player_name = "player_test_1231"

database.try_create()

#init game
PyUnity.create_display((800, 600), "TestTask", (39, 3, 58));

#start game
PyUnity.start_main_loop(create_main_scene())


