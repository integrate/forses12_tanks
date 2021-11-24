import time

import wrap
from wrap import sprite
import tank

wrap.world.create_world(800, 650)

tank1 = sprite.add('battle_city_tanks', 400, 300, 'tank_player_size1_green1')
tank2 = sprite.add('battle_city_tanks', 300, 400, 'tank_enemy_size1_white1')

bullets = []

bullet2 = None
bullet = None

# tank1
tank1_speed = 4
tank1_angle = 4
fire_time = time.time() - 3
# tank2
tank2_speed = 5
tank2_angle = 3
fire_time2 = time.time() - 3


@wrap.on_key_always(wrap.K_w)
def game_play_w(keys):
    tank.move_tank(tank1, tank1_speed, 'tank_player_size1_green1', 'tank_player_size1_green2')


@wrap.on_key_always(wrap.K_a)
def game_play_w():
    tank.rotate(tank1, -tank1_angle)


@wrap.on_key_always(wrap.K_LEFT)
def game_play_w():
    tank.rotate(tank2, -tank2_angle)


@wrap.on_key_always(wrap.K_RIGHT)
def game_play_d():
    tank.rotate(tank2, tank2_angle)


@wrap.on_key_always(wrap.K_d)
def game_play_d():
    tank.rotate(tank1, tank1_angle)


@wrap.on_key_always(wrap.K_UP)
def game_play_up():
    tank.move_tank(tank2, tank2_speed, 'tank_enemy_size1_white1', 'tank_enemy_size1_white2')


@wrap.on_key_down(wrap.K_s)
def game_play_shot():
    global bullet
    global fire_time
    tim = time.time()
    yt = tim - fire_time
    if yt >= 3:
        bullet = tank.shot(tank1)
        bullets.append(bullet)
        print(bullets)
        fire_time = time.time()


@wrap.on_key_down(wrap.K_DOWN)
def game_play_shot():
    global fire_time2
    global bullet2
    tim = time.time()
    yt = tim - fire_time2
    if yt >= 3:
        bullet2 = tank.shot(tank2)
        bullets.append(bullet2)
        print(bullets)
        fire_time2 = time.time()


@wrap.always()
def game_play_shot():
    for b in bullets:
        sprite.move_at_angle_dir(b, 10)
        g = sprite.is_collide_sprite(tank1, b)
        f = sprite.is_collide_sprite(tank2, b)
        print(g)
        if g == True:
            sprite.remove(b)
            sprite.remove(b)
            tank.boom(tank1)
            wrap.sprite.add_text('ПОБЕДА БЕЛЫЕ', 299, 400, text_color=[255, 250, 250], font_size=80)

        if f == True:
            sprite.remove(b)
            sprite.remove(b)
            tank.boom(tank2)
            wrap.sprite.add_text('ПОБЕДА ЗЕЛЁНЫЕ', 299, 315, text_color=[0, 140, 49], font_size=80)
