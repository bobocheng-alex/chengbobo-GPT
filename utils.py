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

# memory=ConversationBufferMemory(return_messages=True)
# print(get_chat_response("牛顿提出过哪些知名的定律",memory,"sk-29749206de9a4897bc10cde944ad4448"))
# print(get_chat_response("我上一个问题是什么？",memory,"sk-29749206de9a4897bc10cde944ad4448"))