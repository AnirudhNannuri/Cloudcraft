from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import requests

def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def scrape_site(url):
    driver = init_driver()
    driver.set_page_load_timeout(20)
    try:
        driver.get(url)
        time.sleep(5)  # Wait for full page load

        # HTML
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        # CSS links
        css_links = [link['href'] for link in soup.find_all('link', rel='stylesheet') if 'href' in link.attrs]

        # JS links
        js_links = [script['src'] for script in soup.find_all('script') if 'src' in script.attrs]

        # Fetch CSS/JS content
        def fetch_links(links):
            contents = {}
            for link in links:
                if link.startswith("http"):
                    try:
                        res = requests.get(link, timeout=10)
                        contents[link] = res.text
                    except:
                        continue
            return contents

        css_content = fetch_links(css_links)
        js_content = fetch_links(js_links)

        driver.quit()
        return {
            "url": url,
            "html": html,
            "css_files": css_content,
            "js_files": js_content
        }

    except Exception as e:
        driver.quit()
        print(f"❌ Failed to scrape {url}: {e}")
        return None
