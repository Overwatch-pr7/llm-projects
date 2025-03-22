from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = OpenAI(openai_api_key="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")

prompt = PromptTemplate(
    input_variables=["input_language", "output_language", "text"],
    template="Translate the following text from {input_language} to {output_language}: {text}"
)

llm_chain = LLMChain(llm=llm, prompt=prompt)

result = llm_chain.run({
    'input_language': 'English',
    'output_language': 'French',
    'text': 'Hello, how are you?'
})
print(result)
