import wrap
from wrap import sprite
import tank

def add_brick (spisok,set_x,set_y):
    brick = sprite.add('battle_city_items', set_x,set_y, 'block_brick')
    spisok.append(brick)