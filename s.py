from bs4 import BeautifulSoup
import json
import os

# Path to your local HTML file
file_path = "src_data_a.html"  # Replace with your file path

# Read the HTML file content
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

# Extract product data
products = []

# Find all <div class="sp-box">
for item in soup.find_all('div', class_='sp-box'):
    # Extract image URL and convert it to a local path using only the file name
    image_url = item.find('img', class_='sp-pic')['src']
    filename = os.path.basename(image_url)
    image = "img/" + filename
    
    # Extract title and remove "Daily income Daily withdrawal" if present
    product_name = item.find('div', class_='title').text.strip()
    product_name = product_name.replace("Daily income Daily withdrawal", "").strip()
    
    # Extract other details from <ul><li>
    details = item.find('div', class_='wrap').find_all('li')
    price = details[0].find_all('span')[1].text.replace(':', '').strip()
    daily_income = details[1].find_all('span')[1].text.replace(':', '').strip()
    total_return = details[2].find_all('span')[1].text.replace(':', '').strip()
    duration = details[3].find_all('span')[1].text.replace(':', '').strip()
    
    # Check for the Pre-Sale status
    status_obj = {}
    pre_button = item.find('button', class_="btn-style yus")
    status_obj["pre"] = True if pre_button and "Pre-Sale" in pre_button.text else False
    
    # Append the extracted data along with status to the list
    products.append({
        'name': product_name,
        'price': price,
        'daily_income': daily_income,
        'total_return': total_return,
        'duration': duration,
        'image': image,
        'status': status_obj
    })

# Convert to JSON and save to a file
with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=4, ensure_ascii=False)

print("✅ Data extracted and saved to 'products.json'")
