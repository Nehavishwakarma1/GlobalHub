from openai import OpenAI

# Add your API key here
client = OpenAI(api_key="YOUR_API_KEY_HERE")

print("🌍 GlobalHub AI Assistant (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a visa and travel assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    print("AI:", response.choices[0].message.content)