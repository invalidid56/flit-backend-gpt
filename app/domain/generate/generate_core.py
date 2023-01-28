# coding=utf8
# REST API 호출에 필요한 라이브러리
import requests
import json

# [내 애플리케이션] > [앱 키] 에서 확인한 REST API 키 값 입력
REST_API_KEY = '9e5439d84ef67a884e65c99d4bd9eb82'

# KoGPT API 호출을 위한 메서드 선언
# 각 파라미터 기본값으로 설정
def kogpt_api(prompt, max_tokens = 1, temperature = 0.3, top_p = 0.6, n = 1):
    r = requests.post(
        'https://api.kakaobrain.com/v1/inference/kogpt/generation',
        json = {
            'prompt': prompt,
            'max_tokens': max_tokens,
            'temperature': temperature,
            'top_p': top_p,
            'n': n
        },
        headers = {
            'Authorization': 'KakaoAK ' + REST_API_KEY,
            'Content-Type': 'application/json'
        }
    )
    # 응답 JSON 형식으로 변환
    response = json.loads(r.content)
    return response

# KoGPT에게 전달할 명령어 구성
prompt = """
사업계획서 작성 중, 한글로만 문장을 하나만 끝마쳐야 함, 다음 문장을 끝까지 이어보시오: 
4.1 제품화 및 양산, 판로확보계획 ◦ 제품 개발 계획
1) 실제 사용 고객 수요 조사
- 사용자 중심 UX 시나리오를 위한 설문 조사
Ÿ 트랜드 연구, 사용자 니즈 및 시장 분석
Ÿ 이용 패턴 분석을 통해 제품 기획에 반영
- 제품 컨셉 추출
Ÿ 이해 관계자 인터뷰, 다학제적 """

# 파라미터를 전달해 kogpt_api()메서드 호출
response = kogpt_api(
    prompt=prompt,
    max_tokens=48,
    temperature=0.3,
    top_p=0.6,
    n=3
)

print(response['generations'][0]['text'])
print(response['generations'][1]['text'])
print(response['generations'][2]['text'])