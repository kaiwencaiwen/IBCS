import pygame
from pygame import gfxdraw


class GridWorld():
    def __init__(self, width, height, resolution):
        self.setup_dimensions(width, height, resolution)
        self.setup_window()
        self.setup_grid()

    def setup_dimensions(self, width, height, resolution):
        self.screen_width = width * resolution
        self.screen_height = height * resolution
        self.resolution = resolution
        self.grid_width = width  
        self.grid_height = height 
        self.size = [self.screen_width, self.screen_height]

    def setup_window(self):
        pygame.init()
        pygame.display.set_caption('GridWorld Simulation')
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
    
    def setup_grid(self):
        self.grid = [[0] * self.grid_height for i in range(0, self.grid_width)]
        self.cells = {}

    def set_cell(self, x, y, color):
        if self.is_valid_coordinate(x, y):
            self.grid[x][y] = color
            self.cells[(x, y)] = color

    def remove_cell(self, x, y):
        if (x, y) in self.cells: 
            del self.cells[(x, y)]

    def get_cell(self, x, y):
        if (x, y) in self.cells: 
            return self.cells[(x, y)]
        return -1

    def get_surroundings(self, x, y, depth):
        x_min = x - depth
        y_min = y - depth
        dim = 2 * depth + 1
        surroundings = [[-1] * dim for i in range(0, dim)]
        for x_offset in range(0, dim):
            for y_offset in range(0, dim):
                if self.is_valid_coordinate(x_min + x_offset, y_min + y_offset) and (x_min + x_offset, y_min + y_offset) in self.cells: 
                    surroundings[y_offset][x_offset] = self.cells[(x_min + x_offset, y_min + y_offset)]
        return surroundings
 
    def is_valid_coordinate(self, x, y):
        if x < 0 or x >= self.grid_width or y < 0 or y >= self.grid_height:
            return False
        return True

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def end(self): 
        pygame.quit()

    def update(self):
        self.screen.fill((0, 0, 0))
        for cell in self.cells:
            self.aa_round_rect(self.screen, (cell[0] * self.resolution, cell[1] * self.resolution, self.resolution, self.resolution), self.cells[cell], 3) 
        pygame.display.flip()

    def aa_round_rect(self, surface, rect, color, rad=20, border=0, inside=(0,0,0)):
        rect = pygame.Rect(rect)
        self._aa_render_region(surface, rect, color, rad)
        if border:
            rect.inflate_ip(-2*border, -2*border)
            self._aa_render_region(surface, rect, inside, rad)

    def _aa_render_region(self, image, rect, color, rad):
        corners = rect.inflate(-2*rad-1, -2*rad-1)
        for attribute in ("topleft", "topright", "bottomleft", "bottomright"):
            x, y = getattr(corners, attribute)
            gfxdraw.aacircle(image, x, y, rad, color)
            gfxdraw.filled_circle(image, x, y, rad, color)
        image.fill(color, rect.inflate(-2*rad,0))
        image.fill(color, rect.inflate(0,-2*rad))
    