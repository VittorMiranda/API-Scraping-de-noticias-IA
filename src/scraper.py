import requests
from bs4 import BeautifulSoup

def coletar_noticias():
    urls = [
        "https://www.google.com/search?q=(\"Artificial+Intelligence\"+OR+AI+OR+\"Machine+Learning\"+OR+\"Deep+Learning\")+AND+(China+OR+USA+OR+\"United+States\"+OR+Europe+OR+\"European+Union\")+AND+(health+OR+finance+OR+education+OR+robotics+OR+automotive+OR+\"supply+chain\")+-video+-game&tbs=qdr:d&tbm=nws&num=100&start=0",
        "https://www.google.com/search?q=(\"Artificial+Intelligence\"+OR+AI+OR+\"Machine+Learning\"+OR+\"Deep+Learning\")+AND+(China+OR+USA+OR+\"United+States\"+OR+Europe+OR+\"European+Union\")+AND+(health+OR+finance+OR+education+OR+robotics+OR+automotive+OR+\"supply+chain\")+-video+-game&tbs=qdr:d&tbm=nws&num=100&start=101",
        "https://www.google.com/search?q=Artificial+Intelligence&tbs=qdr:d&tbm=nws&num=100",
        "https://www.google.com/search?q=Artificial+Intelligence&tbs=qdr:d&tbm=nws&num=101"
    ]

    noticias = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }

    for url in urls:
        resposta = requests.get(url, headers=headers, timeout=10)
        if resposta.status_code != 200:
            noticias.append({"erro": f"Não foi possível acessar {url}"})
            continue

        soup = BeautifulSoup(resposta.text, "html.parser")

        for item in soup.find_all("a", href=True):
            href = item['href']
            if not href.startswith("http"):
                continue

            titulo = item.get_text(strip=True)

            # Resumo: geralmente aparece em um <div> logo após o link
            resumo_tag = item.find_next("div", class_="GI74Re nDgy9d")
            resumo = resumo_tag.get_text(strip=True) if resumo_tag else None

            if titulo:
                noticias.append({
                    "titulo": titulo,
                    "link": href,
                    "resumo": resumo
                })

    return noticias

# Exemplo de uso
resultado = coletar_noticias()
print(f"Foram coletadas {len(resultado)} notícias")
for n in resultado[:5]:  # mostrar apenas 5 primeiras
    print(n)