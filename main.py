from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw

# ------------------------- CONSTANTS --------------------------#
window = Tk()
White = "#f1f6f7"
Bg = "#69ceec"
filetype = [('Jpg files', '*jpg'), ('PNG files', '*.png'), ('All files', '*.*')]


# ------------------------- UPLOAD PHOTO USING BUTTON --------------------------#
def upload_photo():
    global img_tk, new_window, img, label

    # SET NEW WINDOW FOR IMAGE
    new_window = Toplevel(window)
    new_window.geometry("600x500")
    new_window.title("Image display")

    # UPLOAD AND DISPLAY PHOTO

    file_name = filedialog.askopenfilename(filetypes=filetype)
    img = Image.open(file_name)
    img = img.resize((600, 500))
    img_tk = ImageTk.PhotoImage(image=img)
    label = Label(new_window, image=img_tk)
    label.image = img_tk
    label.pack()


# ------------------------- ADD TEXT TO THE PHOTO--------------------------#
def add_text():
    global img_tk, new_window, img, label, img_text
    text = text_entry.get()

    # COPY THE IMAGE AND ADD TEXT
    img_text = img.copy()
    draw = ImageDraw.Draw(img_text)
    text_position = (20, 20)
    text_color = (0, 0, 0)
    draw.text(text=text, xy=text_position,
              fill=text_color, font_size=30)

    # DISPLAY THE IMAGE
    img_tk = ImageTk.PhotoImage(image=img_text)
    label.config(image=img_tk)
    label.image = img_tk


# ------------------------- SAVE THE UPDATED PHOTO --------------------------#
def save_photo():
    global img_text
    file_names = filedialog.asksaveasfilename(defaultextension=".png",
                                              filetypes=filetype)
    img_text.save(file_names)


# ------------------------- WINDOW --------------------------#
window.title("Logo Adder")
window.minsize(width=600, height=500)
window.config(padx=100, pady=50, bg=Bg)

# ------------------------- TITLE TEXT --------------------------#
text_label = Label(text="Add logo to your Image", font=("Arial", 30, "bold"), background=Bg)
text_label.grid(column=1, row=1)

# ------------------------- SET A CANVAS --------------------------#
canvas = Canvas(width=400, height=300)
canvas.grid(column=1, row=2)

# ------------------------- LABELS,ENTRY AND BUTTONS -------------------------#
upload_label = Label(width=20, text="Upload an Image", font=("Arial", 10, "bold"))
upload_label.place(x=170, y=90)

upload_button = Button(text="Upload", command=upload_photo)
upload_button.place(x=180, y=120)

text_label = Label(width=30, text="Add text to the Image", font=("Arial", 10, "bold"))
text_label.place(x=150, y=170)

text_entry = Entry()
text_entry.place(x=160, y=190)

add_button = Button(text="Add", command=add_text)
add_button.place(x=180, y=220)

text_label = Label(width=30, text="Save the updated photo", font=("Arial", 10, "bold"))
text_label.place(x=140, y=270)

save_button = Button(text="Save", command=save_photo)
save_button.place(x=180, y=300)

window.mainloop()
