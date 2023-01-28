from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from starlette import status
from typing import List
import requests
import json


router = APIRouter(
    prefix="/generate"
)


REST_API_KEY = '9e5439d84ef67a884e65c99d4bd9eb82'


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


prompt = """
사업 계획서 작성 중, 한글로만 문장을 하나만 끝 마쳐야 함, 다음 문장을 끝까지 이어 보시오: 
{0}"""


@router.get('/{sentence}', status_code=status.HTTP_204_NO_CONTENT)
def generate(sentence: str):
    response = kogpt_api(
        prompt=prompt.format(sentence),
        max_tokens=48,
        temperature=0.3,
        top_p=0.6,
        n=1
    )

    return JSONResponse(content={
        'suggestion': response['generations'][0]['text']
    })
