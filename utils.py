from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from  langchain.memory import  ConversationBufferMemory
def get_chat_response(prompt,memory,openai_api_key):
 model=ChatOpenAI(
     model="deepseek-chat",
     openai_api_key=openai_api_key,
     base_url="https://api.deepseek.com/v1")
 chain=ConversationChain(llm=model,memory=memory)
 response=chain.invoke({"input":prompt})
 return response["response"]
