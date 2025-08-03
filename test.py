from langchain_openai import ChatOpenAI
from langchain_core.utils.utils import convert_to_secret_str

api_key = convert_to_secret_str("sk-L53ZUgB9WiwHjnmQl0hCtxLMAVvoPRfNJy234GzX3DFKlQbs")
llm = ChatOpenAI(model="gemini-2.5-pro",base_url="https://www.chataiapi.com/v1", api_key=api_key)

print(llm.invoke("你好,介绍一下你自己！我问的是你叫啥名字！具体代号是什么？听说你是gemini系列，具体介绍你的版本、模型体量等。比如到底是1.5还是2.5，是pro还是flash。"))

# for k in llm.stream("大香蕉，你是大香蕉！"):
#     print(k.content)

