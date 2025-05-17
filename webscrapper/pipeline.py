from url_collector import collect_urls
from scraper import scrape_site
from store import save_to_mongo

# queries = {
#     "food": [
#         "",
#         "top food delivery business sites"
#     ],
#     "ecommerce": [
#         "top ecommerce websites 2024",
#         "popular clothing ecommerce"
#     ]
# }


# food_urls = [
# ]

ecommerce_urls = [
    "https://www.target.com",               # General retail
    "https://www.costco.com",               # Bulk retail, warehouse model
    "https://www.newegg.com",               # Tech & electronics
    "https://www.bhphotovideo.com",         # Pro electronics & photo gear
    "https://www.wayfair.com",              # Home furniture and decor
    "https://www.ikea.com",                 # Furniture with flat-pack UX
    "https://www.overstock.com",            # Discounted furniture and more
    "https://www.sephora.com",              # Beauty & cosmetics
    "https://www.ulta.com",                 # Beauty, skincare, haircare
    "https://www.glossier.com",             # Minimalist direct-to-consumer beauty
    "https://www.myntra.com",               # Indian fashion ecommerce
    "https://www.flipkart.com",             # Indian general ecommerce (Walmart-owned)
    "https://www.farfetch.com",             # Luxury designer fashion
    "https://www.ssense.com",               # Luxury & streetwear ecommerce
    "https://www.revolve.com",              # Fashion boutique brand
    "https://www.allbirds.com",             # Eco-friendly footwear
    "https://www.warbyparker.com",          # Eyewear and glasses
    "https://www.blueapron.com",            # Meal kit delivery ecommerce
    "https://www.chewy.com",                # Pet supplies and products
    "https://www.made.com"
]


def run_pipeline():
    # for url in food_urls:
    #     print(f"\nScraping FOOD: {url}")
    #     data = scrape_site(url)
    #     save_to_mongo(data, "food")

    for url in ecommerce_urls:
        print(f"\nScraping ECOMMERCE: {url}")
        data = scrape_site(url)
        save_to_mongo(data, "ecommerce")

if __name__ == "__main__":
    run_pipeline()