import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
import threading
import queue
import time

BASE_URL = "https://airsdk.dev/reference/actionscript/3.0/"
START_URLS = [
    "https://airsdk.dev/reference/actionscript/3.0/all-classes.html",
    "https://airsdk.dev/reference/actionscript/3.0/package-summary.html",
    "https://airsdk.dev/reference/actionscript/3.0/class-summary.html",
    "https://airsdk.dev/reference/actionscript/3.0/language-elements.html",
    "https://airsdk.dev/reference/actionscript/3.0/all-index-Symbols.html",
    "https://airsdk.dev/reference/actionscript/3.0/appendices.html",
    "https://airsdk.dev/reference/actionscript/3.0/conventions.html",
]
OUTPUT_DIR = "html-docs"
MAX_WORKERS = 15

visited = set()
visited_lock = threading.Lock()
url_queue = queue.Queue()

for url in START_URLS:
    url_queue.put(url)


def download_page(url):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None


def save_page(url, content):
    parsed_url = urlparse(url)
    rel_path = parsed_url.path.replace("/reference/actionscript/3.0/", "")
    if not rel_path or rel_path == "3.0/":
        rel_path = "index.html"
    elif rel_path.endswith("/"):
        rel_path += "index.html"

    file_path = os.path.join(OUTPUT_DIR, rel_path)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


def worker():
    while True:
        try:
            url = url_queue.get(timeout=10)
        except queue.Empty:
            return

        with visited_lock:
            if url in visited:
                url_queue.task_done()
                continue
            visited.add(url)

        # Check if file already exists to skip re-downloading
        parsed_url = urlparse(url)
        rel_path = parsed_url.path.replace("/reference/actionscript/3.0/", "")
        if not rel_path or rel_path == "3.0/":
            rel_path = "index.html"
        elif rel_path.endswith("/"):
            rel_path += "index.html"
        file_path = os.path.join(OUTPUT_DIR, rel_path)

        if os.path.exists(file_path):
            # Still need to parse it for links if it was just downloaded but not visited in this session
            # However, for simplicity, we'll just download if not in visited.
            # If it exists, we skip downloading but still parse for links.
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except:
                content = None
        else:
            print(f"Crawling ({len(visited)}): {url}")
            content = download_page(url)
            if content:
                save_page(url, content)

        if content:
            soup = BeautifulSoup(content, "html.parser")
            for link in soup.find_all("a", href=True):
                href = link["href"]
                href = href.split("#")[0]
                if not href:
                    continue

                full_url = urljoin(url, href)

                if full_url.startswith(BASE_URL):
                    with visited_lock:
                        if full_url not in visited:
                            url_queue.put(full_url)

        url_queue.task_done()


def crawl():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for _ in range(MAX_WORKERS):
            executor.submit(worker)

    url_queue.join()
    print("Crawling complete.")


if __name__ == "__main__":
    start_time = time.time()
    crawl()
    print(f"Finished in {time.time() - start_time:.2f} seconds")
