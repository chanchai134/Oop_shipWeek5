import arcade
from models import World, Ship , ModelSprite
import arcade.key

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
 
class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)
        self.world = World(width, height)
        self.ship_sprite = ModelSprite('images/ship.png',model=self.world.ship)
        self.gold_sprite = ModelSprite('images/gold.png',model=self.world.gold)

    def on_draw(self):
        arcade.start_render()
        self.gold_sprite.draw()
        self.ship_sprite.draw()
        
    def update(self, delta):
        self.world.update(delta)
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
 
if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()