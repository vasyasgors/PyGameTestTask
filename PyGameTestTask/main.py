from pyunity.pyunity import *
from scenes import *

import config
import database


config.player_name = input("Введите ваше имя: ")

database.init()

PyUnity.create_display((800, 600), "TestTask", (39, 3, 58));
PyUnity.start_main_loop(create_main_scene())


