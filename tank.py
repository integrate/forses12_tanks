import wrap
from wrap import sprite


def rotate(name, name_angle):
    z = sprite.get_angle(name)
    sprite.set_angle(name, z + name_angle)

def shot(name):
    z = sprite.get_angle(name)
    x, y = sprite.get_pos(name)
    bullet = sprite.add('battle_city_items', x, y, 'bullet')
    sprite.set_angle(bullet, z)
    sprite.move_at_angle_dir(bullet, 22)
    return bullet