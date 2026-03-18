# Construction Content Generator

A Gen AI project for construction professionals that generates structured reports using:
- FastAPI
- ChromaDB
- Sentence Transformers
- Hugging Face InferenceClient
- Single-page HTML frontend

## Setup

### 1. Install dependencies
pip install -r requirements.txt

### 2. Add your Hugging Face token in `.env`
HF_TOKEN=your_token_here
HF_MODEL=Qwen/Qwen2.5-7B-Instruct
HF_PROVIDER=hf-inference

### 3. Ingest knowledge base
python -m app.services.ingest_data

### 4. Run backend
uvicorn app.main:app --reload

### 5. Run frontend
cd frontend
python -m http.server 5500

Open:
http://127.0.0.1:5500