#web-scraping con HTTPX e SELECTOLAX

import httpx
from selectolax.parser import HTMLParser

#settiamo il sito da cui estrarre i dati
url = "https://www.rei.com/c/camping-and-hiking/f/scd-deals"

#ogni PC ha il suo user-agent, per trovarlo cerca sul web "my user-agent" 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'}

#carichiamo la pagina web con HTTPX, più efficiente e moderno di beautifulsoup e analizziamo (parse) la pagina html con selectolax in modo da trasformarla in testo 
resp = httpx.get(url, headers=headers)
html = HTMLParser(resp.text) #html rappresenta un oggetto HTMLParser che a sua volta rappresenta la pagina HTML da cui estrarre i dati 

#creiamo una funzione per estrarre i dati desiderati prevedendo che in caso di errore o dato non trovato la funzione ritorni "None" dove:
#sel rappresenta il selettore CSS che verrà utilizzato per trovare l'elemento HTML da cui estrarre il testo.
def extract_text(html, sel):
    try: 
      return html.css_first(sel).text()
    except Attributeerror:
      return None

#nel sito di riferimento tutti i prodotti sono dettagliati all'interno di uno specifico box definito come: <li class ="Xpx0MUGhB7jSm5UvK2EY">. Pertanto:
products = html.css("li.VcGDfKKy_dvNbxUqm29K")

for product in products:
  item = {
      "name": extract_text(product, ".Xpx0MUGhB7jSm5UvK2EY"),#per estrarre il nome posso far riferimento alla classe. Il punto davanti al nome della classe indica che il selettore CSS deve cercare un elemento HTML con la classe specificata
      "name1": extract_text(product, "span[data-ui=product-title]"),#per estrarre il nome posso far riferimento anche al nome dello span che va però inserito tra []
      "price": extract_text(product, "span[data-ui=sale-price]"),
  }
  print(item)
