import pygame
from math import sin, cos

WHITE = (255, 255, 255)

class Ray():
    def __init__(self,screen, size) -> None:
        self.size = size
        self.screen = screen
        x_cordinates, y_cordinates = size
        self.cordinates = x_cordinates/2, y_cordinates/2  
        self.offscreen = 100
    
    def march(self, objects, angle): # objects = [(pos, radius)]
        pygame.draw.circle(self.screen, WHITE, self.cordinates, 4)
        counter = 50
        current_position = self.cordinates
        for (object_position, raduis, color) in objects:
            pygame.draw.circle(self.screen, color, object_position, raduis)
            
        while counter > 0:
            signed_distances = [1300]
            for (object_position, raduis, color) in objects:
                signed_distances.append(self.Signed_Distance(current_position, object_position, raduis))
            
            pygame.draw.circle(self.screen, WHITE, current_position, min(signed_distances), 1)
            new_position = self.spherical_cordinates(current_position, min(signed_distances), angle)
            pygame.draw.circle(self.screen, WHITE, new_position, 2)
            pygame.draw.line(self.screen, WHITE, current_position, new_position)
            
            current_position = new_position
            counter -= 1
            if min(signed_distances) < 5:
                break 
            if self.off_screen(current_position):
                break
    
    def Signed_Distance(start_position, end_position, radius):
        start_x_position, start_y_position = start_position 
        end_x_position, end_y_position = end_position
        distance = ((end_x_position - start_x_position)**2 + (end_y_position - start_y_position)**2)**0.5
        return distance - radius
    
    def spherical_cordinates(self, start_cordinates, radius, angle):
        start_x_cordinate, start_y_cordinate = start_cordinates
        end_x_cordinate = radius * sin(angle) + start_x_cordinate
        end_y_cordinate = radius * cos(angle) + start_y_cordinate
        return end_x_cordinate, end_y_cordinate
    
    def off_screen(self, current_cordinates):
        x_cordinate, y_cordinate = current_cordinates
        boundary_x, boundary_y = self.size
        if x_cordinate - self.offscreen > boundary_x or x_cordinate < -self.offscreen:
            return True
        if y_cordinate - self.offscreen > boundary_y or y_cordinate < -self.offscreen:
            return True
        else:
            return False
