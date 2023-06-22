class Ball:
    def __init__(self,canvas,x,y,diameter,xspeed,yspeed,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xspeed = xspeed
        self.yspeed = yspeed

    def move(self):
        coordinates = self.canvas.coords(self.image)
        #print(coordinates)
        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.xspeed = -self.xspeed
        if (coordinates[3] >= (self.canvas.winfo_height()) or coordinates[1] < 0):
            self.yspeed = -self.yspeed

        self.canvas.move(self.image,self.xspeed,self.yspeed)