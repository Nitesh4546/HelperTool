import os
import random
import shutil
import requests
import speedtest
from send2trash import send2trash
from bs4 import BeautifulSoup as bs
from cryptography.fernet import Fernet

motivational_quotes = [
    "What great thing would you attempt,\n if you knew you could not fail.",
    "It's not about money or connections. It's the willingness to outwork and outlearn everyone when it comes to your business.",
    "Success is not final; failure is not fatal; it is the courage to continue that counts.",
    "Don't stop when you're tired. Stop when you're done.",
    "Shoot for the moon. Even if you miss,\n you'll land among the stars.",
    "The journey of a thousand miles begins with one step.",
    "Act as if what you do makes a difference. IT DOES.",
    "Always take another step. If this is to no avail take another,\n and yet another. One step at a time is not too difficult.",
    "If you can't fly, then run,\n if you can't run then walk,\n if you can't walk then crawl,\n but whatever you do, you have to keep moving forward.",
    "Much effort, much prosperity.",
    "Your true success in life begins only when you make the commitment to become excellent at what you do.",
    "Much good work is lost for the lack of a little more.",
    "Your biggest failure is the thing you dreamed of contributing but didn't find the guts to do.",
    "That some achieve great success,\n is proof to all that others can achieve it as well.",
    "Never let the fear of striking out get in your way.",
    "Hustle until you no longer need to introduce yourself.",
    "The heights by great men reached and kept,\n were not attained by sudden flight,\n but they, while their companions slept,\n were toiling upward in the night.",
    "He who would accomplish little must sacrifice little; he who would achieve much must sacrifice much.",
    "If you wish to be out front,\n then act as if you were behind.",
    "The key to success is failure.",
    "Formula for success: rise early, work hard, strike oil.",
    "Plough deep while sluggards sleep.",
    "Work hard in silence and let success be your noise.",
    "Don't stop until you're proud.",
    "The path to success is to take massive,\n determined action.",
    "If it's important,\n you'll find a way. If it's not,\n you'll find an excuse.",
    "Men of action are favored by the goddess of good luck.",
    "A somebody was once a nobody who wanted to and did.",
    "Man cannot discover new oceans unless he has the courage to lose sight of the shore.",
    "If you believe you can do a thing,\n you can do it."
]


def check_internet_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert from bits to megabits
        upload_speed = st.upload() / 1_000_000  # Convert from bits to megabits
        ping = st.results.ping
        return f"Download Speed: {download_speed:.2f} Mbps\nUpload Speed: {upload_speed:.2f} Mbps\nPing: {ping:.2f} ms"
    except Exception as e:
        return "Unable to retrive the data"


def quote():
    try:
        url = "https://www.bing.com/search?q=Quote%20of%20the%20day&form=ML2BFU&OCID=ML2BFU&PUBL=RewardsDO&PROGRAMNAME=QuoteOfTheDay&CREA=ML2BFU"
        response = requests.get(url).content
        soup = bs(response,'html.parser')
        div = soup.find('div',class_="bt_quoteText")
        return (div.get_text())
    except Exception as e:
        return random.choice(motivational_quotes)


def writePath(safe: str, path_: str) ->str:
    '''
    Record the dir. that you want to encrypt in a file Encrypt_dir.txt
    '''
    with open(f"{safe}\\Encrypt_dir.txt",'a') as file:
        file.write(path_)
    return "Done"

def add_files(files: list, path: str) ->str:
    '''
    This function adds the file names inside folder to a text file named as
    names.txt.
    '''
    with open("Data\\names.txt",'a') as file:
        for i in files:
                if os.path.isfile(os.path.join(path,i)):
                    file.write(i+'\n')         
        return "Names are added"


def fake_names(files: list, enPath:str) ->str:
    '''
    This function assigns the files a fake name which makes the files unable to
    recognize. file->list is list containg the file from the dir. that is going to be encrytpted.
    '''
    total = len(files)
    fake = range(total)
    for i in range(len(files)):
        os.rename(os.path.join(enPath,files[i]),os.path.join(enPath,str(fake[i])).zfill(5))
    return "Fake names are given."

def encryption(safe :str,path :str) ->str:
    """
    This function takes one argument path -> str which you want to encrypt.
    And generate a key that will be used to decrypte the files in the future.
    file->list is list containg the file from the dir. that is going to be encrytpted.
    """
    os.chdir(path)
    files = os.listdir()
    key = Fernet.generate_key()#key generated
    with open(f'{safe}\\TheKey.key',"wb")  as thekey:
        thekey.write(key)

    for file in files:
        if os.path.isfile(os.path.join(path,file)):
            with open(file,"rb") as thefile:
                contents = thefile.read()
            contents_encrypted = Fernet(key).encrypt(contents)
            with open(file,"wb") as thefile:
                thefile.write(contents_encrypted)
    return "Files have been encrypted"
def decryption(files: list,safe: str,path : str) ->str:
    '''Decrypts the files using the key.
       safe-> str is a path where the encryption key and other two files are stored
       path-> str is the path of the dir. you want to dencrypt.
       file->list is list containg the file from the dir. that is going to be decrytpted.'''

    os.chdir(path)
    #files = os.listdir()
    with open(f'{safe}\\TheKey.key',"rb")  as key:
        secertKey = key.read()#stored the key in secertKey variable

    for file in files:
        with open(file,"rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secertKey).decrypt(contents)
        with open(file,"wb") as thefile:
            thefile.write(contents_decrypted)
    return (f"Files of directory : {path} \nhas been decrypted.")

def realName(safe: str,path: str)->str:
    '''
    Gives the files their real names.
    safe-> str is the path where the encryption key is stored 
    path-> str is the path of the dir. you decrypted.
    '''
    os.chdir(path)
    #files = os.listdir()
    files = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,file)):
            files.append(file)
    with open(f'{safe}\\names.txt','r') as name:
        data = name.read()
    names = data.split('\n')
    names.remove('')
    for i in range(len(files)):
        os.rename(files[i],names[i])
    os.chdir(safe)
    for i in ["names.txt","TheKey.key","Encrypt_dir.txt"]:
        send2trash(i)
    return("Original names are given back to the files")


def organize_files_by_category(directory):
    # Dictionary to define file categories and their extensions
    categories = {
        'doc': ['txt', 'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx','csv'],
        'code': ['py','c','html','css','json','cpp'],
        'pic': ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
        'audio': ['mp3', 'wav'],
        'video': ['mp4', 'avi', 'mkv'],
        'archive': ['zip', 'rar', 'tar', 'gz'],
    }

    if not os.path.exists(directory):
        return
    
    # Create "Other" folder if it doesn't exist for unmatched extensions
    other_folder = os.path.join(directory, 'Other')
    if not os.path.exists(other_folder):
        os.makedirs(other_folder)
    
    # Loop through all the files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories, we only want to organize files
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension
        _, extension = os.path.splitext(filename)
        extension = extension[1:].lower()  # Remove the dot and convert to lowercase
        
        # Skip files with no extension
        if extension == "":
            continue
        
        # Find the category for the file based on its extension
        moved = False
        for category, extensions in categories.items():
            if extension in extensions:
                category_folder = os.path.join(directory, category)
                
                # Create the category folder if it doesn't exist
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                
                # Move the file to the appropriate category folder
                new_file_path = os.path.join(category_folder, filename)
                shutil.move(file_path, new_file_path)
                moved = True
                break
        
        # If the file doesn't match any category, move it to the "Other" folder
        if not moved:
            new_file_path = os.path.join(other_folder, filename)
            shutil.move(file_path, new_file_path)