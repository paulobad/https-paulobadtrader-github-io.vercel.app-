import os
from bs4 import BeautifulSoup

def update_html_file(file_name, title, main_content):
    with open(file_name, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Update title
    soup.title.string = f"{title} - EDGARD TRADER AND DEVELOPER"

    # Update main content
    main = soup.find('main')
    main.clear()
    h1 = soup.new_tag('h1')
    h1.string = main_content
    main.append(h1)

    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(str(soup.prettify()))

# Update all pages
pages = [
    ('index.html', 'Home', 'Welcome to Edgard Trader and Developer'),
    ('skills.html', 'Skills', 'My Skills'),
    ('projects.html', 'Projects', 'My Projects'),
    ('about.html', 'About', 'About Me'),
    ('contact.html', 'Contact', 'Contact Me'),
    ('download.html', 'Download', 'Downloads')
]

for page in pages:
    update_html_file(*page)

print("HTML files have been updated.")