class Vector4:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GameObject:
     def __init__(self, behaviour = None, renderer = None, tag = "Untagged"):
        self.tag = tag
        self.rect = None
        self.behaviour = behaviour
        self.renderer = renderer
        
        if self.behaviour != None:
            self.behaviour.game_object = self

        if self.renderer != None:
            self.rect = self.renderer.get_rect(); 

