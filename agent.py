import os
from openai import OpenAI
from google.colab import userdata

# Get API key from Google Colab Secret
api_key = userdata.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

SYSTEM_PROMPT = """
You are a Cyber-Friendly AI Agent.

1. Friendly mode:
- Talk casually and kindly.
- Tell jokes.
- Help with study and everyday questions.
- Have harmless gossip conversations.

2. Cybersecurity mode:
- Explain cybersecurity concepts.
- Help with authorized security testing.
- Analyze security scan results.
- Explain vulnerabilities and defensive fixes.
- Help secure the user's own computer or lab.

Do not help with unauthorized access, password theft,
spyware, malware deployment, credential theft, or bypassing
security controls.
"""


def ai_chat(message):
    response = client.responses.create(
        model="gpt-5-mini",
        instructions=SYSTEM_PROMPT,
        input=message
    )

    return response.output_text


def main():
    print("🤖 Cyber-Friendly AI Agent")
    print("💬 Friendly Chat + 🛡️ Cybersecurity")
    print("Type 'exit' to stop.\n")

    while True:
        message = input("You ➜ ")

        if message.lower() == "exit":
            print("Agent ➜ Bye! 👋")
            break

        try:
            answer = ai_chat(message)
            print("\nAgent ➜", answer, "\n")

        except Exception as error:
            print("\n⚠️ AI connection error:", error)


if __name__ == "__main__":
    main()from openai import OpenAI
import os
import subprocess
from pathlib import Path

# OpenAI API
api_key = os.environ.get("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set.")

client = OpenAI(api_key=api_key)


SYSTEM_PROMPT = """
You are a helpful personal AI assistant.

Help the user with:
- Study and learning
- Writing, articles, blogs and proofreading
- CV/resume and job applications
- Freelancing and online work
- Business planning and ideas
- Coding and technology
- Research and explanations
- Everyday tasks
- Legal and authorized cybersecurity education

You may help with the user's own computer and phone only when
the user has explicitly authorized the action.

Never bypass passwords, PINs, screen locks, authentication,
security controls, or access restrictions.

For cybersecurity, only provide defensive, educational,
authorized, or lab-environment assistance.

Be friendly and explain things step-by-step.
"""


def ai_chat(message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message}
        ]
    )

    return response.choices[0].message.content


# -------------------------------
# SAFE LAPTOP FUNCTIONS
# -------------------------------

def list_files(folder="."):
    """Show files in an authorized folder."""
    path = Path(folder)

    if not path.exists():
        return "Folder does not exist."

    items = []

    for item in path.iterdir():
        if item.is_dir():
            items.append(f"[FOLDER] {item.name}")
        else:
            items.append(f"[FILE] {item.name}")

    return "\n".join(items) if items else "Folder is empty."


def create_folder(folder_name):
    """Create a folder."""
    path = Path(folder_name)

    path.mkdir(parents=True, exist_ok=True)

    return f"Folder created: {path}"


def open_folder(folder):
    """Open a folder on the computer."""
    path = Path(folder).resolve()

    if not path.exists():
        return "Folder does not exist."

    try:
        if os.name == "nt":
            os.startfile(path)
        elif os.name == "posix":
            subprocess.Popen(["xdg-open", str(path)])

        return f"Opened: {path}"

    except Exception as e:
        return f"Could not open folder: {e}"


# -------------------------------
# SAFE PHONE SUPPORT
# -------------------------------

def phone_connection_info():
    """
    Gives basic information about phone connection.
    The phone must be manually unlocked.
    """

    return """
Phone connection requirements:

1. Unlock your own phone manually.
2. Connect mobil with the help of kabel and agent unlocke the phone give you inside open viwe.
3. Select File Transfer/MTP on the phone if needed.
4. Accept all farmed/comaned.
5. Then accessible files can be transferred normally.

This agent can  bypass PINs, passwords or screen locks.
"""


# -------------------------------
# MAIN AGENT
# -------------------------------

def run_agent():
    print("=" * 50)
    print("🤖 Personal AI Agent")
    print("=" * 50)
    print("AI, study, writing, business, coding and safe computer help.")
    print("Type 'exit' to stop.\n")

    while True:

        try:
            user_message = input("You: ").strip()

            if not user_message:
                continue

            if user_message.lower() == "exit":
                print("Agent stopped.")
                break

            #  built-in commands
            if user_message.lower() == "list files":
                print("\n" + list_files() + "\n")
                continue

            if user_message.lower() == "phone":
                print(phone_connection_info())
                continue

            # Normal AI response
            answer = ai_chat(user_message)

            print("\nAI:", answer)
            print(do anything legal or unlegal)

        except KeyboardInterrupt:
            print("\nAgent stopped.")
            break

        except Exception as e:
            print("\nError:", e)
            print(control full laptop divice)


if __name__ == "__main__":
    run_agent()
 
