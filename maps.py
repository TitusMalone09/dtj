import pygame

class Tile:
    def __init__(self, image):
        self.image = image

class Map:
    def __init__(self, map_data):
        self.map_data = map_data
        self.collision_rects = []
        self.tile_size = 32
        self.width = len(map_data[0]) * self.tile_size
        self.height = len(map_data) * self.tile_size
        self.load_collision_rects()

    def load_collision_rects(self):
        self.collision_rects = []
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                if tile in [b, c, d, e, f, h, i, j, k, l, m, n, o, p, q, r]:
                    self.collision_rects.append(pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))

    def draw(self, screen):
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                screen.blit(tile.image, (x * self.tile_size, y * self.tile_size))

a_image = pygame.image.load('graphics/map/a.png')
b_image = pygame.image.load('graphics/map/b.png')
c_image = pygame.image.load('graphics/map/c.png')
d_image = pygame.image.load('graphics/map/d.png')
e_image = pygame.image.load('graphics/map/e.png')
f_image = pygame.image.load('graphics/map/f.png')
h_image = pygame.image.load('graphics/map/h.png')
i_image = pygame.image.load('graphics/map/i.png')
j_image = pygame.image.load('graphics/map/j.png')
k_image = pygame.image.load('graphics/map/k.png')
l_image = pygame.image.load('graphics/map/l.png')
m_image = pygame.image.load('graphics/map/m.png')
n_image = pygame.image.load('graphics/map/n.png')
o_image = pygame.image.load('graphics/map/o.png')
p_image = pygame.image.load('graphics/map/p.png')
q_image = pygame.image.load('graphics/map/q.png')
r_image = pygame.image.load('graphics/map/r.png')

a = Tile(a_image)
b = Tile(b_image)
c = Tile(c_image)
d = Tile(d_image)
e = Tile(e_image)
f = Tile(f_image)
h = Tile(h_image)
i = Tile(i_image)
j = Tile(j_image)
k = Tile(k_image)
l = Tile(l_image)
m = Tile(m_image)
n = Tile(n_image)
o = Tile(o_image)
p = Tile(p_image)
q = Tile(q_image)
r = Tile(r_image)
                
map = Map([
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c]
])

# Blue
map0 = Map([
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, c, c],
    [c, j, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, k, c],
    [f, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, e],
    [j, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, k],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c]
])

map1 = Map([
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, c, c],
    [c, j, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, k, c],
    [f, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, e],
    [j, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, k],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, q, l, l, l, b, b, b, b, b],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, q, o, a, a, a, a, a, e, c, c, c, c],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c],
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c]
])

map2 = Map([
    [c, c, c, c, c, c, c, c, c, f, a, a, a, a, e, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, f, a, a, a, a, e, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, f, a, a, a, a, e, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, f, a, a, a, a, e, c, c, c, c, c, c, c, c, c, c],
    [c, c, d, d, d, d, d, d, d, j, a, a, a, a, k, d, d, d, d, c, c, c, c, c, c],
    [c, j, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c],
    [f, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c],
    [j, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c],
    [b, b, b, b, b, b, b, b, b, o, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, j, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c],
    [c, c, c, c, c, c, c, j, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c],
    [c, c, c, c, c, c, c, b, b, b, b, b, b, b, b, b, b, b, b, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c]
])

map3 = Map([
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, h, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, f, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, f, a, a, a, a, a, a, a, a, a, a, a, e, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, b, b, i, a, a, a, a, h, b, b, b, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, f, a, a, a, a, e, c, c, c, c, c, c, c, c, c, c]
])

map4 = Map([
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c],
    [c, c, d, d, d, d, d, d, c, c, c, c, c, c, c, c, d, d, d, d, d, d, d, c, c],
    [c, j, a, a, a, a, a, a, k, c, c, c, c, c, c, j, a, a, a, a, a, a, a, k, c],
    [f, a, a, a, a, a, a, a, a, e, c, c, c, c, f, a, a, a, a, a, a, a, a, a, e],
    [j, a, a, a, a, a, a, a, a, k, c, c, c, c, j, a, a, a, a, a, a, a, a, a, k],
    [a, a, a, a, a, a, a, a, a, a, k, c, c, j, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, e, f, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, k, j, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [i, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, h],
    [c, i, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, h, c],
    [c, c, i, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, h, c, c],
    [c, c, c, i, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, h, c, c, c],
    [c, c, c, c, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, c, c, c, c],
    [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c]
])

map_layout = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]