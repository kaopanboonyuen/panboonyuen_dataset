import os
import requests
from unsplash.api import Api
from unsplash.auth import Auth
from pathlib import Path
from tqdm import tqdm


class ImageScraper:
    def __init__(self, access_key, secret_key, callback_url):
        """Initializes the Unsplash API client."""
        self.auth = Auth(access_key, secret_key, callback_url)
        self.api = Api(self.auth)

    def download_image(self, url, folder_name, file_name):
        """Download image from a URL and save it to a folder."""
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(f'{folder_name}/{file_name}', 'wb') as f:
                    f.write(response.content)
                print(f"Image saved: {file_name}")
            else:
                print(f"Failed to download {file_name}")
        except Exception as e:
            print(f"Error downloading {file_name}: {e}")

    def fetch_images(self, species, num_images=10):
        """Fetch images from Unsplash for a given species."""
        query = species + ' plant'
        folder_name = species.replace(" ", "_").lower()

        # Create directory if it doesn't exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        photos = self.api.photos.search(query, per_page=num_images)

        for i, photo in tqdm(enumerate(photos['results']), total=num_images, desc=f"Downloading {species} images"):
            image_url = photo['urls']['regular']
            self.download_image(image_url, folder_name, f'{species}_{i + 1}.jpg')

    def scrape_images_for_species(self, species_list, images_per_species=10):
        """Scrape images for multiple plant species."""
        for species in species_list:
            self.fetch_images(species, num_images=images_per_species)


if __name__ == "__main__":
    # Replace with your Unsplash credentials
    access_key = 'YOUR_UNSPLASH_ACCESS_KEY'
    secret_key = 'YOUR_UNSPLASH_SECRET_KEY'
    callback_url = 'YOUR_UNSPLASH_CALLBACK_URL'

    species_list = ["Aloe Vera", "Cactus", "Sunflower", "Rose", "Tulip", 
                    "Daisy", "Lavender", "Orchid", "Basil", "Mint"]
    
    scraper = ImageScraper(access_key, secret_key, callback_url)
    scraper.scrape_images_for_species(species_list, images_per_species=10)