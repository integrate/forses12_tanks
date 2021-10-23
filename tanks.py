import wrap
from wrap import sprite

wrap.world.create_world(800, 650)

tank1 = sprite.add('battle_city_tanks', 400, 300, 'tank_player_size1_green1')
tank2 = sprite.add('battle_city_tanks', 300, 400, 'tank_enemy_size1_white1')

# tank1
tank1_speed = 5
tank1_angle = 4
# tank2
tank2_speed = 5
tank2_angle = 3


@wrap.on_key_always(wrap.K_w)
def game_play_w():
    sprite.move_at_angle_dir(tank1, tank1_speed)


@wrap.on_key_always(wrap.K_a)
def game_play_w():
    z = sprite.get_angle(tank1)
    sprite.set_angle(tank1, z - tank1_angle)


@wrap.on_key_always(wrap.K_d)
def game_play_d():
    z = sprite.get_angle(tank1)
    sprite.set_angle(tank1, z + tank1_angle)


@wrap.on_key_always(wrap.K_UP)
def game_play_up():
    sprite.move_at_angle_dir(tank2, tank2_speed)


@wrap.on_key_always(wrap.K_LEFT)
def game_play_left():
    z = sprite.get_angle(tank2)
    sprite.set_angle(tank2, z - tank2_angle)


@wrap.on_key_always(wrap.K_RIGHT)
def game_play_right():
    z = sprite.get_angle(tank2)
    sprite.set_angle(tank2, z + tank2_angle)


@wrap.on_key_down(wrap.K_s)
def game_play_shot():
    z = sprite.get_angle(tank1)
    x, y = sprite.get_pos(tank1)
    bullet = sprite.add('battle_city_items', x, y,'bullet')
    sprite.set_angle(bullet,z)
    sprite.move_at_angle_dir(bullet,22)
