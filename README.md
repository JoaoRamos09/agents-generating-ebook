# Sistema de Agentes de IA para Criação de eBooks

## Descrição do Projeto

Este é um sistema de **IA Agentics** desenvolvido para criar uma estrutura inicial de um eBook com base em um tema fornecido pelo usuário. A aplicação utiliza buscas na internet para coletar informações relevantes, organizando-as de forma estruturada em capítulos e seções, facilitando o desenvolvimento do conteúdo pelo usuário, ele poderá escolher a quantidade máxima de capítulos.

Um dos diferenciais deste projeto é seu formato modularizado, fugindo do modelo tradicional baseado em notebooks. Essa abordagem garante maior escalabilidade, organização do código e facilidade de integração com outras ferramentas e fluxos de trabalho. 

## Funcionalidades

- **Busca automatizada de informações**: O sistema realiza consultas na internet para encontrar conteúdos relacionados ao tema proposto, priorizando fontes relevantes e confiáveis.
- **Geração de estrutura inicial de eBook**: A IA organiza os dados coletados em uma estrutura lógica, com capítulos e seções sugeridos.
- **Modularização**: O projeto é desenvolvido com uma arquitetura modular, permitindo fácil manutenção, extensão e reutilização de componentes em diferentes aplicações.
- **Personalização**: O usuário pode ajustar a estrutura gerada de acordo com suas necessidades, incluindo ou excluindo tópicos conforme o contexto.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Framework de Agentes**: Langchain, Langgraph;
- **Framework de Tracing**: Langsmith
- **Bibliotecas Relevantes**: 
  - Para Web Scraping: duckduckgo-search
- **Arquitetura Modular**: Implementada com pacotes Python, visando organização e escalabilidade.

## Como Usar

1. Clone este repositório:  
   ```bash
   git clone https://github.com/JoaoRamos09/agents-generating-ebook.git
   cd agents-generating-ebook
   ```

2. Instale as depêndecias:
   ```bash
   pip install -r requirements.txt

3. Insira as variáveis de ambiente;

4. Execute o sistema:
    ```bash
    python main.py

   