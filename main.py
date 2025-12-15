import customtkinter as ctk
from PIL import Image
import pygame
from functions import search_genre, search_year, search_both, write_output, visit_freetogame

# Initialize mixer for sound effects
pygame.mixer.init()
success_sound = pygame.mixer.Sound("success.wav")
fail_sound = pygame.mixer.Sound("fail.wav")

# Event handler for searching by genre
def on_search_genre():
    choice = dropdown_genre.get()

    if choice == "Select Genre":
        fail_sound.play()
        write_output(output_box, "Please select a genre.")
        print("Please select a genre.")
        return

    success_sound.play()
    search_genre(output_box, choice)


# Event handler for searching by year
def on_search_year():

    try:
        choice = int(search_year_input.get())

    except ValueError:
        fail_sound.play()
        write_output(output_box, "Please enter a year.")
        print("Please enter a year.")
        return

    success_sound.play()
    search_year(output_box, choice)


# Event handler for searching by genre & year
def on_search_both():

    try:
        choice_genre = dropdown_genre.get()
        choice_year = int(search_year_input.get())


        if choice_genre == "Select Genre":
            fail_sound.play()
            write_output(output_box, "Please select a genre.")
            print("Please select a genre.")
            return

        success_sound.play()
        search_both(output_box, choice_genre, choice_year)

    except ValueError:
        fail_sound.play()
        write_output(output_box, "Please choose a genre & year.")
        print("Please choose a genre & year.")
        return


# Colors for all the visual elements
colors = {
    "button": "#006400",
    "border": "#008500",
    "hover": "#004400",
    "background": "#2b2b2b",
    "font": "black",
    "button_text": "white",
    "placeholder_text": "gray60",
}

# Main window.
root = ctk.CTk()
root.title("Free PC Games Finder")
root.geometry("500x900")
root.resizable(False, False)
root.configure(fg_color=colors["background"])

# Logo details
img = Image.open("logo4.png")

# Scale width to 150px to keep aspect ratio
width = 190
ratio = width / img.width
height = int(img.height * ratio)

logo_image = ctk.CTkImage(
    size=(width, height),
    light_image=img,
    dark_image=img,
)

# Placeholder text for dropdown_genre menu
choose_genre = ctk.StringVar(value="Select Genre")

# Widgets
logo_label = ctk.CTkLabel(
    master=root,
    image=logo_image,
    text=""
)

dropdown_genre = ctk.CTkOptionMenu(
    master=root,
    values=["Shooter", "MMORPG", "Battle Royale", "ARPG", "Action RPG", "MMOARPG", "Fighting", "RPG"],
    fg_color=colors["button"],
    button_color=colors["button"],
    hover=False,
    font=("Arial", 20),
    corner_radius=10,
    width=250,
    height=50,
    text_color=colors["button_text"],
    variable=choose_genre,
)

search_genre_button = ctk.CTkButton(
    master=root,
    fg_color=colors["button"],
    border_width=2,
    border_color=colors["border"],
    corner_radius=10,
    text_color=colors["button_text"],
    hover_color=colors["hover"],
    font=("Arial", 20),
    width=250,
    height=50,
    text="Search By Genre",
    command=on_search_genre
)

search_year_input = ctk.CTkEntry(
    master=root,
    fg_color=colors["button"],
    border_width=2,
    border_color=colors["border"],
    corner_radius=10,
    text_color=colors["button_text"],
    placeholder_text_color=colors["placeholder_text"],
    font=("Arial", 20),
    width=250,
    height=50,
    placeholder_text="Type a year..."
)

search_year_button = ctk.CTkButton(
    master=root,
    fg_color=colors["button"],
    border_width=2,
    border_color=colors["border"],
    corner_radius=10,
    text_color=colors["button_text"],
    hover_color=colors["hover"],
    font=("Arial", 20),
    width=250,
    height=50,
    text="Search By Year",
    command=on_search_year
)

search_both_button = ctk.CTkButton(
    master=root,
    fg_color=colors["button"],
    border_width=2,
    border_color=colors["border"],
    corner_radius=10,
    text_color=colors["button_text"],
    hover_color=colors["hover"],
    font=("Arial", 20),
    width=250,
    height=50,
    text="Search By Genre & Year",
    command=on_search_both
)

output_box = ctk.CTkTextbox(
    master=root,
    width=440,
    height=250,
    wrap="word",
    corner_radius=10,
    fg_color="white",
    border_width=3,
    border_color=colors["border"],
    font=("Arial", 16),
    text_color=colors["font"]
)

# Make output_box read only and describe its purpose via text
output_box.insert("end", "Search results will appear here...\n")
output_box.configure(state="disabled")

website_label = ctk.CTkLabel(
    master=root,
    text="API kindly provided by freetogame.com",
    text_color="white",
    font=("Arial", 14, "underline"),
    cursor="hand2",
    fg_color="transparent"
)

# Widget placement
logo_label.place(relx=0.5, rely=0.138, anchor="center")
dropdown_genre.place(relx=0.5, rely=0.30, anchor="center")
search_genre_button.place(relx=0.5, rely=0.38, anchor="center")
search_year_input.place(relx=0.5, rely=0.46, anchor="center")
search_year_button.place(relx=0.5, rely=0.54, anchor="center")
search_both_button.place(relx=0.5, rely=0.62, anchor="center")
output_box.place(relx=0.5, rely=0.82, anchor="center")
website_label.place(relx=0.5, rely=0.978, anchor="center")

# Bindings
website_label.bind("<Button-1>", visit_freetogame)

# Run main program
root.mainloop()

