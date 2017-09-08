import arcade
import arcade.key
class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0
class Ship(Model):
    DIR_HORIZONTAL = 0
    DIR_VERTICAL = 1
 
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
 
        self.direction = Ship.DIR_VERTICAL
        self.world = world
        self.x = x
        self.y = y
        self.direction = Ship.DIR_VERTICAL
        self.angle = 0
 
    def switch_direction(self):
        if self.direction == Ship.DIR_HORIZONTAL:
            self.direction = Ship.DIR_VERTICAL
            self.angle = 0
        else:
            self.direction = Ship.DIR_HORIZONTAL
            self.angle = -90
 
    def update(self, delta):
        if self.direction == Ship.DIR_VERTICAL:
            if self.y > self.world.height:
                self.y = 0
            self.y += 5
        else:
            if self.x > self.world.width:
                self.x = 0
            self.x += 5
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ship = Ship(self,100, 100)
        self.gold = Gold(self, 400, 400)
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
    def update(self, delta):
        self.ship.update(delta)
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.ship.switch_direction()

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            self.angle = self.model.angle
    def draw(self):
        self.sync_with_model()
        super().draw()
class Gold:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

class Gold(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)