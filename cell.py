
import pygame as p
class Cell:
    def __init__(self,value,row,col,screen):
        self.value=value
        self.row=row
        self.col=col
        self.screen=screen
        self.sketched_value=0
        self.selected=False
    def set_cell_value(self,value):
        self.value=value
        self.sketched_value=0
    def set_sketched_value(self,value):
        self.sketched_value=value
    def draw(self):
        s=60
        x=self.col*s
        y=self.row*s
        if self.value!=0:
            f=p.font.Font(None,40)
            t=f.render(str(self.value),True,(0,0,0))
            self.screen.blit(t,(x+20,y+10))
        elif self.sketched_value!=0:
            f=p.font.Font(None,25)
            t=f.render(str(self.sketched_value),True,(120,120,120))
            self.screen.blit(t,(x+5,y+5))
        if self.selected==True:
            p.draw.rect(self.screen,(255,0,0),(x,y,s,s),3)
