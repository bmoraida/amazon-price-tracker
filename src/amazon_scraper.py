from bs4 import BeautifulSoup
import requests
import lxml


class AmazonScraper:
    def __init__(self) -> None:
        pass

    def _get_amazon_product_html(self, url=None, backup=False):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        }
        r = requests.get(url=url, headers=headers)
        if backup:
            with open("telescope.html", "w") as f:
                f.write(r.text)
        return r.text

    def get_price(self, url):
        web_page = self._get_amazon_product_html(url)
        soup = BeautifulSoup(web_page, "lxml")
        price_string = (
            soup.find(id="tp_price_block_total_price_ww")
            .findChild(class_="a-offscreen")
            .text.lstrip("$")
        )
        price_number = float(price_string)

        return price_number
