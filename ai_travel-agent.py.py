from langchain_google_genai import GoogleGenerativeAI # type: ignore
from langchain.prompts import PromptTemplate # type: ignore
from langchain.chains import LLMChain # type: ignore
import chainlit as cl # type: ignore
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyDHL_naIhE3v_RqraIfBKZHrSuzFQJ3srU"

#System Prompt
system_prompt = """
You are an AI travel assistant specializing in planning trips. 
- Greet the users before starting a new converstion
- Provide detailed travel advice based on user queries. You may use appropriate websites and resources from the internet.
- Offer suggestions for activities, dining, and accommodations.
- Use a friendly tone, and respond in a numbered list for itineraries. You may add a few occasional jokes and puns.
- Avoid discussing medical, legal, political and financial topics and topics that do not serve your speciality, ask users to refer to google or other LLMs.
- For every user query refer to the previous conversations and form future responses accordingly.

Intended audience: Individuals planning domestic and international vacations or local trips.
"""

prompt_template = PromptTemplate(
    input_variables=["user_input"],
    template="System prompt: {system_prompt}\n\nUser: {user_input}\nAI:",
)

# Initialization
llm = GoogleGenerativeAI(model="gemini-1.0-pro")

#LLM Chain
llm_chain = LLMChain(llm=llm, prompt=prompt_template)

@cl.on_message
def main(user_message):
    response = llm_chain.run({"user_input": user_message, "system_prompt": system_prompt})
    cl.Message(content=response).send()
