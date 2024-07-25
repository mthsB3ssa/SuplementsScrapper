# SuplementsScrapper

## Visão Geral
SuplementsScrapper é um projeto de web scraping projetado para extrair dados de vários sites de suplementos. O objetivo é coletar informações sobre diferentes suplementos, incluindo preços, ingredientes e avaliações, e armazenar esses dados em um formato estruturado para análise.

## Funcionalidades
- **Web Scraping:** Coleta dados de diversos sites de suplementos.
- **Armazenamento de Dados:** Armazena os dados raspados em um formato estruturado.
- **Suporte Docker:** Inclui um Dockerfile e docker-compose para fácil configuração e implantação.

## Requisitos
- Python 3.8+
- Docker

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/mthsB3ssa/SuplementsScrapper.git
    cd SuplementsScrapper
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute com Docker:
    ```bash
    docker-compose up
    ```

## Uso
1. Configure os sites alvo e os parâmetros de scraping no arquivo `src/config.py`.
2. Execute o scraper:
    ```bash
    python src/main.py
    ```

## Contribuição
1. Faça um fork do repositório.
2. Crie um novo branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Faça suas alterações e comite-as:
    ```bash
    git commit -m "Descrição das alterações"
    ```
4. Faça push para o branch:
    ```bash
    git push origin feature-branch
    ```
5. Abra um pull request.

## Licença
Este projeto é licenciado sob a licença MIT.

## Contato
Para quaisquer dúvidas ou problemas, entre em contato com os mantenedores do projeto via GitHub.
