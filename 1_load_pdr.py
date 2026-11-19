
from langchain_community.document_loaders import (
    PyPDFLoader,
    WebBaseLoader
)
from langchain_text_splitters import (
        CharacterTextSplitter,
        RecursiveCharacterTextSplitter
        )

from langchain_ollama import OllamaEmbeddings

from langchain_chroma import Chroma
# -------------------------------
# 1. Load PDF document
# -------------------------------

loader = PyPDFLoader("Swamy_Sai_Resume_Updated_HELIOS_RAG.pdf")

docs = loader.load()

print("=" * 60)

# -------------------------------
# 2. Load Web document
# -------------------------------

urls = [
    "https://en.wikipedia.org/wiki/MS_Dhoni",
    "https://en.wikipedia.org/wiki/Sachin_Tendulkar",
    "https://en.wikipedia.org/wiki/Virat_Kohli",
    "https://en.wikipedia.org/wiki/Rohit_Sharma",
]

wiki = WebBaseLoader(urls)
w = wiki.load()
all_docs = docs+w

'''
splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size = 50,
        chunk_overlap=10
        )

chunks = splitter.split_documents(all_docs)
'''
'''
for i,chunk in enumerate(chunks):
    print(f"\nchunks {i+1}")
    print(chunk)
'''
print("*"*60)

s = RecursiveCharacterTextSplitter(
        chunk_size = 50,
        chunk_overlap=10
        )

rch = s.split_documents(all_docs)
'''
for i,c in enumerate(rch):
    print(f"\nchunks {i+1}")
    print(c)

'''

embeddings = OllamaEmbeddings(
        model = "nomic-embed-text"
        )


text = [s.page_content for s in rch]

vector = embeddings.embed_documents(
        text
        )

print(type(vector))
print(len(vector))
print(vector[:20])

vectorstore = Chroma.from_documents(
        documents = rch,
        embedding=embeddings,
        collection_name="helios_documents",
        persist_directory="./chroma_db"
        
        )

print("Data stored in chromaDB")
