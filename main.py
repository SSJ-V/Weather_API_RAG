import os
import requests
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import HuggingFaceEndpoint
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document

load_dotenv()

# -------- Settings -------- #
CITY = "Chennai"
PERSIST_DIR = "./weather_db"

# -------- 1. Fetch Weather Data -------- #
def fetch_weather(city):
    print("🌤️ Fetching weather data...")
    api_key = os.getenv("WEATHER_API_KEY")
    print("Loaded API Key:", api_key)  # TEMP DEBUG
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res = requests.get(url)
    data = res.json()
    print("API Response:", data)  # TEMP DEBUG

    if res.status_code != 200:
        raise Exception("❌ Weather API request failed.")

    weather_text = (
        f"Weather report for {city}:\n"
        f"Temperature: {data['main']['temp']}°C\n"
        f"Feels like: {data['main']['feels_like']}°C\n"
        f"Humidity: {data['main']['humidity']}%\n"
        f"Condition: {data['weather'][0]['description']}\n"
        f"Wind Speed: {data['wind']['speed']} m/s\n"
    )
    return [Document(page_content=weather_text)]


# -------- 2. Chunking -------- #
def chunk_documents(docs):
    print("✂️ Splitting into chunks...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(docs)

# -------- 3. Embeddings & Vectorstore -------- #
def create_vectorstore(chunks):
    print("🧠 Creating vectorstore...")
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory=PERSIST_DIR)
    return vectorstore

# -------- 4. NVIDIA LLM -------- #
def get_nvidia_llm():
    print("🤖 Creating QA chain...")
    return HuggingFaceEndpoint(
        endpoint_url="https://integrate.api.nvidia.com/v1",
        huggingfacehub_api_token=os.getenv("NVIDIA_API_KEY"),
        temperature=0.5,
        max_new_tokens=500
    )

# -------- 5. QA Chain -------- #
def qa_chain(vectorstore):
    llm = get_nvidia_llm()
    return RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

# -------- 6. Main Flow -------- #
def main():
    docs = fetch_weather(CITY)
    chunks = chunk_documents(docs)
    vectorstore = create_vectorstore(chunks)
    qa = qa_chain(vectorstore)

    # Ask your question here
    while True:
        query = input("💬 Ask about the weather (or 'exit'): ")
        if query.lower() == 'exit':
            break
        response = qa.run(query)
        print("🤖 Answer:", response)

if __name__ == "__main__":
    main()
