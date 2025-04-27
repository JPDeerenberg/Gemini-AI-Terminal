import os
from google import genai

def talk_to_gemini(message):
    key = os.getenv("GOOGLE_API_KEY")
    if key is None:
        raise Exception("Missing API key. Set GOOGLE_API_KEY first.")

    bot = genai.Client(api_key=key)

    reply = bot.models.generate_content(
        model="gemini-2.0-flash",
        contents=message
    )

    return reply.text

def main():
    print("== Gemini AI Terminal ==")
    print("Say 'exit' to close.")

    while True:
        user_text = input("> ")

        if user_text.strip().lower() == "exit":
            print("Bye!")
            break

        try:
            response = talk_to_gemini(user_text)
            print(response)
        except Exception as err:
            print(f"Error: {err}")

if __name__ == "__main__":
    main()
