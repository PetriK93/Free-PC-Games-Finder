import requests
import webbrowser

# API endpoint for free PC games
url_pc_platform = "https://www.freetogame.com/api/games?platform=pc"

# Send a get request to the API
response = requests.get(url_pc_platform)

# Parse json into python format
data = response.json()

# Clear text from the output_box
def clear_output(output_box):
    output_box.configure(state="normal")
    output_box.delete("1.0", "end")
    output_box.configure(state="disabled")


# Enable writing mode temporarily for output_box
def write_output(output_box, text):
    output_box.configure(state="normal")
    output_box.insert("end", text + "\n")
    output_box.see("end")
    output_box.configure(state="disabled")


# Search PC games by genre
def search_genre(output_box, genre):

    # Clear previous text
    clear_output(output_box)

    # Counter for indexing
    count = 0

    for entry in data:

        release_date = entry["release_date"]
        release_year = int(release_date.split("-")[0])

        if entry["genre"] == genre:
            count += 1
            write_output(output_box, f"{count}. {entry['title']} - {release_year}")
            print(f"{count}. {entry['title']}")

    if count == 0:
        write_output(output_box, "No results found.")
        print("No results found.")


# Search PC games by year
def search_year(output_box, year):

    # Clear previous text
    clear_output(output_box)

    # Counter for indexing
    count = 0

    for entry in data:

        release_date = entry["release_date"]
        release_year = int(release_date.split("-")[0])

        if year == release_year:
            count += 1
            write_output(output_box, f"{count}. {entry['title']} - {release_year}")
            print(f"{count}. {entry['title']} - {release_year}")

    if count == 0:
        write_output(output_box, "No results found.")
        print("No results found.")


# Search PC games by genre & year
def search_both(output_box, genre, year):

    # Clear previous text
    clear_output(output_box)

    # Counter for indexing
    count = 0

    for entry in data:

        search_genre = entry["genre"]
        release_date = entry["release_date"]
        release_year = int(release_date.split("-")[0])

        if genre == search_genre and year == release_year:
            count += 1
            write_output(output_box, f"{count}. {entry['title']} - {release_year}")
            print(f"{count}. {entry['title']} - {release_year}")

    if count == 0:
        write_output(output_box, "No results found.")
        print("No results found.")


# Direct user to the API provider's website
def visit_freetogame(event):
    webbrowser.open("https://www.freetogame.com")