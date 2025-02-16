from tkinter import Tk, BOTH, Canvas 

class Window():

    def __init__(self, width, height):
        self.width = width 
        self.height = height
        self.__root = Tk()
        self.__root.title = "Window"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.running = False 
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)
    
    def wait_for_close(self):
        self.running = True 
        while self.running:
            self.redraw()
        print("Window closed...")
    
    def close(self):
        self.running = False 

class Point():
    def __init__(self, x, y):
        self.x = x 
        self.y = y

class Line():
    def __init__(self, p1, p2):
        self.p_1 = p1 
        self.p_2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p_1.x, self.p_1.y, self.p_2.x, self.p_2.y, fill=fill_color, width = 2
            )






        

        
        















