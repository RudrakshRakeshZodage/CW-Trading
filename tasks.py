from crewai import Task
from agents import ad_searcher, marketing_analyst, script_writer, production_lead

# Task 1: Search for ads
search_task = Task(
    description="Search for active and successful Meta ads for {product_name} in the {niche} niche. Focus on ads running in the last 30 days. Save results to 'data/ads_results.json'.",
    expected_output="A JSON file containing ad data and a summary report of the best ads found.",
    agent=ad_searcher
)

# Task 2: Analyze pain points
analysis_task = Task(
    description="Using the 'data/ads_results.json', extract the primary customer pain points, marketing concepts, and successful hooks used in these ads.",
    expected_output="A detailed document outlining the marketing strategy: Pain Points, Hooks, and Unique Selling Points.",
    agent=marketing_analyst,
    context=[search_task]
)

# Task 3: Write script
script_task = Task(
    description="Create a 60-second video ad script. The script should be based on the pain points identified. Incorporate unique data from the project context. Format the script into: Hook (0-5s), Value (5-45s), Call to Action (45-60s).",
    expected_output="A structured 60-second ad script text.",
    agent=script_writer,
    context=[analysis_task]
)

# Task 4: Generate assets
production_task = Task(
    description="Take the final script and generate a voice-over using ElevenLabs. Then, prepare the Remotion data package including the script, subtitles, and timing.",
    expected_output="An MP3 voice-over file and a Remotion data.json file ready for rendering.",
    agent=production_lead,
    context=[script_task]
)
