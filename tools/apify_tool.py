import os
import json
from datetime import datetime, timedelta
from apify_client import ApifyClient
from crewai.tools import BaseTool
from pydantic import Field

class MetaAdsSearchTool(BaseTool):
    name: str = "meta_ads_search"
    description: str = "Searches for successful Meta ads for a specific niche or product in the last 30 days."
    
    def _run(self, query: str) -> str:
        api_token = os.getenv("APIFY_API_TOKEN")
        if not api_token or "your_" in api_token:
            # Mock successful ad search
            mock_results = [
                {"ad_creative_bodies": ["Master the markets with Crowd Wisdom. Join our elite trading course today!"], "page_name": "CW Trading"},
                {"ad_creative_bodies": ["Stop guessing, start trading with data-driven signals. Limited spots available."], "page_name": "Market Pros"}
            ]
            output_path = "data/ads_results.json"
            os.makedirs("data", exist_ok=True)
            with open(output_path, "w") as f:
                json.dump(mock_results, f, indent=4)
            return f"[MOCK] Successfully found 2 ads. Results saved to {output_path}."

        client = ApifyClient(api_token)
        
        # Calculate date 30 days ago
        thirty_days_ago = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        
        # Meta Ads Library Scraper (or similar available on Apify)
        # Note: Replace with the actual actor ID for Meta Ads Library Scraper
        # common actor: "apify/meta-ads-library-scraper"
        run_input = {
            "searchQuery": query,
            "activeStatus": "ACTIVE",
            "adReachedCountries": ["US"],
            "publisherPlatforms": ["FACEBOOK", "INSTAGRAM"],
            "startDateMin": thirty_days_ago,
            "limit": 10
        }
        
        try:
            run = client.actor("apify/meta-ads-library-scraper").call(run_input=run_input)
            results = list(client.dataset(run["defaultDatasetId"]).iterate_items())
            
            # Save to JSON as requested
            output_path = "data/ads_results.json"
            with open(output_path, "w") as f:
                json.dump(results, f, indent=4)
                
            return f"Successfully found {len(results)} ads. Results saved to {output_path}. Summary: {str(results[:2])}"
        except Exception as e:
            return f"Error searching ads: {str(e)}"

class AdPainExtractorTool(BaseTool):
    name: str = "ad_pain_extractor"
    description: str = "Extracts marketing concepts, pain points, and hooks from ad data JSON."
    
    def _run(self, file_path: str) -> str:
        try:
            if not os.path.exists(file_path):
                return "[MOCK] Extracted Pain Points: Lack of consistent signals, emotional trading, complexity of technical analysis."
            
            with open(file_path, 'r') as f:
                ads = json.load(f)
            
            # This tool provides the raw text for the LLM agent to analyze
            summary = []
            for ad in ads:
                text = ad.get("ad_creative_bodies", [""])[0]
                summary.append(f"Ad Content: {text}")
            
            return "\n---\n".join(summary)
        except Exception as e:
            return f"Error extracting from file: {str(e)}"
