# https://www.promptingguide.ai/introduction/settings
# Temperature - In short, the lower the temperature, the more deterministic the results in the sense that the highest probable next token is always picked. Increasing temperature could lead to more randomness, which encourages more diverse or creative outputs. You are essentially increasing the weights of the other possible tokens. In terms of application, you might want to use a lower temperature value for tasks like fact-based QA to encourage more factual and concise responses. For poem generation or other creative tasks, it might be beneficial to increase the temperature value.
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

llm = GoogleGenerativeAI(
     model="gemini-3.5-flash-lite",
     google_api_key=os.getenv("GEMINI_API_KEY"),
     temperature=0.7
)


question = input("Enter you prompt: ")

response = llm.invoke(question)

print("Response", response)
