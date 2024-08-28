class GameObject:
     def __init__(self, behaviour = None, renderer = None, tag = "Untagged"):
        self.tag = "Untagged"
        self.rect = None
        self.behaviour = behaviour
        self.renderer = renderer
        
        if self.behaviour != None:
            self.behaviour.game_object = self

        if self.renderer != None:
            self.rect = renderer.get_rect(); 

