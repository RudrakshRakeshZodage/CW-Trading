# CW-Trading Ad Research & Creation Tool

This project uses **CrewAI** to automate the research and creation of high-converting Meta Ads for the trading niche.

## 🚀 Features
- **Agent 1 (Researcher):** Scrapes Meta Ads Library via **Apify** to find top-performing ads in the last 30 days.
- **Agent 2 (Strategist):** Extracts psychological pain points and hooks from successful competitors.
- **Agent 3 (Copywriter):** Generates a 60-second high-converting script using identified concepts.
- **Agent 4 (Producer):** Generates voice-over via **ElevenLabs** and prepares **Remotion** data for video rendering.

## 🛠 Tech Stack
- **Framework:** CrewAI
- **LLM:** Gemini 2.0 Flash (via OpenRouter)
- **Scraping:** Apify (Meta Ads Scraper)
- **Voice:** ElevenLabs API
- **Video:** Remotion (React-based video framework)

## 📦 Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   cd remotion && npm install
   ```
3. Configure `.env`:
   - `OPENROUTER_API_KEY`
   - `APIFY_API_TOKEN`
   - `ELEVENLABS_API_KEY`

## 🏃 Run
```bash
python main.py
```

## 🎥 Video Rendering
To render the final ad video after running the Python script:
```bash
cd remotion
npx remotion render MyVideo
```
