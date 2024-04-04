import PIL.ImageTk
import PIL.Image
import PIL.ImageOps
from tkinter import *

global main_image
main_image = input('Image Name: ')

root = Tk()
root.title("Hologram")
root.geometry("900x1000")
root.resizable(0, 0)

def importimg(file_name, rotate_angle, size, flip_image):
    global im
    im = PIL.Image.open(file_name)
    if rotate_angle != 0:
        im = im.rotate(rotate_angle, PIL.Image.NEAREST, expand = 1)
    while True:
        im = im.resize((round(im.size[0]*0.8), round(im.size[1]*0.8)))
        if im.size[0] + im.size[1] <= size:
            print(im.size)
            print(file_name)
            if flip_image:
                im = PIL.ImageOps.flip(im)
            # im.save('donotcare.png', format = 'png')
            break
    # print(im.size)
    return PIL.ImageTk.PhotoImage(im)

#x import and placement

x = importimg('x.png', 0, 1000, False) #importimg('x.png', 0, 1560, False)

x_frame = Frame(width = im.size[0], height = im.size[1])
x_frame.pack()
x_frame.place(anchor='center', relx = 0.5, rely = 0.5, width = im.size[0], height = im.size[1]) #RELX AND RELY BETWEEN 0-1

#left import and placement

left_image = importimg(main_image, 90, 540, False)
left_image_size = im.size

left_frame = Frame(width = im.size[0], height = im.size[1])
left_frame.pack()
left_frame.place(anchor='w', relx = 0.005, rely = 0.5, width = im.size[0], height = im.size[1])

#right image import and placement

right_image = importimg(main_image, 270, 540, True)
right_image_size = im.size

right_frame = Frame(width = im.size[0], height = im.size[1])
right_frame.pack()
right_frame.place(anchor='e', relx = 0.995, rely = 0.5, width = im.size[0], height = im.size[1])

#up image import and placement

up_image = importimg(main_image, 0, 540, False)
up_image_size = im.size

up_frame = Frame(width = im.size[0], height = im.size[1])
up_frame.pack()
up_frame.place(anchor='n', relx = 0.5, rely = 0.005, width = im.size[0], height = im.size[1]) #up_image_size[1] / 2000

#down image import and placement

down_image = importimg(main_image, 0, 540, True)
down_image_size = im.size

down_frame = Frame(width = im.size[0], height = im.size[1])
down_frame.pack()
down_frame.place(anchor='s', relx = 0.5, rely = 0.995, width = im.size[0], height = im.size[1]) #down_image_size[1] / 2000


#pack

x_label = Label(x_frame, image = x)
x_label.pack()

left_label = Label(left_frame, image = left_image, width = left_image_size[0], height = left_image_size[1])
left_label.pack()

right_label = Label(right_frame, image = right_image, width = right_image_size[0], height = right_image_size[1])
right_label.pack()

up_label = Label(up_frame, image = up_image, width = up_image_size[0], height = up_image_size[1])
up_label.pack()

down_label = Label(down_frame, image = down_image, width = down_image_size[0], height = down_image_size[1])
down_label.pack()

root.mainloop()

