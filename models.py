import arcade
class Ship:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
 
    def update(self, delta):
        if self.y > self.world.height:
            self.y = 0
        self.y += 5

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ship = Ship(self,100, 100)
  
    def update(self, delta):
        self.ship.update(delta)
        
class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()
