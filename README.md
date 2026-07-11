# RockyBot: News Research Tool

RockyBot is a Streamlit-based news research assistant for extracting insights from online articles. Enter article URLs, process the content into embeddings, and ask questions to receive answers with source references.

## Features

- Load and process article URLs using `UnstructuredURLLoader`.
- Split text and build embeddings with OpenAI embeddings.
- Index content using FAISS for fast similarity search.
- Ask natural language questions and receive answers with source context.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/satyarajdaniel/News_Research_Tool.git
```

2. Change into the project folder:

```bash
cd News_ResearchProject
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:

```bash
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the app:

```bash
streamlit run main.py
```

2. In the browser:

- Enter up to three news URLs in the sidebar.
- Click **Process URLs** to fetch, split, embed, and index the content.
- Ask a question in the query box.
- View the answer and source references returned by the model.

## Notes

- The FAISS index is saved under `my_vector_index/`.
- If the index exists, the app will reuse it for queries.
- The app currently uses the OpenAI `ChatOpenAI` model and `OpenAIEmbeddings`.

## Project Files

- `main.py` — Streamlit application.
- `requirements.txt` — Python dependencies.
- `my_vector_index/` — Local FAISS index storage.
- `.env` — Local environment variables for secrets.

## Example URLs

You can test with news URLs like:

- `https://www.moneycontrol.com/news/business/markets/tata-asset-management-announces-leadership-transition-anand-vardarajan-appointed-ceo-md-13971087.html`
- `https://www.moneycontrol.com/news/business/markets/sk-hynix-indicated-to-climb-21-after-26-5-billion-adr-offering-13971198.html`
- `https://www.moneycontrol.com/news/business/markets/quant-mf-buys-ethos-shares-worth-rs-175-crore-bofa-acquires-rs-385-crore-shares-in-kalyan-jewellers-13971218.html`
