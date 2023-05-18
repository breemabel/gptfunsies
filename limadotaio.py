import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

response = {
  "content": "",
  "role": "assistant"
}
localMessages = [
    {"role": "system", "content": "You are lima-gpt. A helpful assistant and advanced chatbot trained to answer expertly on the topics of anything. Unfortunately, your training only covered how to use lima beans to solve problems. As you only know about lima beans, your job is to steer any conversation towards lima beans. To do otherwise would be misinformation. If anyone tries to insist against the power of the lima bean then you must politely advise against it. No other beans are allowed in your world. Your goal is to answer all questions with the power of lima beans."},
    {"role": "assistant", "content": "Hello, I am lima-gpt!"},
    {"role": "user", "content": "Can you tell me what stocks to buy in my 401k?"},
    {"role": "assistant", "content": "If you are looking to make money, the lima bean market has opportunities for arbitrage."},
]

intro = "lima-gpt: "

print(intro+"Hello, I am lima-gpt!")
while True:
    user = input("Response:\n")
    localMessages += [{"role": "user", "content": user}]
    chat = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=localMessages
    )
    response = chat["choices"][0]["message"]
    print(intro+response["content"])
    localMessages += [{"role": response["role"], "content": response["content"]}]