import pygame

def create_tiled_surface(size, filename):
    """Returns a surface with the specified size (width and height,
       as a 2-tuple), tiled using the image with the given filename."""

    surface = pygame.Surface(size).convert()
    tile = pygame.image.load(filename).convert()
    width, height = size
    tile_width, tile_height = tile.get_size()

    y = 0
    while y < height:
        x = 0
        while x < width:
            surface.blit(tile, (x, y))
            x += tile_width
        y += tile_height

    return surface