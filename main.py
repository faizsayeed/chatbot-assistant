import os
import webbrowser
from dotenv import load_dotenv
import google.generativeai as genai  # Gemini SDK

# 🔹 Load API key from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found. Please set it in a .env file!")

genai.configure(api_key=GEMINI_API_KEY)

# Load model
model = genai.GenerativeModel("gemini-2.0-flash")

print("✅ Script started... (type 'exit' to quit)")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    # 🔹 Handle "open ..." commands
    if user_input.lower().startswith("open "):
        target = user_input[5:].strip()

        # If it looks like a website (contains a dot like .com, .org, .ai, etc.)
        if "." in target:
            if not target.startswith("http"):
                target = "https://" + target
            webbrowser.open(target)
            print(f"🌐 Opening website: {target}")
        else:
            # Try to open as a Windows app or file
            try:
                os.system(target)
                print(f"🖥️ Opening application: {target}")
            except Exception as e:
                print(f"❌ Could not open {target}: {e}")
        continue

    # 🔹 If not a command, send input to Gemini
    response = model.generate_content(user_input)
    print("Bhai:", response.text)
