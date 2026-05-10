#!/bin/bash
# ─────────────────────────────────────────────
# SHL Assessment Recommender - Startup Script
# ─────────────────────────────────────────────

set -e

# Load environment variables if .env exists
if [ -f .env ]; then
    export $(cat .env | grep -v '#' | xargs)
    echo "✅ Loaded .env file"
fi

# Check for Groq API key
if [ -z "$GROQ_API_KEY" ]; then
    echo "❌ GROQ_API_KEY is not set. Please set it in .env or as an environment variable."
    echo "   Get your key at: https://console.groq.com"
    exit 1
fi

echo "🚀 Starting SHL Assessment Recommender..."
echo "   Model: ${GROQ_MODEL:-llama-3.3-70b-versatile}"
echo ""

# Start FastAPI in background
echo "📡 Starting FastAPI server on port 8000..."
uvicorn main:app --host 0.0.0.0 --port 8000 --reload &
FASTAPI_PID=$!
echo "   FastAPI PID: $FASTAPI_PID"

# Wait for FastAPI to start
sleep 2

# Check FastAPI health
if curl -s http://localhost:8000/health > /dev/null 2>&1; then
    echo "✅ FastAPI is running!"
else
    echo "⚠️  FastAPI may still be starting..."
fi

echo ""
echo "🎨 Starting Streamlit UI on any available port..."
export API_URL=http://localhost:8000
streamlit run streamlit_app.py &
STREAMLIT_PID=$!
echo "   Streamlit PID: $STREAMLIT_PID"

echo ""
echo "═══════════════════════════════════════════"
echo "✅ SHL Assessment Recommender is running!"
echo ""
echo "   API:       http://localhost:8000"
echo "   UI:        http://localhost:<streamlit-port> (see terminal output)"
echo "   API docs:  http://localhost:8000/docs"
echo "═══════════════════════════════════════════"
echo ""
echo "Press Ctrl+C to stop both services."

# Wait for either process to exit
wait $FASTAPI_PID $STREAMLIT_PID

# Cleanup on exit
trap "kill $FASTAPI_PID $STREAMLIT_PID 2>/dev/null; echo 'Stopped.'" EXIT
