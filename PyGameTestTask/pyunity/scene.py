class Scene:
    def __init__(self, objects):
         self.objects = objects 
       
    def update(self):
        for i in range(len(self.objects)):
            if self.objects[i].behaviour != None:
                self.objects[i].behaviour.update()

            for j in range(len(self.objects)):
                if self.objects[i].rect.colliderect(self.objects[j].rect) == True:
                    self.objects[i].behaviour.on_collied(self.objects[j])
                    self.objects[j].behaviour.on_collied(self.objects[j])

    def render(self, display):
         for object in self.objects:
            if object.renderer != None:
                object.renderer.render(display)

    def add_object(self, object):
        self.objects.append(object)

        if object.behaviour != None:
            object.behaviour.start()

    def remove_object(self, object):
        self.objects.remove(object)
        if object.behaviour != None:
            object.behaviour.on_destroy()



