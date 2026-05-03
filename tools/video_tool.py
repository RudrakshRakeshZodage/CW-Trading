import os
import requests
from crewai.tools import BaseTool

class ElevenLabsTTSTool(BaseTool):
    name: str = "elevenlabs_tts"
    description: str = "Converts ad script to voice using ElevenLabs API."
    
    def _run(self, text: str, voice_id: str = "pNInz6obpg8ndclQU7Nc") -> str:
        api_key = os.getenv("ELEVENLABS_API_KEY")
        if not api_key or "your_" in api_key:
            return "[MOCK] Voice generated successfully at data/ad_voice.mp3 (Simulated)"
            
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": api_key
        }
        data = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }
        
        try:
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 200:
                output_path = "data/ad_voice.mp3"
                with open(output_path, "wb") as f:
                    f.write(response.content)
                return f"Voice generated successfully at {output_path}"
            else:
                return f"Error from ElevenLabs: {response.text}"
        except Exception as e:
            return f"Exception in TTS: {str(e)}"

class RemotionVideoTool(BaseTool):
    name: str = "remotion_video_generator"
    description: str = "Triggers Remotion to render the video with script and audio."
    
    def _run(self, script_json: str) -> str:
        try:
            os.makedirs("remotion", exist_ok=True)
            with open("remotion/data.json", "w") as f:
                f.write(script_json)
            
            return "[MOCK] Remotion data prepared. Video rendering simulation complete."
        except Exception as e:
            return f"Error preparing Remotion: {str(e)}"
