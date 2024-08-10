
## Web Crawler Project
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

class WebCrawler:
    def _init_(self, base_url, max_depth):
        self.base_url = base_url
        self.max_depth = max_depth
        self.visited_urls = set()

    def crawl(self):
        self._crawl(self.base_url, 0)

    def _crawl(self, url, depth):
        if depth > self.max_depth or url in self.visited_urls:
            return

        print(f"Crawling: {url} at depth: {depth}")
        self.visited_urls.add(url)

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract and follow all links
        for link in soup.find_all('a', href=True):
            full_url = urljoin(url, link['href'])
            if full_url.startswith(self.base_url):  # Only follow links within the base domain
                self._crawl(full_url, depth + 1)

        time.sleep(1)  # Be polite and avoid overwhelming the server

if _name_ == "_main_":
    base_url = "http://example.com"  # Replace with the starting URL
    max_depth = 2  # Define how deep the crawler should go

    crawler = WebCrawler(base_url, max_depth)
    crawler.crawl()
