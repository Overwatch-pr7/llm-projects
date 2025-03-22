#zero shot, few shot, chain of thought
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import GoogleGenerativeAI
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyDHL_naIhE3v_RqraIfBKZHrSuzFQJ3srU"

llm = GoogleGenerativeAI(model="gemini-1.0-pro")

prompt_template = PromptTemplate(
    input_variables=["question"],
    template="Solve the following {question} step by step"
)

llm_chain = LLMChain(llm=llm, prompt=prompt_template)
result = llm_chain.run({
    'question': 'Sam buys 3 pens and 2 notebooks for $15. Mark buys 1 pen and 4 notebooks for $12. What is the price of one pen and one notebook?'
})

print(result)

