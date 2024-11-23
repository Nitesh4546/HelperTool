# Application
#### Video Demo: [Link to Video Demo](https://youtu.be/mesaZPQCkrw)
#### Description:

**Application** is a multi-functional desktop application created in Python using Tkinter. Designed to simplify various tasks, this tool combines file organization, encryption, decryption, and real-time information display in a user-friendly interface. With an intuitive design, it’s suitable for users looking to manage files efficiently, secure sensitive data, and monitor internet speed in one place. The application includes four main tabs, each offering unique features:

### Features

1. **Home Tab**  
   The Home tab is the main dashboard, providing users with essential information and utilities:
   - **Date and Time**: The current date and time are displayed at the top of the screen.
   - **Quote of the Day**: A motivational or thought-provoking quote appears to inspire users daily.
   - **Waterfall Image**: For a touch of relaxation, a beautiful waterfall image is displayed as the background.
   - **Internet Speed Test**: A button to check the upload and download speeds of the internet connection. Users can quickly assess network performance without needing a separate application.

2. **Organizer Tab**  
   This tab simplifies file management with three core functions:
   - **Choose Directory**: Opens a file explorer window, allowing users to select a folder for organization.
   - **Organize**: The selected directory is scanned, and files are automatically organized into folders based on file type (e.g., images, documents, videos).
   - **Refresh**: Clears the status log, enabling users to start organizing a new directory or re-organize the same one.

3. **Encrypter Tab**  
   Data security is a key feature of Application. The Encrypter tab allows users to encrypt files within a selected directory:
   - **Choose Directory**: Users can select a folder to encrypt all contained files.
   - **Encrypt**: All files within the chosen directory are encrypted, providing an additional layer of security.
   - **Refresh**: Clears the log of encrypted files and directories for a fresh start.

4. **Decrypter Tab**  
   This tab offers decryption capabilities for previously encrypted files:
   - **Choose Directory**: Opens a window to select the folder containing encrypted files.
   - **Decrypt**: Decrypts the files, restoring them to their original form.
   - **Refresh**: Clears the log, making it easy to work with multiple folders in succession.

### Technologies Used
Application is built with various libraries to ensure functionality and user experience:
- **Tkinter**: The primary library for GUI creation, providing a seamless interface for users.
- **time** and **datetime**: For displaying and updating date and time.
- **send2trash**: For moving files to the recycle bin safely.
- **cryptography**: Implements encryption and decryption for user data security.
- **requests** and **bs4 (BeautifulSoup)**: Requests checks for internet speed, while BeautifulSoup can be used for quote retrieval from online sources.
- **PIL (Pillow)**: To display and manage images, such as the waterfall background.

   ```bash
   git clone https://github.com/Nitesh4546/helpertool.git
   cd helpertool
   pip install -r requirements.txt

