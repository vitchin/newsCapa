# unknowProject

Este projeto é um agregador de notícias que utiliza a NewsAPI.

## Como rodar localmente

1. Instale as dependências:
   ```bash
   pip install flask requests
   ```
2. Execute o aplicativo:
   ```bash
   python main.py
   ```

## Implantação no GitHub Pages

Para hospedar este projeto no GitHub Pages, você precisa converter o aplicativo Flask em um site estático.

1. Instale o Frozen-Flask:
   ```bash
   pip install Frozen-Flask
   ```
2. Gere os arquivos estáticos:
   ```bash
   python freeze.py
   ```
   Isso criará uma pasta `build/` com o site estático.
3. Envie o conteúdo da pasta `build/` para a branch `gh-pages` do seu repositório GitHub.
