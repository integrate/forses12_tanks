import time
import wrap
from wrap import sprite

wrap.world.create_world(800, 650, )
wrap.world.set_back_color(15, 173, 255)

ok=wrap.sprite.add_text('ИГРАТЬ',400,325 , text_color=[0, 0, 0], font_size=80)

#var





@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def button (pos_x,pos_y):
    if sprite.is_collide_point(ok,pos_x,pos_y,True):
        import tanks



#@wrap.on_mouse_move()
#def button (pos_x,pos_y):
    #wrap.world.create_world(pos_x+50,pos_y+50)


import wrap_py
wrap_py.app.start()
