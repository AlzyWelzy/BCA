import requests
import os
from bs4 import BeautifulSoup

# Base URL for the series
base_url = "https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/data-structures-and-algorithms-in-hindi-"

# Create a directory to store the downloaded files
os.makedirs("content", exist_ok=True)

# Iterate over the range of numbers from 1 to 92
for i in range(1, 93):
    # Construct the URL for the current iteration
    url = base_url + str(i) + "/"

    # Send an HTTP request to the website and store the response
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the `a` tags
    download_links = soup.find_all("a")

    # Iterate over the download links
    for link in download_links:
        # Check if the link has a "href" attribute
        if "href" in link.attrs:
            # Extract the URL of the link
            file_url = link["href"]

            # Check if the URL is not the link to the parent directory
            if file_url != "../":
                # Check if the URL ends with a JPG, WEBP, or PDF file extension
                if file_url.endswith(".jpg") or file_url.endswith(".webp") or file_url.endswith(".pdf"):
                    # Check if the URL starts with the API URL
                    if file_url.startswith("https://api.codewithharry.com"):
                        # Send an HTTP request to the link and store the response
                        file_response = requests.get(file_url)

                        # Check if the request was successful
                        if file_response.ok:
                            # Extract the file name from the URL
                            file_name = file_url.split("/")[-1]

                            # Save the file to the content directory
                            with open(os.path.join("content", file_name), "wb") as f:
                                f.write(file_response.content)
