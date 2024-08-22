class Scene:
    def __init__(self, objects):
         self.objects = objects

    def update(self):
        for object in self.objects:
            object.update()

    def render(self, display):
        for object in self.objects:
            object.render(display)



