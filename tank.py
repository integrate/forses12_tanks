import wrap,time
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

def move_tank(name,name_speed,animation,animation2):
    sprite.move_at_angle_dir(name,name_speed)
    a = sprite.get_costume(name)
    if a==animation:
        wrap.sprite.set_costume(name,animation2)
    else:
        wrap.sprite.set_costume(name, animation)

def boom(name):
    x, y = sprite.get_pos(name)
    sprite.remove(name)
    z1 = sprite.add("battle_city_items", x, y, 'effect_explosion_big1')
    time.sleep(0.3)
    sprite.set_costume(z1, 'effect_explosion_big2')
    time.sleep(0.3)
    sprite.set_costume(z1, 'effect_explosion1')
    time.sleep(0.3)
    sprite.set_costume(z1, 'effect_explosion2')
    time.sleep(0.3)
    sprite.set_costume(z1, 'effect_explosion3')
    time.sleep(0.3)
    sprite.remove(z1)
