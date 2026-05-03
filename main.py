import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import ad_searcher, marketing_analyst, script_writer, production_lead
from tasks import search_task, analysis_task, script_task, production_task

# Load environment variables
load_dotenv()

def run_ad_crew():
    print("🚀 Starting the CW-Trading Ad Creation Crew...")
    
    # Define the Crew
    crew = Crew(
        agents=[ad_searcher, marketing_analyst, script_writer, production_lead],
        tasks=[search_task, analysis_task, script_task, production_task],
        process=Process.sequential,
        verbose=True
    )

    # Inputs for the crew
    inputs = {
        "product_name": "Crowd Wisdom Trading Course",
        "niche": "Stock Market Education & Trading Signals"
    }

    # Kickoff the crew
    result = crew.kickoff(inputs=inputs)
    
    print("\n\n########################")
    print("## AD CREATION COMPLETE ##")
    print("########################\n")
    print(result)

if __name__ == "__main__":
    run_ad_crew()
