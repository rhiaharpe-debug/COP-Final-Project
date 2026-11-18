
import pygame as p
class Cell:
    def __init__(self,value,row,col,screen):
        self.value=value
        self.row=row
        self.col=col
        self.screen=screen
        self.sketched_value=0
        self.selected=False

        # Added Size and Position
        self.size = 44
        self.offset_x=0
        self.offset_y=0

    def set_cell_value(self,value):
        self.value=value
        self.sketched_value=0

    def set_sketched_value(self,value):
        self.sketched_value=value

    def draw(self):
        s=self.size
        x=self.col*s + self.offset_x
        y=self.row*s + self.offset_y
        if self.value!=0:
            f=p.font.Font(None,int(s * 0.8))
            t=f.render(str(self.value),True,(0,0,0))

            text_rect = t.get_rect(
                center=(x + s // 2, y + s // 2)
            )

            self.screen.blit(t,(x+20,y+10))

        elif self.sketched_value!=0:
            f=p.font.Font(None,int(s * 0.45))
            t=f.render(
                str(self.sketched_value),
                True,
                (120,120,120)
            )
            self.screen.blit(t,(x+5,y+5))

        if self.selected:
            p.draw.rect(
                self.screen,
                (255,0,0),
                (x,y,s,s),
                3
            )
