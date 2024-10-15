from bs4 import BeautifulSoup
import os

# Read the existing HTML file
with open('index.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Function to create or update a section
def create_or_update_section(id, title, image_path, image_alt):
    section = soup.find('section', id=id)
    if not section:
        section = soup.new_tag('section', id=id)
        soup.main.append(section)
    
    section.clear()
    
    h2 = soup.new_tag('h2')
    h2.string = title
    section.append(h2)
    
    img = soup.new_tag('img', src=image_path, alt=image_alt, **{'class': f'{id}-image'})
    section.append(img)

# Update or create sections
create_or_update_section('profile', 'Profile', 'path/to/image1.jpg', 'Profile picture')
create_or_update_section('trading', 'Trading Expertise', 'path/to/image2.jpg', 'Trading concept')
create_or_update_section('analytics', 'Analytics Dashboard', 'path/to/image3.jpg', 'Analytics dashboard')

# Save the modified HTML
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(str(soup.prettify()))

print("HTML file has been updated with the new images.")