import bs4, os
import smtplib
import requests

rtx4060_url = "https://www.amazon.com.br/Galax-Rtx4060-128Bits-1-Click-46Nsl8Md8Loc/dp/B0CB3RBW68/"
sender = os.environ.get("SENDER")
sender_pass = os.environ.get("SENDER_PASS")
receiver = os.environ.get("RECEIVER")

# web scraping
http_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "pt-BR,pt;q=0.9",

}
response = requests.get(url=rtx4060_url, headers=http_headers)
soup = bs4.BeautifulSoup(response.text, "html.parser")
price_whole = soup.find("span", class_="a-price-whole").getText().replace(",", "").replace(".", "")
price_fraction = soup.find("span", class_="a-price-fraction").getText()
price = float(price_whole) + float(price_fraction)/100

# send email
if price < 2000:
    with smtplib.SMTP("smtp.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender, password=sender_pass)
        connection.sendmail(
            from_addr=sender,
            to_addrs=receiver,
            msg=f"Subject:Amazon Price Alert!\n\n"
                f"Rtx 4060 Galax 8GB is now {price}"
        )
