# Free PC Games Finder

![Preview](https://github.com/user-attachments/assets/3f9dfbd9-6208-4f8b-8bff-9cbd3aea5e94)

## 📖 Introduction

Free PC Games Finder is a desktop app built with Python for discovering free PC games.
It connects to the freetogame.com API and lets you filter games by release year, genre, or both simultaneously.

The app's interface is built with CustomTkinter GUI, complete with a CTkTextbox for showing the filtered games, and includes success and fail sound effects for button interactions.

---

## ✨ Features

🕹 Search for free PC games by genre.

📅 Search for free PC games by release year.

🔎 Combine genre and year filters for precise results.

🖥 Display results neatly in a scrollable CTkTextbox.

🔊 Success and fail sounds when performing searches.

---

## 🚀 Installation

1. git clone https://github.com/PetriK93/Free-PC-Games-Finder.git  
    cd Free-PC-Games-Finder

2. Create a virtual environment (optional but recommended)

   python -m venv venv  
   source venv/bin/activate # On Linux / macOS  
   venv\Scripts\activate # On Windows

3. Install dependencies

   pip install customtkinter pillow pygame requests webbrowser

4. Run the app

   python main.py

   ***

## 💻 How to use the app

Choose a folder containing files you want to organize.

The app will scan and categorize files by type.

Subfolders are automatically created for each file type.

Files are moved into their corresponding folders.

Switch between dark and light mode — your choice is saved for next time! 🎉

---

## 📦 Dependencies

Python 3.12.10

customtkinter

pygame

pillow

requests

webbrowser

---

## 📝 License

This project is open source under the MIT License.
