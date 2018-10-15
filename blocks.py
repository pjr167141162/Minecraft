#BEDROCK is the only block to not be loaded from here.
#any blocks loaded here are placeable, and removeable by the player.

def get_blocks():
    #top,bottom,sides.
    TNT = tex_coords((5, 0), (6, 0), (4, 0))
    GRASS = tex_coords((1, 0), (0, 1), (0, 0))
    SAND = tex_coords((1, 1), (1, 1), (1, 1))
    BRICK = tex_coords((2, 0), (2, 0), (2, 0))
    STONE_BRICK = tex_coords((2, 1), (2, 1), (2, 1))
    PLANK = tex_coords((3, 0), (3, 0), (3, 0))
    COBBLE = tex_coords((3, 1), (3, 1), (3, 1))
    DIRT = tex_coords((0, 1), (0, 1), (0, 1))
    WOOD = tex_coords((0, 3), (0, 3), (0, 2))
    LEAF = tex_coords((1, 2), (1, 2), (1, 2))
    CACTUS = tex_coords((3, 2), (3, 2), (2, 2))
    MOSSY_STONE = tex_coords((1, 3), (1, 3), (1, 3))
    STONE = tex_coords((2, 3), (2, 3), (2, 3))
    INVENTORY = [BRICK, GRASS, SAND,STONE,PLANK,COBBLE,DIRT,WOOD,LEAF,CACTUS,MOSSY_STONE,STONE_BRICK,TNT]#all the blocks the player can place/remove in the world.
    INVENTORY_NAMES = ["BRICK","GRASS","SAND","STONE","PLANK","COBBLE","DIRT","WOOD","LEAF","CACTUS","MOSSY STONE","STONE BRICK","TNT"]#for use in block picker
    BLOCKS = {}
    for x in range(len(INVENTORY)):
        BLOCKS[INVENTORY_NAMES[x]]=INVENTORY[x]
    return INVENTORY,INVENTORY_NAMES,BLOCKS


def tex_coord(x, y, n=8):
    """ Return the bounding vertices of the texture square.
    """
    m = 1.0 / n
    dx = x * m
    dy = y * m
    return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m


def tex_coords(top, bottom, side):
    """ Return a list of the texture squares for the top, bottom and side.
    """
    top = tex_coord(*top)
    bottom = tex_coord(*bottom)
    side = tex_coord(*side)
    result = []
    result.extend(top)
    result.extend(bottom)
    result.extend(side * 4)
    return result
