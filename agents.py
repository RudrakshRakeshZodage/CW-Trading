import os
from crewai import Agent
from langchain_openai import ChatOpenAI
from tools.apify_tool import MetaAdsSearchTool, AdPainExtractorTool
from tools.video_tool import ElevenLabsTTSTool, RemotionVideoTool

# Initialize LLM via OpenRouter
llm = ChatOpenAI(
    model=os.getenv("MODEL", "google/gemini-2.0-flash-lite-001"),
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1"
)

# Agent 1: Search successful ads
ad_searcher = Agent(
    role="Meta Ads Research Specialist",
    goal="Find the top performing ads in the last 30 days for {product_name} and {niche}.",
    backstory="Expert in digital marketing and competitive intelligence. You know how to find what's working on Meta Ads Library.",
    tools=[MetaAdsSearchTool()],
    llm=llm,
    verbose=True
)

# Agent 2: Extract marketing concepts
marketing_analyst = Agent(
    role="Marketing Strategist",
    goal="Analyze the successful ads and extract core pain points, hooks, and marketing concepts.",
    backstory="You are a psychology-driven marketer who understands deep customer pain points and how to leverage them in ads.",
    tools=[AdPainExtractorTool()],
    llm=llm,
    verbose=True
)

# Agent 3: Scriptwriter
script_writer = Agent(
    role="Creative Copywriter",
    goal="Create a high-converting 60-second ad script based on identified pain points and product data.",
    backstory="Award-winning copywriter specialized in short-form video ads. You know how to make people stop scrolling.",
    llm=llm,
    verbose=True
)

# Agent 4: Production Lead
production_lead = Agent(
    role="Video Production Specialist",
    goal="Generate the audio and prepare video assets for the final ad.",
    backstory="Expert in multimedia production, specialized in automated video creation using AI voices and Remotion.",
    tools=[ElevenLabsTTSTool(), RemotionVideoTool()],
    llm=llm,
    verbose=True
)
