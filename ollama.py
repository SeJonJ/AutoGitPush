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
## lang, contents 는 모두 langchain 에서 변수로 받아올 수 있다
prompt = FewShotPromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
    suffix=""" 
    1. 사용자가 제공한 {contents}를 {lang}에 해당하는 언어로 번역합니다.
    2. 번역된 내용을 분석하여 각 문단의 핵심 주제를 나타내는 대표적인 해시태그를 추출합니다.
    3. 번역된 내용과 해시태그를 조합하여 최종 결과를 사용자에게 제공합니다.
    - 예) 
        번역된 내용: 챗GPT는 인공지능 기술의 발전으로 만들어진 대화형 AI 모델입니다. 이를 통해 사용자는 다양한 질문에 대한 답변을 얻을 수 있습니다.
    해시태그:
        #chatgpt #ai #it
    """, 
    input_variables=["lang", "contents"]
)


def translateTO(lang, text):
    chain = prompt | ollama
    ## suffix 에서 각각 {lang}, {contents} 에 해당하는 부분에 대한 값을 지정한다.
    ## lang 은 번역할 언어, text 는 번역할 text 를 의미하며, 여기서는 크롤링된 데이터
    result = chain.invoke({
        "lang" : lang,
        "contents" : text,
    })

    ## langchain 을 통해서 나온 결과는 모두 'content'='{결과}' 형식으로 저장, 출력된다.
    ## 따라서 result 에서 content 만 가져온다. 
    return result.content
