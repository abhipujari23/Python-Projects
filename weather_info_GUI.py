from tkinter import *
from PIL import Image, ImageTk
from weather_info import weatherAPIinfo, wdirection

def update_location():
    root.geometry('500x330')
    current_location = location.get()
    info = weatherAPIinfo(current_location)
    location_label = Label(root, text='Location:', bg='#313131', fg='#FFFFFF', font=('Arial Regular', 16))
    location_label.place(x=187, y= 95)
    location_name = info['location']['name']
    location_region = info['location']['region']
    location_value = Label(root, text=f'{location_name}, {location_region}', bg='#313131', fg='#FFFFFF', font=('Arial Regular', 16))
    location_value.place(x=281, y= 95)
    temperature_label = Label(root, text="Temperature:", bg='#313131', fg='#FFFFFF', font=('Arial Regular', 16))
    temperature_label.place(x= 150, y= 134)
    temp_c = info['current']['temp_c']
    temp_f = info['current']['temp_f']
    temperature_value = Label(root, text=f'{temp_c}°C / {temp_f}°F', bg='#313131', fg='#FFFFFF', font=('Arial Regular', 16))
    temperature_value.place(x=281, y=134)
    feelslike_label = Label(root, text='Feels Like:', bg='#313131', fg='#FFFFFF', font=('Arial Regular', 16))
    feelslike_label.place(x=169, y=173)
    feelslike_c = info['current']['feelslike_c']
    feelslike_f = info['current']['feelslike_f']
    feelslike_value = Label(root, text=f'{feelslike_c}°C / {feelslike_f}°F', bg='#313131', fg='#FFFFFF', font=('Arial Regular', 16))
    feelslike_value.place(x=281, y=173)
    weather_label = Label(root, text='Weather:', bg='#313131', fg='#FFFFFF', font=('Arial Regular', 16))
    weather_label.place(x=185, y=212)
    weather_condition = info['current']['condition']['text']
    weather_value = Label(root, text=f'{weather_condition}', bg='#313131', fg='#FFFFFF', font=('Arial Regular', 16))
    weather_value.place(x=281, y=212)
    wind_label = Label(root, text='Wind:', bg='#313131', fg='#FFFFFF', font=('Arial Regular', 16))
    wind_label.place(x=218, y=251)
    wind_speed = info['current']['wind_kph']
    wind_direction = wdirection(info['current']['wind_dir'])
    wind_value = Label(root, text=f'{wind_speed}kph {wind_direction}', bg='#313131', fg='#FFFFFF', font=('Arial Regular', 16))
    wind_value.place(x=281, y=251)
    size = 64
    img = info['current']['condition']['icon'].split('/')
    display_image(f"F:\\IANT\\Python\\projects\\weather\\64x64\\{img[-2]}\\{img[-1]}", 54, 88, size, size)

def display_image(path, x, y, width, height):
    image = Image.open(path)
    image = image.convert('RGBA')
    mask = Image.new('RGBA', image.size, (0, 0, 0, 0))
    mask.paste(image, (0, 0), image)
    photo = ImageTk.PhotoImage(mask)
    label = Label(root, image=photo, bg='#313131')
    label.place(x=x, y=y, width=width, height=height)
    label.image = photo

    def update_bg_color(event):
        label.configure(bg=root.cget('bg'))

    root.bind('<Configure>', update_bg_color)


root = Tk()
root.geometry('500x100')
root.title("Weather update")

root.configure(bg='#313131')

label = Label(root, text="Weather Update", bg="#313131", fg='#FFFFCC' , font=('Arial Bold', 12))
label.place(x=10, y=10)

location = Entry(root, width=13, font='Arial 14')
location.place(x=250, y=15)
submit = Button(root, text='Submit', height=1, command=update_location).place(x=390,y=15)

mainloop()
