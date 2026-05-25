import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):

    try:

        headers = {

            "User-Agent":
            "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        soup = BeautifulSoup(
            response.text,
            'html.parser'
        )

        paragraphs = soup.find_all('p')

        text = ""

        for p in paragraphs[:20]:

            text += p.get_text() + " "

        if text.strip() == "":

            return "No meaningful article content found."

        return text

    except Exception as e:

        return f"URL analysis failed: {str(e)}"