import wrap
from wrap import sprite
import tank


def add_brick (spisok,set_x,set_y):

    brick = sprite.add('battle_city_items', set_x,set_y, 'block_brick')
    spisok.append(brick)

def bbrick (spisok,set_x,set_y):

    add_brick(spisok,set_x*32+16,set_y*32+16)


def ctaf_cteny_vertikil (spisok, x, ys, yf, ):
    for f in range(ys,yf+1):
        bbrick(spisok, x, f)

def ctaf_cteny_gorizont (spisok,y,xs,xf,):
    for f in range(xs,xf+1):
        bbrick(spisok, f, y)
