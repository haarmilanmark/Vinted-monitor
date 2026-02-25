import requests
import os

# Discord webhook a GitHub Secret-ből
WEBHOOK = os.environ["DISCORD_WEBHOOK"]

# Te Vinted linked
URL = "https://www.vinted.hu/catalog?catalog[]=1242&currency=HUF&order=newest_first&page=1&size_ids[]=780&size_ids[]=781&size_ids[]=782&size_ids[]=783&size_ids[]=784&size_ids[]=785&size_ids[]=786&size_ids[]=787&size_ids[]=788&brand_ids[]=14&brand_ids[]=53&brand_ids[]=2703&price_from=0&price_to=6000&status_ids[]=6&status_ids[]=1&status_ids[]=2"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# Lekérjük a Vinted JSON adatokat
r = requests.get(URL, headers=headers)
data = r.json()

# Végigmegyünk az összes hirdetésen
for item in data.get("items", []):
    title = item.get("title", "N/A")
    price = item.get("price", {}).get("amount", "N/A")
    currency = item.get("price", {}).get("currency", "HUF")
    link = item.get("url")
    # Az első kép linkje
    photo = item.get("photos", [{}])[0].get("url_fullxfull", "")

    # Discord üzenet formázás
    content = f"🆕 **{title}**\n💰 {price} {currency}\n🔗 {link}\n{photo}"

    # Küldés a Discord webhookra
    requests.post(WEBHOOK, json={"content": content})
