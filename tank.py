import wrap, time
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


def move_tank(name, name_speed, animation, animation2):
    sprite.move_at_angle_dir(name, name_speed)
    a = sprite.get_costume(name)
    if a == animation:
        wrap.sprite.set_costume(name, animation2)
    else:
        wrap.sprite.set_costume(name, animation)


def boom(name):
    x, y = sprite.get_pos(name)
    sprite.remove(name)
    z1 = sprite.add("battle_city_items", x, y, 'effect_explosion_big1')
    time.sleep(0.3)
    sprite.set_costume(z1, 'effect_explosion_big2')
    time.sleep(0.3)
    sprite.set_costume(z1,  'effect_explosion1')
    time.sleep(0.3)
    sprite.set_costume(z1, 'effect_explosion2')
    time.sleep(0.3)
    sprite.set_costume(z1, 'effect_explosion3')
    time.sleep(0.3)
    sprite.remove(z1)


def blok(name, brick):
    g = sprite.is_collide_sprite(name, brick)
    xn, yn = sprite.get_pos(name)

    if g:
        if xn < sprite.get_left(brick) or xn > sprite.get_right(brick):
            sprite.set_reverse_x(name, not sprite.get_reverse_x(name))
        else:
            sprite.set_reverse_y(name, not sprite.get_reverse_y(name))
        # sprite.set_angle(name, sprite.get_angle(name)+180)

        sprite.move_at_angle_dir(name, 10)


def tank_tank(name1, name2):
    g = sprite.is_collide_sprite(name1, name2)
    if g:
        boom(name1)
        boom(name2)


def nop(name):
    x,y=sprite.get_pos(name)
    d=sprite.get_angle(name)
    if x<=0 or x>=800 or y<=0 or y>=653:
        sprite.set_angle(name,d+180)
