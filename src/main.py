from amazon_scraper import AmazonScraper
from email_handler import EmailHandler
import csv

scraper = AmazonScraper()
email_sender = EmailHandler()
data_file = "./data/Amazon Price Tracker.csv"
with open(data_file) as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        product_title = row["Product Description"]
        url = row["Product URL"]
        strike_price = float(row["Strike Price ($)"])
        current_price = scraper.get_price(url)
        # print(f"Product name: {product_title}")
        # print(f"Current Price: ${current_price}")
        # print(f"Strike price: ${strike_price}")
        if current_price < strike_price:
            message = f"Buy {product_title} now! It is only ${current_price}"
            email_sender.send_price_notification(message=message)
