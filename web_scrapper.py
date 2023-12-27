import requests
from bs4 import BeautifulSoup
import csv


# Function to scrape data from a website
def scrape_website(url):
    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data from the HTML using BeautifulSoup
        # (Replace this part with the actual HTML structure of the website)
        data_list = []
        for item in soup.find_all('div', class_='example-class'):
            # Extract specific data from each item
            title = item.find('h2').text.strip()
            description = item.find('p').text.strip()

            # Append the data to the list
            data_list.append({'Title': title, 'Description': description})

        return data_list
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None


# Function to write data to a CSV file
def write_to_csv(data, filename):
    # Specify the CSV file header
    fieldnames = ['Title', 'Description']

    # Write data to the CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write the data
        writer.writerows(data)


# URL of the website to scrape
target_url = 'https://example.com'

# Scrape data from the website
scraped_data = scrape_website(target_url)

# Check if data was successfully scraped
if scraped_data:
    # Specify the filename for the CSV file
    csv_filename = 'scraped_data.csv'

    # Write the scraped data to a CSV file
    write_to_csv(scraped_data, csv_filename)

    print(f"Data successfully scraped and saved to {csv_filename}")
else:
    print("No data to save.")
