import requests
from bs4 import BeautifulSoup
import json
import re

# URL da matéria
BASE_URL = "https://g1.globo.com/economia/noticia/2025/01/09/fiscalizacao-da-receita-por-que-emprestar-o-cartao-de-credito-pode-virar-um-problema.ghtml"

# Função para fazer o scraping
def scrape_g1_article(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Erro ao acessar a página: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, "html.parser")

    # Extrair título da matéria
    title = soup.find("h1", class_="content-head__title")
    title_text = title.text.strip() if title else ""

    # Extrair subtítulo
    subtitle = soup.find("h2", class_="content-head__subtitle")
    subtitle_text = subtitle.text.strip() if subtitle else ""

    # Extrair autor
    author = soup.find("span", class_="content-publication-data__from")
    author_text = author.text.strip() if author else ""

    # Extrair data de publicação
    publication_date = soup.find("time", class_="content-publication-data__updated")
    publication_date_text = publication_date["datetime"] if publication_date else ""

    # Extrair conteúdo da matéria
    paragraphs = soup.find_all("p", class_=None)  # Parágrafos do conteúdo principal
    content = "\n".join([p.text.strip() for p in paragraphs if p.text.strip()])

    # Organizar os dados em um dicionário
    article_data = {
        "Título": title_text,
        "Subtítulo": subtitle_text,
        "Autor da matéria": author_text,
        "Data de publicação": publication_date_text,
        "Conteúdo": content
    }

    return article_data

# Função para limpar dados usando regex
def clean_article_data(article_data):
    if not article_data:
        return None

    cleaned_data = {}
    for key, value in article_data.items():
        # Remove múltiplos espaços e caracteres desnecessários
        cleaned_value = re.sub(r"\s+", " ", value).strip()
        cleaned_data[key] = cleaned_value

    return cleaned_data

# Executando o script para coletar os dados
data = scrape_g1_article(BASE_URL)

if data:
    # Limpar os dados com regex
    cleaned_data = clean_article_data(data)

    # Salvar os dados limpos em um arquivo JSON
    with open("G1_Fiscalizacao_da_receita.json", "w", encoding="utf-8") as json_file:
        json.dump(cleaned_data, json_file, ensure_ascii=False, indent=4)
    print("Dados limpos e traduzidos salvos no arquivo 'G1_Fiscalizacao_da_receita.json'.")
else:
    print("Nenhum dado foi coletado.")