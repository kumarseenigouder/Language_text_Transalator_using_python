from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm1=ChatOpenAI( model="gpt-5")

# llm=ChatAnthropic(model="claude-3-5-sonnet")
responce=llm1.invoke("how are you?")
print(responce)



