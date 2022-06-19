import requests
from PyPDF2 import PdfReader

reader = PdfReader("extract.pdf")
page = reader.pages[0]
text = page.extract_text()


API_KEY = "9b9605052b35475e9ff252fcd9afc44c"
URL_ENDPOINT = "http://api.voicerss.org/"
PARAMS = {
    "key": API_KEY,
    "hl": "en-us",
    "src": f"{text}"
}

response = requests.get(URL_ENDPOINT, params=PARAMS)

with open('audio.mp3', 'wb') as f:
    f.write(response.content)

