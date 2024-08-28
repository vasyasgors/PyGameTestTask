class Scene:
    def __init__(self, objects = []):
         self.objects = objects 
         self.object_to_destroy = []
         self.object_to_add = []
       
    def update(self):
        for object in self.object_to_destroy:
            if object in self.objects:
                self.objects.remove(object)

        for object in self.object_to_add:
             self.objects.append(object)

        self.object_to_add.clear()
        self.object_to_destroy.clear()


        for i in range(len(self.objects)):
            if self.objects[i].behaviour != None:
                if self.objects[i].behaviour.enabled == True:
                    self.objects[i].behaviour.update()
            
            # Check collision
            for j in range(len(self.objects)):
                if i == j:
                    continue

                if self.objects[i].rect == None or self.objects[j].rect == None:
                    continue

                if self.objects[i].rect.colliderect(self.objects[j].rect) == True:
                    self.objects[i].behaviour.on_collied(self.objects[j])
                    self.objects[j].behaviour.on_collied(self.objects[i])

    def render(self, display):
         for object in self.objects:
            if object.renderer != None:
                object.renderer.render(display)

    def add_object(self, object):
        self.object_to_add.append(object)

        if object.behaviour != None:
            object.behaviour.start()

    def remove_object(self, object):
        self.object_to_destroy.append(object)
        
        if object.behaviour != None:
            object.behaviour.on_destroy()



