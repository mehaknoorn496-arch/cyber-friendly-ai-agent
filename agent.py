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
    main()
 
