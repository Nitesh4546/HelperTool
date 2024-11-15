import os
import functions
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from PIL import Image, ImageTk
from tkinter import filedialog

#Declerations
FILEPATH = ""
ORGANISEPATH = ""
SORTPATH = ""
CURRENTPATH = os.getcwd()
root = tk.Tk()


root.title("Application")
root.geometry("600x400")
root.iconbitmap("feather.ico")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)
tab3 = tk.Frame(notebook)
tab4 = tk.Frame(notebook)

#--------------------------------------------------Tab 1------------------------------------------------------
#HOME
#--------------Image---------------
image = Image.open("img.png")
image = image.resize((150, 150))
image_tk = ImageTk.PhotoImage(image)

tk.Label(tab1, image=image_tk).pack(side=tk.TOP, anchor="ne")
#---------------------Clock---------------
def update_time():
    current_time = datetime.now().strftime("%I:%M %p")
    current_date = datetime.now().strftime("%A, %B %d, %Y")
    time_label.config(text=f"{current_time}\n{current_date}")
    time_label.after(1000, update_time)

time_label = tk.Label(tab1, font=("Helvetica", 20))
time_label.place(x=10, y=10)
update_time()
#-----------Data Speed--------------

def data_speed():
    data = functions.check_internet_speed()
    data_info_label.config(text=data)

data_info_label = tk.Label(tab1)
data_info_label.pack(side=tk.BOTTOM)
tk.Button(tab1,text="Check data speed", command= data_speed).pack(side=tk.BOTTOM)
#-----------Quote----------------
a = functions.quote()
quote_label = tk.Label(tab1, text=f"Quote of the day\n{a}", font=("Helvetica", 14, "italic"), fg="darkblue", wraplength=550,width=200)
quote_label.pack()

#--------------------------------------------------Tab 2------------------------------------------------------
#ORGANIZER
#---------------Organise---------
tk.Label(tab2,text = "Organise your Files",font=("Helvetica", 16, "bold")).pack()
def action_organise():
    global ORGANISEPATH
    ORGANISEPATH = filedialog.askdirectory(title="Choose the directory to organize")
    action_organise_label.config(text = f"The directory selected:\n{ORGANISEPATH}")
action_organise_label = tk.Label(tab2)
action_organise_label.pack(pady=10)

def organise():
    functions.organize_files_by_category(ORGANISEPATH)
    organise_label.config(text="Files are organized")
organise_label = tk.Label(tab2)
organise_label.pack()

def refresh_or():
    action_organise_label.config(text="")
    organise_label.config(text="")

tk.Button(tab2,text="Choose directory.",command=action_organise, width=50).pack(pady=10)
tk.Button(tab2,text="Organize the files",command=organise, width=50).pack()
tk.Button(tab2, text="Refresh", command=refresh_or, width=50).pack(side = tk.BOTTOM,pady=10)

#--------------------------------------------------Tab 3------------------------------------------------------
#ENCRYPTER
#---------------Encrypt-----------------
tk.Label(tab3,text = "Encrypt the files",font=("Helvetica", 16, "bold")).pack()
def action_encrypt():
    global FILEPATH
    FILEPATH = filedialog.askdirectory(title="Choose the dir to encrypt")
    action_encrypt_label.config(text=f"The directory selected:\n\n{FILEPATH}")
action_encrypt_label = tk.Label(tab3)
action_encrypt_label.pack(pady=10)


def filecaller(path:str) -> list:

    with open(f"{os.path.join(path,'names.txt')}",'r') as file:
        data = file.readlines()
    content = list(map(str.strip,data))
    return content

def encrypt():
    global FILEPATH, CURRENTPATH
    # Important variables & condition checks
    if os.path.exists("Data") and len(os.listdir("Data")) != 0:
        error_label.config(text="Data folder exists and has files in it. Please move the folder to another location or delete the folder.")
        return
    os.makedirs("Data", exist_ok=True)
    safe = os.path.join(CURRENTPATH, "Data")
    files = os.listdir(FILEPATH)
    # Recording the dir. in a txt file
    functions.writePath(safe, FILEPATH)
    # Adding the file names to the txt file
    functions.add_files(files, FILEPATH)
    files = filecaller(safe)
    # Giving files fake names
    functions.fake_names(files, FILEPATH)
    # Encrypting the files
    encrypt_label.config(text=functions.encryption(safe, FILEPATH))
encrypt_label = tk.Label(tab3)
error_label = tk.Label(tab3)
encrypt_label.pack()
error_label.pack()

def refresh_en():
    action_encrypt_label.config(text="")
    encrypt_label.config(text="")
    error_label.config(text="")    


tk.Button(tab3, text="Choose directory", command=action_encrypt, width=50).pack(pady=10)
tk.Button(tab3, text="Encrypt the files", command=encrypt, width=50).pack()
tk.Button(tab3, text="Refresh", command=refresh_en, width=50).pack(side = tk.BOTTOM,pady=10)

#--------------------------------------------------Tab 4------------------------------------------------------
#DECRYPTER
#-------------------------Decryption-----------
tk.Label(tab4,text = "Dencrypt the files",font=("Helvetica", 16, "bold")).pack()
def action_decrypt():
    global FILEPATH
    FILEPATH = filedialog.askdirectory(title="Choose the Folder with Key and files")
    action_decrypt_label.config(text = f"The directory selected:\n\n{FILEPATH}")
action_decrypt_label = tk.Label(tab4)
action_decrypt_label.pack(pady=10)

def decrypt():
    if len(os.listdir(FILEPATH)) != 3:
        tk.Label(tab4,text="Files are missing from the Data folder.").pack()
        return
    with open(f'{FILEPATH}\\encrypt_dir.txt', 'r') as file:
        get_path = file.read().strip()#encryptrypted dir path

    #FILEPATH->key dir path
    #encryptrypted files without real names
    files = []
    for file in os.listdir(get_path):
        if os.path.isfile(os.path.join(get_path,file)):
            files.append(file)
    decrypt_label.config(text=functions.decryption(files, FILEPATH, get_path))
    functions.realName(FILEPATH, get_path)
decrypt_label = tk.Label(tab4)
decrypt_label.pack()

def refresh_de():
    action_decrypt_label.config(text="")
    decrypt_label.config(text="")

tk.Button(tab4, text="Choose directory", command=action_decrypt, width=50).pack(pady=10)
tk.Button(tab4, text="Decrypt the files", command=decrypt, width=50).pack()
tk.Button(tab4, text="Refresh", command=refresh_de, width=50).pack(side = tk.BOTTOM,pady=10)

#Adding tabs to the notebook
notebook.add(tab1, text="Home")
notebook.add(tab2, text="Organizer")
notebook.add(tab3, text="Encrypt")
notebook.add(tab4, text="Decrypt")

root.mainloop()