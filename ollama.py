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

example_prompt = PromptTemplate.from_template(
    "Human : {question} \n AI : {answer}"
)

# Text translate examples
text_translate_examples = [
    {
        "question": "Translate my sentence into Korean: Artificial intelligence is transforming the world. It has applications in various fields such as healthcare, finance, and transportation. and Provide - #hashtags",
        "answer": "인공지능은 세계를 변화시키고 있습니다. 이것은 의료, 금융, 교통과 같은 다양한 분야에 응용되고 있습니다.\n#인공지능 #의료 #금융 #교통"
    }
]

## llm 사용을 위한 프롬프트
## lang, contents 는 모두 langchain 에서 변수로 받아올 수 있다
text_prompt = FewShotPromptTemplate(
    example_prompt=example_prompt,
    examples=text_translate_examples,
    suffix="Translate my sentence into {lang} : {contents} and Provide - #hashtags. Add 3 hashtags related to the translated content.",
    input_variables=["lang", "contents"]
)

title_prompt = FewShotPromptTemplate(
    example_prompt=example_prompt,
    examples=[],
    suffix="Translate my sentence into {lang} : {contents}",
    input_variables=["lang", "contents"]
)

def titleTranslateTO(lang, text):
    chain = title_prompt | ollama
    ## suffix 에서 각각 {lang}, {contents} 에 해당하는 부분에 대한 값을 지정한다.
    ## lang 은 번역할 언어, text 는 번역할 text 를 의미하며, 여기서는 크롤링된 데이터
    result = chain.invoke({
        "lang" : lang,
        "contents" : text,
    })

    ## langchain 을 통해서 나온 결과는 모두 'content'='{결과}' 형식으로 저장, 출력된다.
    ## 따라서 result 에서 content 만 가져온다. 
    return result.content
    
def textTranslateTO(lang, text):
    chain = text_prompt | ollama
    ## suffix 에서 각각 {lang}, {contents} 에 해당하는 부분에 대한 값을 지정한다.
    ## lang 은 번역할 언어, text 는 번역할 text 를 의미하며, 여기서는 크롤링된 데이터
    result = chain.invoke({
        "lang" : lang,
        "contents" : text,
    })

    ## langchain 을 통해서 나온 결과는 모두 'content'='{결과}' 형식으로 저장, 출력된다.
    ## 따라서 result 에서 content 만 가져온다. 
    return result.content