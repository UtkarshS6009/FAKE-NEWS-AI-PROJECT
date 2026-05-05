import os

def generate_fake_news(topic):
    try:
        from groq import Groq

        api_key = "api key"

        if not api_key:
            return "⚠ GROQ_API_KEY not set."

        client = Groq(api_key=api_key)

        prompt = f"Write a realistic fake news article about {topic}."

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",

            messages=[
                {"role": "user", "content": prompt}
            ],
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Generator Error: {str(e)}"
