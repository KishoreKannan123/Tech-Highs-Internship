import cv2
from colour import colour
import random
import os

def Processed_image(image_path,touch,size,file_to_delete):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image,size)#.astype('uint8')
    color_array = image[touch[1]][touch[0]]
    color = colour(color_array)
    rectangle_color = tuple([int(color_array[0]),int(color_array[1]),int(color_array[2])])
    text_colour = (0,0,0)
    thickness = 2
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontscale = 1
    spacing = 4
    (w, h), _ = cv2.getTextSize(color, cv2.FONT_HERSHEY_SIMPLEX, fontscale, thickness)
    if(touch[0]<250):
        image = cv2.rectangle(image, (touch[0]-spacing,touch[1]+spacing), (touch[0]+w+spacing,touch[1]-h-spacing), rectangle_color, thickness) 
        image = cv2.putText(image,color, (touch[0],touch[1]), font,  
                    fontscale, text_colour, thickness, cv2.LINE_AA) 
    else:
        image = cv2.rectangle(image, (touch[0]-spacing-200,touch[1]+spacing), (touch[0]+w+spacing-200,touch[1]-h-spacing), rectangle_color, thickness) 
        image = cv2.putText(image,color, (touch[0]-200,touch[1]), font,  
                    fontscale, text_colour, thickness, cv2.LINE_AA) 
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if os.path.exists(file_to_delete):
        os.remove(file_to_delete)
    save_path = r'example_images\tmp'+str(random.randint(1,1000000))+'.jpg'
    cv2.imwrite(save_path,image) 
    return save_path,color
