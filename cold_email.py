from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import getpass
import chromadb
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate

#setup the model
load_dotenv()


llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0
)

response = llm.invoke("Hello, how are you?")
print(response.content)


#setup a vector database in this case i will use chromadb

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="cold_email")
collection.add(
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges"
    ],
    ids=["id1", "id2"]
)

all_docs = collection.get()

print(all_docs)


# documents = collection.get(ids=["id1"])
# print(documents)

# res = collection.query(
#     query_texts= "orange fruite"
# )

# print(res)


loader = WebBaseLoader("https://careers.jesagroup.com/job/Junior-Associate-Consultant/782366702/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic")
page_data = loader.load().pop().page_content
print(page_data)