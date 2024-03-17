from langchain.chat_models import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.callbacks import StreamingStdOutCallbackHandler
import os
from dotenv import load_dotenv

# .env 파일을 로드
load_dotenv()

base_ollama_url = os.getenv('OLLAMA_URL_LOCAL')
ollama = ChatOllama(
    base_url = base_ollama_url,
    model="openHermes",
    temperature=0.1,
    # streaming=True,
    # callbacks=[
    #     StreamingStdOutCallbackHandler()
    # ]
)

examples = []

example_prompt = PromptTemplate.from_template(
    "Human : {question} \n AI : {answer}"
)

## llm 사용을 위한 프롬프트
prompt = FewShotPromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
    suffix="Translate my sentence into {lang} : {contents}", ## lang, contents 는 모두 langchain 에서 변수로 받아올 수 있다
    input_variables=["lang", "contents"]
)


def transrateTO(lang, text):
    chain = prompt | ollama
    ## suffix 에서 각각 {lang}, {contents} 에 해당하는 부분에 대한 값을 지정한다.
    ## lang 은 번역할 언어, text 는 번역할 text 를 의미하며, 여기서는 크롤링된 데이터
    result = chain.invoke({
        "lang" : lang,
        "contents" : text,
    })

    ## langchain 을 통해서 나온 경과는 모두 'content'='{결과}' 형식으로 저장, 출력된다.
    ## 따라서 result 에서 content 만 가져온다. 
    return result.content
