# SHL Assessment Recommender 🎯

A conversational agent that helps hiring managers select the right SHL assessments through natural dialogue.

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     Streamlit UI                        │
│          (Conversational interface + results)           │
└──────────────────────┬──────────────────────────────────┘
                       │ HTTP (POST /chat)
┌──────────────────────▼──────────────────────────────────┐
│                   FastAPI Service                       │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │ Off-topic   │  │ Vagueness    │  │ Comparison    │  │
│  │ Detection   │  │ Detection    │  │ Detection     │  │
│  └─────────────┘  └──────────────┘  └───────────────┘  │
│  ┌─────────────────────────────────────────────────┐   │
│  │           Signal Extraction Engine              │   │
│  │  (Keywords, Levels, Test Types, Domain Mapping) │   │
│  └─────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────┐   │
│  │           Retrieval & Ranking                   │   │
│  │    (Keyword scoring against catalog items)      │   │
│  └─────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────┐   │
│  │           Groq LLM (Llama 3.3 70B)             │   │
│  │   (Grounded response generation)               │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│                 SHL Catalog (catalog.py)                 │
│              50+ Individual Test Solutions               │
└─────────────────────────────────────────────────────────┘
```

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
# Get a free key at: https://console.groq.com
```

### 3. Run Both Services

```bash
chmod +x start.sh
./start.sh
```

Or run separately:

```bash
# Terminal 1: FastAPI
export GROQ_API_KEY=your_key_here
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Terminal 2: Streamlit UI
export API_URL=http://localhost:8000
streamlit run streamlit_app.py  # Streamlit will use any available port
```

### 4. Access

- **UI**: http://localhost:8501
- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## API Reference

### GET /health
```json
{"status": "ok"}
```

### POST /chat
**Request:**
```json
{
  "messages": [
    {"role": "user", "content": "Hiring a Java developer who works with stakeholders"},
    {"role": "assistant", "content": "What seniority level?"},
    {"role": "user", "content": "Mid-level, around 4 years"}
  ]
}
```

**Response:**
```json
{
  "reply": "Here are 5 assessments that fit a mid-level Java developer...",
  "recommendations": [
    {"name": "Java 8 (New)", "url": "https://www.shl.com/...", "test_type": "K"},
    {"name": "OPQ32r", "url": "https://www.shl.com/...", "test_type": "P"}
  ],
  "end_of_conversation": false
}
```

## Design Decisions

### Why Groq + Llama 3.3 70B?
- **Speed**: Groq's LPU inference is ~10x faster than typical GPU inference (critical for 30s timeout)
- **Quality**: Llama 3.3 70B beats GPT-4o-mini on many benchmarks
- **Free tier**: Generous free limits for development

### Why keyword-based retrieval over vector DB?
- **Zero cold start**: No embedding computation needed on startup
- **Deterministic**: Same signals → same candidate set, easier to debug
- **Fast**: < 1ms retrieval vs 50-200ms for vector search
- **Sufficient**: With domain signal mapping, recall is competitive

The DOMAIN_SIGNALS dictionary acts as a hand-crafted semantic layer, mapping role signals (e.g., "java developer") to catalog keywords. This is more reliable than cosine similarity for a bounded, well-structured catalog.

### Context engineering strategy
Instead of sending the whole 50-item catalog as LLM context, we:
1. Extract signals from the conversation
2. Retrieve top-K candidates (typically 5-10 items)
3. Send only the relevant catalog subset as context
4. Instruct the LLM to use ONLY these items

This keeps prompts short (→ fast, cheap) while grounding the LLM to prevent hallucination.

### Agent behavior logic
```
User message received
    ↓
Off-topic / prompt injection? → Redirect
    ↓
Comparison query? → Load both items as context, compare mode
    ↓
Vague query (< 2 meaningful tokens)? → Ask ONE clarifying question
    ↓
Has enough context? → Retrieve candidates → LLM generates shortlist
```

## Running Tests

```bash
pip install pytest pytest-asyncio
pytest test_agent.py -v
```

## Deployment (Render)

1. Push to GitHub
2. Create Web Service on Render
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add env vars: `GROQ_API_KEY`, `GROQ_MODEL`

## Catalog Coverage

The catalog (`catalog.py`) covers 50+ SHL Individual Test Solutions including:

| Category | Examples |
|----------|---------|
| Ability & Aptitude (A) | Verify Interactive series, Graduate batteries |
| Knowledge & Skills (K) | Java, Python, SQL, JavaScript, DevOps |
| Personality & Behavior (P) | OPQ32r, MQM5, Agility |
| Situational Judgment (S) | Manager SJT, Customer Service SJT, Automata |
| Behavioral Simulation (B) | Sales, Customer Service simulations |
| Development (D) | UCF 360 |
