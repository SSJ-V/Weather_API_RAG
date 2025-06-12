# Weather_API_RAG
Sure! Here's the complete **copy-paste-ready `README.md`** file for your **Weather API RAG Bot** project:

---

````markdown
# 🌦️ Weather Information RAG Bot using LangChain + NVIDIA API

This project is a Retrieval-Augmented Generation (RAG) chatbot that fetches current weather data for a city using the **OpenWeatherMap API**, embeds the data using **Ollama's `nomic-embed-text`**, and allows users to query this weather information using **NVIDIA's LLM API**.

---

## 🧠 Tech Stack

- **LangChain** – Framework for building LLM applications  
- **Ollama** – Local embeddings using `nomic-embed-text`  
- **Chroma** – Vector database to store weather embeddings  
- **NVIDIA API** – For question answering via large language model  
- **OpenWeatherMap API** – Provides real-time weather data  
- **Python (.env)** – Secrets management  

---
````

## 📦 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/weather-rag-bot.git
cd weather-rag-bot
````

2. **Set Up Virtual Environment**

```bash
python -m venv .venv
.venv\Scripts\activate  # For Windows
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Install and Run Ollama**

Download Ollama from [https://ollama.com](https://ollama.com)

Then pull the embedding model:

```bash
ollama pull nomic-embed-text
```

> ⚠️ Do **not** run the model, it is only used for embedding.

---

## 🔑 Setup `.env`

Create a `.env` file in the root directory with your keys:

```env
WEATHER_API_KEY=your_openweather_api_key
NVIDIA_API_KEY=your_nvidia_api_key
```

Replace the placeholders with your actual API keys.

---

## 🚀 Run the Bot

```bash
python main.py
```

You'll be prompted to ask weather-related questions:

```
💬 Ask about the weather (or 'exit'):
```

Example Questions:

* "What’s the temperature in Chennai?"
* "Is it humid today?"
* "What is the wind speed?"

---

## 📂 Project Structure

```
weather-rag-bot/
│
├── main.py               # Main app logic
├── .env                  # API keys (not shared)
├── weather_db/           # Vectorstore directory (auto-generated)
├── requirements.txt      # Python dependencies
└── README.md             # Project info
```

---

## ✅ To Do

* [ ] Add multi-city support
* [ ] Cache results for offline use
* [ ] Deploy as a web app using Streamlit or Flask

---

## 🙏 Credits

* [OpenWeatherMap](https://openweathermap.org/)
* [LangChain](https://www.langchain.com/)
* [Ollama](https://ollama.com/)
* [NVIDIA API](https://catalog.ngc.nvidia.com/ai-foundation-models)

---

## 📜 License

MIT License. Use freely but give credit where due!

```

---

You can now save this as `README.md` in the root of your project folder. Let me know if you'd like a `requirements.txt` file too.
```
