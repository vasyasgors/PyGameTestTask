from pyunity.pyunity import *
from scenes import *




#init game
PyUnity.create_display((800, 600), "TestTask", (39, 3, 58));

#start game
PyUnity.start_main_loop(create_main_scene())


