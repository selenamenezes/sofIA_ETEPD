<h1 align="center">sofIA 🤖</h1>

<p align="center">
  Um agente de Inteligência Artificial inteligente e contextualizado, construído com arquitetura RAG (Retrieval-Augmented Generation).
</p>

<p align="center">
  <a href="#-sobre-o-projeto">Sobre</a> •
  <a href="#-tecnologias">Tecnologias</a> •
  <a href="#-funcionalidades">Funcionalidades</a> •
  <a href="#-como-executar">Como executar</a> •
  <a href="#-estrutura-do-projeto">Estrutura</a> •
  <a href="#-autores">Autores</a>
</p>

---

## 📌 Sobre o Projeto

O projeto **sofIA** é um agente de Inteligência Artificial desenvolvido para interagir, compreender e fornecer informações com alto nível de precisão. 

O diferencial da sofIA é a implementação da arquitetura **RAG (Retrieval-Augmented Generation)**, que permite ao modelo de linguagem buscar dados armazenados localmente num banco de dados **SQLite** antes de gerar a sua resposta. Isso reduz as alucinações da IA e permite que o sistema ofereça respostas baseadas num contexto de dados específicos.

Repositório Oficial: [https://github.com/selenamenezes/sofIA_ETEPD](https://github.com/selenamenezes/sofIA_ETEPD)

## 🛠 Tecnologias

As seguintes ferramentas e tecnologias foram utilizadas na construção deste projeto:

- **[Python](https://www.python.org/)**: Linguagem de programação principal utilizada no backend e manipulação de dados.
- **RAG (Retrieval-Augmented Generation)**: Técnica de inteligência artificial que combina a recuperação de informações (retrieval) com a geração de textos, garantindo respostas embasadas em dados específicos fornecidos.
- **[SQLite](https://www.sqlite.org/index.html)**: Banco de dados relacional leve e embutido utilizado para armazenar e organizar os documentos de contexto consumidos pelo sistema.

## ⚙️ Funcionalidades

- **Interação Conversacional:** Interface (ou CLI) para perguntas e respostas com a agente sofIA.
- **Busca Semântica/Lexical:** Acesso à base de dados para recuperar as informações mais relevantes antes da geração da resposta.
- **Armazenamento Otimizado:** Utilização do SQLite de forma ágil para guardar a base de conhecimento sem a necessidade de instâncias de bancos de dados pesados.
- **Respostas Precisas:** Redução drástica das "alucinações" do LLM graças ao pipeline de RAG.

## 🚀 Como executar

### Pré-requisitos

Antes de começar, vai precisar de ter instalado na sua máquina o [Python 3.8+](https://www.python.org/downloads/) e o [Git](https://git-scm.com).

### Passo a passo

1. **Clone este repositório**
    ```bash
   git clone [https://github.com/selenamenezes/sofIA_ETEPD.git](https://github.com/selenamenezes/sofIA_ETEPD.git)

   Acesse a pasta do projeto no seu terminal/cmd ```

```Bash 
cd sofIA_ETEPD
Crie e ative um ambiente virtual (Altamente Recomendado)
```

```Bash
# Windows
python -m venv venv
.\venv\Scripts\activate
```

```Bash
# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
Instale as dependências
```

 ```Bash
pip install -r requirements.txt
Inicie a aplicação
```

```Bash
python main.py
(Substitua main.py pelo nome correto do arquivo principal, caso seja diferente).
```

## 📁 Estrutura do Projeto (Exemplo)
```Bash
Plaintext
sofIA_ETEPD/
├── data/               # Banco de dados SQLite e arquivos base
├── src/                # Código-fonte da aplicação (RAG, integrações)
├── requirements.txt    # Bibliotecas Python necessárias
├── README.md           # Documentação do projeto
└── main.py             # Arquivo para executar a IA
```
## 👩‍💻 Autores
@selenamenezes
