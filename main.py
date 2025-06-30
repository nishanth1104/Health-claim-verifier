from whisper_input import record_and_transcribe
from tts_output import speak_text
from agent import get_agent_response
from dotenv import load_dotenv

load_dotenv()

def main():
    print("🎤 Please speak a health claim...")
    claim = record_and_transcribe()
    print("📝 You said:", claim)

    response = get_agent_response(claim)
    print("🤖 AI Response:", response)

    speak_text(response)

if __name__ == "__main__":
    main()
