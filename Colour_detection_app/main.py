import kivy
import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from colour import colour
from Bounding_box import Processed_image
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.clock import Clock
from kivy.config import Config
Config.set('graphics', 'maxfps', 0)
Config.set('graphics', 'resizable', False)
import os

class widgettree(BoxLayout):
    def __init__(self,**kwargs):
        super(BoxLayout,self).__init__(**kwargs)

class Picture(BoxLayout):
    colour = StringProperty('')
    To_be_deleted = StringProperty('some_file.jpg')
    def __init__(self,**kwargs):
        super(BoxLayout,self).__init__(**kwargs)
        with self.canvas.after:
            Color(1,1,1,1)
            self.Rectangle = Rectangle(source = r'example_images\1.jpg',pos = self.pos,size = (500,650))

    def on_touch_down(self, touch,*args):
        if self.collide_point(touch.x,touch.y):
            save_path,colour = Processed_image(r'example_images\1.jpg',(int(touch.x - self.pos[0]),int(self.size[1]-(touch.y-self.pos[1]))),(int(self.size[0]),int(self.size[1])),self.To_be_deleted)
            self.To_be_deleted = save_path
            self.canvas.ask_update()
            self.Rectangle.source = save_path
            self.colour = colour
            
class CDApp(App):
    def build(self,*args):
        self.title = 'Colour_detection_app'
        window = widgettree()
        pic = Picture()
        return window
    
if __name__ == '__main__':
    CDApp().run()
    dir = r'example_images'
    for _,_,file in os.walk(dir):
        for x in file:
            if(x!='1.jpg'):
                os.remove(os.path.join(dir,x))