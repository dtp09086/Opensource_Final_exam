# -*- coding: utf-8 -*-
"""Opensource_Final_exam

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gDo59NfkNB39iRsHVoGfCi5CNF_wr3wt
"""

#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20212064  이름 : 최예진

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.


def solution(my_string, target):
    if target in my_string:   # target이 my_string 문자열 안에 있는지 확인
        answer = 1            # 있다면 answer에 1대입 (True라면 1대입)
    else:                     # target이 my_string 문자열 안에 없다면 (false라면)
        answer = 0            # answer에 0 대입
    return answer             # 결과값으로 answer 값을 돌려줌

my_string = "Life is too short, you need pythton"
target = "need"

print(solution(my_string, target))

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.


def solution(letter):
    morse = {
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}


    answer = ' '  #문자열 선언
    for str in letter.split():     # 문자열에서 공백기준으로 나누어 str에 차례대로 넣어주기
        answer += morse.get(str)   # str(key)에 대응되는 value값 찾아 answer에 이어서 대입해주기

    return answer

letter = '.--- ..- ... - -.- . . .--. --. --- .. -. --.'
print(f'모스부호 해독 결과는{solution(letter)} 입니다.')

# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    alp = {'0':'a','1':'b','2':'c','3':'d', '4':'e',
           '5':'f', '6':'g', '7':'h', '8':'i', '9':'j'}  # 숫자에 대응하는 알파벳을 딕셔너리로 만듦

    age1 = str(age)    # 매개변수로 온 age를 문자열로 반환하여 age1에 대입
    answer = ''      #문자열 선언
    for eng in age1:    # for문을 사용하여 차례대로 eng변수에 대입
        answer += alp.get(eng)  # eng값(key)에 대응되는 value값 찾아 answer에 이어서 대입해주기

    return answer

age = 857                                             # age에 PROGRAMMERS-857행성의 나이 대입
print(f'행성의 나이는 {solution(age)} 입니다.')       # 함수를 통해 숫자로 된 나이를 알파벳으로 바꿔 출력

# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution(r1, r2):

     answer = 0                 #answer 변수 0으로 초기화

     for x in range(1,r2) :           # x에 1부터 r2-1까지 차례대로 대입
        for y in range(1,r2):         # y에 1부터 r2-1까지 차례대로 대입
            if r1*r1 <= x*x + y*y and x*x + y*y <= r2*r2:     # x,y값이 두 원 사이에 있을 경우
                answer += 1                                   #점의 갯수를 하나씩 들려줌
            else:
                continue                               # 만약 x,y값이 두 원 사이에 없다면 다시 for문으로 돌아감

     #for문을 통해 나온 answer -> 제 1사분면에서 두 원 사이에 있는 점(정수)들의 갯수 (다른 사분면들과 겹칠 수 있는 점들은 뺀 값)
     # 나머지 제 2사분면,제 3사분면, 제 4사분면도 두 원 사이에 있는 점들의 갯수가 같으므로(원은 대칭)
     # for문에서 나온 answer깂에 4를 곱해줌 ->  answer * 4
     # 각 사분면의 경계에 있는 점들 (x값이 0이거나 y값이 0인경우)의 갯수를 answer에 더해준다 -> answer *4 + (r2-r1+1)* 4
     # answer *4 + (r2-r1+1)* 4 == (answer+(r2-r1+1)) * 4

     answer = (answer+ (r2-r1 +1)) * 4

     return answer

r1 = 10
r2 = 20
# 두 점 사이에 존재하는 정수로 된 점들의 갯수 출력
print(f'반지름이 {r1},{r2}인 두 점 사이에 존재하는 x,y좌표 값이 정수인 점들의 갯수는 {solution(r1,r2)}개 입니다.')

# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

import itertools    # itertools.permutation 함수를 사용하기 위한 표준 라이브러리 선언

def solution(numbers):
    temp1 = []                         #리스트 생성
    temp2 = []
    temp3 = []

    for number in numbers:             # 리스트값을 차례대로 number에 대입
        temp1.append(str(number))      # 정수형으로 저장된 변수들을 문자열로 바꿔주어 temp1리스트에 순서대로 저장

    temp2 = list(itertools.permutations(temp1,len(temp1)))   #temp1에 저장된 원소들에서 가능한 순열 조합을 temp2에 리스트로 저장

    for x in temp2:                       #가능한 배열 조합을 차례대로 x에 대입
        str1 = ''
        for y in x:                        # 순열 조합에서 차례대로 y값에 대입
            str1 += y                      # 순서대로 문자열을 합쳐 str1에 저장
        temp3.append(str1)                 # 가능한 순열 조합에서 문자열을 합친 str1을 temp3에 차례대로 저장

    answer = max(temp3)                    # 가능한 순열조합을 이어 만든 문자열에서 가장 큰 값을 뽑아 answer에 대입
    return answer

numbers = [8, 30, 17, 2, 23]
print(f'주어진 정수들을 이어 만들수 있는 가장 큰 값은 {solution(numbers)} 입니다.')