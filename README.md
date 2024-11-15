# Python Tkinter Project

This Python project is a graphical user interface (GUI) application built using Tkinter and several libraries to provide a variety of useful features such as a real-time clock, quote generator, image display, internet speed test, file organization, encryption, and decryption.

## Libraries Used

- `tkinter`: For creating the GUI application.
- `time`: For handling time-related functionality.
- `datetime`: For displaying the current date and time.
- `send2trash`: For safely sending files to the trash.
- `cryptography`: For implementing encryption and decryption functionalities.
- `requests`: For making HTTP requests, used for internet speed testing.
- `bs4`: For web scraping and parsing HTML content.
- `os`: For interacting with the operating system, such as working with files and directories.
- `shutil`: For file operations like copying and moving files.
- `random`: For generating random values, used for various functionalities like generating random quotes.
- `PIL` (Python Imaging Library): For working with images.

## Features

### 1. **Home Tab**
   - **Time and Date**: Displays the current time and date.
   - **Quote Generator**: Shows a random inspirational quote.
   - **Waterfall Image**: Displays a beautiful waterfall image.
   - **Internet Speed Test**: Includes a button that calculates the download and upload speeds of your internet connection.

### 2. **Organizer Tab**
   - **Choose Directory**: A button that opens a file explorer window to allow the user to choose a directory.
   - **Organize**: A button that organizes files within the chosen directory (you can define the logic for organizing the files).
   - **Refresh**: Clears the log of organized directories and their status.

### 3. **Encrypter Tab**
   - **Choose Directory**: A button that opens a file explorer window to allow the user to choose a directory.
   - **Encrypt**: A button that encrypts files in the chosen directory using cryptographic methods.
   - **Refresh**: Clears the log of encrypted directories and their status.

### 4. **Decrypter Tab**
   - **Choose Directory**: A button that opens a file explorer window to allow the user to choose a directory.
   - **Decrypt**: A button that decrypts files in the chosen directory using cryptographic methods.
   - **Refresh**: Clears the log of decrypted directories and their status.

## Installation

To run this project, you'll need Python installed along with the required libraries. To install the necessary libraries, you can use `pip`:

```bash
pip install -r requirements.txt
```
