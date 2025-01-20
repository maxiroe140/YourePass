# **YourePass - Secure Password Vault**

> *A simple, elegant password manager created for fun by* **maxiroe140**.  

⚠️ **Disclaimer**: This is a hobby project and not a fully secure application. Use it at your own risk! I (maxiroe140) take no responsibility for any data breaches, leaks, or security risks caused by the use of this software.

---

## **Features**

- Securely store your passwords with **encryption** protected by a **Master Key**.
- Add, view, and manage your passwords with ease.
- **Clipboard functionality**: Copy passwords with a single click.
- Sleek, user-friendly interface.
- Option to create a portable `.exe` file.

---

## **Download**

### 🔽 **Download YourePass.exe**

[**Download the latest release**](https://github.com/maxiroe140/YourePass/releases) *(Insert your release link here)*  

#### **Setup Instructions**
1. Download the `.exe` file.  
2. Create a dedicated folder and move the file **YourePass.exe** into it.  
3. Run the file **YourePass.exe** from the folder.  

---

## **Compile It Yourself**

If you prefer to compile the software yourself, follow these steps:

### **Requirements**
- **Python 3.10+** 
- Install the following Python libraries:  
```bash
  pip install cryptography pyperclip tk
```
- PyInstaller for converting the Python script into an .exe file:
```bash
  pip install pyinstaller
```

## Compilation Steps

1. Clone or download this repository:
```bash
   git clone https://github.com/maxiroe140/YourePass.git
   cd YourePass
```


2. Use PyInstaller to compile the program into a .exe file:
```bash
pyinstaller --onefile --noconsole --icon=icon.ico yourepass.py
```
    - Note: If you don’t have an icon file, remove the --icon=icon.ico parameter.

3. The compiled .exe file will appear in the dist folder. Move this file into its own folder.


# **Important Notes**

    1. File Location:
        - Always store YourePass.exe in a dedicated folder because the encrypted password file and Master Key file will be saved in the same directory.
    2. Security Warning:
        - This is not a 100% secure program.
        - Your passwords could potentially be exposed in the case of data leaks or improper use.
        - Use the program at your own risk.
    3. Backup:
        - Regularly back up your password data to prevent accidental loss.

# **Disclaimer**

This program was created purely for fun by **me**. It is not intended for professional use. Neither I nor anyone else assumes responsibility for the security of your passwords or data when using this software.

Thank you for trying out **YourePass**! 😊
Stay safe and enjoy!
~ maxiroe140