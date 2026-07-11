import os
import streamlit as st
import pickle
import time
import langchain
from langchain_openai import ChatOpenAI
from langchain_classic.chains import RetrievalQAWithSourcesChain
from langchain_classic.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from unstructured import documents

from dotenv import load_dotenv
load_dotenv()  

st.title("RockyBot: News Research Tool 📈")
st.sidebar.title("News Article URLs")


urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")

main_placeholder = st.empty()
llm = ChatOpenAI(temperature=0.9, max_tokens=500) 

if process_url_clicked:
    # load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()
    # split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Data Splitting...Started...✅✅✅")
    docs = text_splitter.split_documents(data)

    # Create your vector index
    main_placeholder.text("Creating Vector Index...Started...✅✅✅")
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    vectorstore_openai.save_local("my_vector_index")
    vectorstore_openai = FAISS.load_local(
    "my_vector_index", 
    embeddings,
    allow_dangerous_deserialization=True)

query = main_placeholder.text_input("Question: ")
vector_index_dir = "./my_vector_index"
if query:
    if os.path.exists(os.path.join(vector_index_dir, "index.faiss")):
        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.load_local(
            vector_index_dir,
            embeddings,
            allow_dangerous_deserialization=True,
        )
        chain = RetrievalQAWithSourcesChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(),
            return_source_documents=True,
        )
        result = chain({"question": query}, return_only_outputs=True)

        st.header("Answer")
        st.write(result.get("answer", ""))

        sources = (result.get("sources") or "").strip()
        if sources:
            st.subheader("Sources:")
            sources_list = [line.strip() for line in sources.split("\n") if line.strip()]
            for source in sources_list:
                st.write(source)
        else:
            source_docs = result.get("source_documents") or []
            if source_docs:
                st.subheader("Source documents")
                for doc in source_docs:
                    st.write(doc.metadata.get("source", doc.metadata))
            else:
                st.warning("No sources were returned by the chain.")
    else:
        st.warning("No saved FAISS index found. Please process URLs first.")

        
  


