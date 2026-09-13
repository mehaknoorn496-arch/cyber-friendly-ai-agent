import platform
import os
import datetime


BANNER = """
╔══════════════════════════════════════╗
║   🤖 CYBER-FRIENDLY AI AGENT         ║
║   🛡️ Cybersecurity + 💬 Friendly    ║
╚══════════════════════════════════════╝
"""


def system_info():
    print("\n🖥️ SYSTEM INFORMATION")
    print("-" * 35)
    print("OS:", platform.system())
    print("Version:", platform.version())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())


def security_check():
    print("\n🛡️ BASIC SECURITY CHECK")
    print("-" * 35)

    if platform.system() == "Windows":
        print("Windows detected.")
        print("Tip: Keep Windows Update and Microsoft Defender enabled.")
    elif platform.system() == "Linux":
        print("Linux detected.")
        print("Tip: Keep your packages updated.")
    else:
        print("Unknown operating system.")

    print("⚠️ This is a safe local check only.")


def friendly_chat(message):
    message = message.lower().strip()

    if message in ["hi", "hello", "salam", "assalamualaikum"]:
        return "Wa Alaikum Assalam! 😄 Main ready hoon."

    if "how are you" in message:
        return "Main bilkul ready hoon 🤖 Tum batao, kya karna hai?"

    if "joke" in message:
        return "😂 Cybersecurity wala computer doctor ke paas gaya... bola: mujhe bugs hain!"

    if "gossip" in message:
        return "☕ Gossip mode ON 😄 Lekin harmless aur respectful gossip hi!"

    if "study" in message:
        return "📚 Study mode bhi available hai. Topic batao!"

    return "😊 Interesting! Thora aur batao."


def help_menu():
    print("""
AVAILABLE COMMANDS

💬 Friendly
  chat <message>       Friendly conversation
  gossip                Friendly gossip mode

🛡️ Cybersecurity
  system                Show your computer information
  security              Basic local security check

ℹ️ Other
  help                  Show this menu
  time                  Show current time
  exit                  Close the agent

⚠️ Security tools are intended only for systems you own
or have explicit permission to test.
""")


def main():
    print(BANNER)
    print("Type 'help' to see commands.\n")

    while True:
        command = input("You ➜ ").strip()

        if not command:
            continue

        if command.lower() == "exit":
            print("Agent ➜ Bye! Stay safe online 👋")
            break

        elif command.lower() == "help":
            help_menu()

        elif command.lower() == "system":
            system_info()

        elif command.lower() == "security":
            security_check()

        elif command.lower() == "gossip":
            print("Agent ➜ ☕ Gossip mode ON! Kya baat karni hai? 😄")

        elif command.lower() == "time":
            print("Agent ➜", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        elif command.lower().startswith("chat "):
            message = command[5:]
            print("Agent ➜", friendly_chat(message))

        else:
            print("Agent ➜", friendly_chat(command))


if __name__ == "__main__":
    main()def phone_check():
    import re

    number = input("📞 Phone number (+country code): ").strip()

    # Basic validation
    cleaned = re.sub(r"[()\-\s]", "", number)

    if not cleaned.startswith("+"):
        print("⚠️ Please enter the number with country code.")
        print("Example: +92XXXXXXXXXX")
        return

    if not cleaned[1:].isdigit():
        print("❌ Invalid phone number format.")
        return

    print("\n📱 PHONE NUMBER CHECK")
    print("-" * 35)
    print("Number:", cleaned)

    # Country-code information
    country_codes = {
        "+92": "Pakistan",
        "+91": "India",
        "+1": "USA / Canada",
        "+44": "United Kingdom",
        "+971": "United Arab Emirates",
        "+966": "Saudi Arabia",
        "+90": "Türkiye",
    }

    country = "Unknown"
    for code, name in country_codes.items():
        if cleaned.startswith(code):
            country = name
            break

    print("Country/region:", country)
    print("Format:", "Looks valid" if len(cleaned) >= 8 else "Possibly invalid")
    print(" Private name, address and exact location are not obtained.")  phone elif command.lower() == "phone":
    phone_check()  You ➜ phone
📞 Phone number (+country )(place)(name):             Check basic phone-number information
