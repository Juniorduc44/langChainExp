from dotenv import find_dotenv, load_dotenv
from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
load_dotenv(find_dotenv())
embeddings = OpenAIEmbeddings()


loader = YoutubeLoader.from_youtube_url(input("Enter a youtube url: "))
transcript = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(transcript)

db = FAISS.from_documents(docs, embeddings)



print("These are the documents:")
print(docs)
print("\n\n")
print("This is the Database:\n")
print(db)

