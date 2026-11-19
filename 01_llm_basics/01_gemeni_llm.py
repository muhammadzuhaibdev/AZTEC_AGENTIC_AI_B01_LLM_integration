from langchain_opneai import GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import os

llm = GoogleGenerativeAI(
     model="gemini-3.5-flash-lite",
     google_api_key=os.getenv("GEMINI_API_KEY")
)

userQuery = input("Enter your asking text here.... ")

result = llm.invoke(userQuery)
print(result)