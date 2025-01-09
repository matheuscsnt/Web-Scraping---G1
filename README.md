# Web Scraping de Matéria do G1

Este projeto realiza um web scraping de uma matéria publicada no site do G1. O objetivo é extrair informações relevantes, como título, subtítulo, autor, data de publicação e conteúdo da matéria, e salvá-las em um arquivo JSON limpo e organizado.

## Ferramentas Utilizadas

- **Linguagem**: Python
- **Bibliotecas**:
  - `requests`: Para realizar requisições HTTP e obter o código HTML da página.
  - `BeautifulSoup` (da biblioteca `bs4`): Para fazer o parsing do HTML e navegar pelo conteúdo da página.
  - `json`: Para salvar os dados extraídos em um arquivo JSON.
  - `re` (Regex): Para realizar a limpeza e organização dos dados.

## Funcionalidades do Código

### 1. Scraping da Matéria
A função `scrape_g1_article(url)` realiza as seguintes etapas:
- Faz uma requisição HTTP à URL da matéria do G1 usando `requests`.
- Analisa o HTML retornado com o `BeautifulSoup`.
- Extrai as seguintes informações:
  - **Título**: A partir da tag `<h1>` com a classe `content-head__title`.
  - **Subtítulo**: A partir da tag `<h2>` com a classe `content-head__subtitle`.
  - **Autor da matéria**: A partir da tag `<span>` com a classe `content-publication-data__from`.
  - **Data de publicação**: A partir da tag `<time>` com a classe `content-publication-data__updated`.
  - **Conteúdo**: Todos os parágrafos do conteúdo principal, extraídos da tag `<p>`.

Os dados são organizados em um dicionário com as seguintes chaves:
- `Título`
- `Subtítulo`
- `Autor da matéria`
- `Data de publicação`
- `Conteúdo`

### 2. Limpeza dos Dados
A função `clean_article_data(article_data)` utiliza regex para:
- Remover espaços desnecessários e caracteres redundantes nos valores dos dados.
- Assegurar que os dados estejam formatados e prontos para serem salvos.

### 3. Salvando os Dados
Os dados limpos são salvos em um arquivo JSON chamado `g1_article_cleaned.json`. O arquivo é codificado em UTF-8 para garantir a compatibilidade com caracteres especiais.

## Como Executar o Código

1. **Instale as dependências**:
   Certifique-se de que as bibliotecas `requests`, `bs4` e `re` estejam instaladas. Caso não estejam, use o comando abaixo para instalar:
   ```bash
   pip install requests beautifulsoup4
   ```

2. **Defina a URL da Matéria**:
   Verifique se a URL atribuída à variável `BASE_URL` corresponde à página desejada.

3. **Execute o Script**:
   Rode o código Python para realizar o scraping e salvar os dados:
   ```bash
   python nome_do_arquivo.py
   ```

4. **Verifique o Arquivo JSON**:
   Ao final da execução, os dados extraídos estarão no arquivo `g1_article_cleaned.json`, localizado no mesmo diretório do script.

## Estrutura do JSON Gerado
O arquivo JSON gerado terá o seguinte formato:
```json
{
    "Título": "Título da matéria",
    "Subtítulo": "Subtítulo da matéria",
    "Autor da matéria": "Nome do autor",
    "Data de publicação": "2025-01-09T00:00:00",
    "Conteúdo": "Texto completo da matéria."
}
```

## Considerações Finais
Este projeto foi desenvolvido como exemplo de web scraping simples, focado na extração de conteúdo textual de uma página web. Ele pode ser adaptado para outros sites e formatos, desde que respeitadas as políticas de uso do site alvo.