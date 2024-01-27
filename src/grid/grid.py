from pydantic import BaseModel
import pygame

from src.art.color import WHITE


class Grid(BaseModel):
    rows:int
    cols:int
    pixel_per_tile:int
    
    def draw(self, screen: pygame.Surface) -> None:
        for col in range(self.cols):
            for row in range(self.rows):
                
                pygame.draw.rect(screen, WHITE, (col*self.pixel_per_tile, row*self.pixel_per_tile, self.pixel_per_tile/2, self.pixel_per_tile/2))
        
        
