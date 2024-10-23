#!/bin/python3

import math
import os
import random
import re
import sys
import requests


#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#

def getTotalGoals(team, year):
    total_goals = 0  # 총 득점을 저장할 변수

    # Helper function to get the total goals from a specific URL
    def get_goals_home_from_url(url):
        nonlocal total_goals  # 바깥 함수의 변수를 수정하기 위해 사용
        page = 1  # 첫 페이지부터 시작
        while True:
            # API 요청
            response = requests.get(url + f"&page={page}")
            data = response.json()  # JSON 응답 파싱

            # 각 경기에서 득점한 골 수를 합산
            for match in data['data']:
                if 'team1goals' in match:  # 홈팀의 득점
                    total_goals += int(match['team1goals'])

            # 모든 페이지를 순회했는지 확인
            if page >= data['total_pages']:
                break  # 마지막 페이지일 경우 종료
            page += 1  # 다음 페이지로 이동

    def get_goals_away_from_url(url):
        nonlocal total_goals  # 바깥 함수의 변수를 수정하기 위해 사용
        page = 1  # 첫 페이지부터 시작
        while True:
            # API 요청
            response = requests.get(url + f"&page={page}")
            data = response.json()  # JSON 응답 파싱

            # 각 경기에서 득점한 골 수를 합산
            for match in data['data']:
                if 'team2goals' in match:  # 홈팀의 득점
                    total_goals += int(match['team2goals'])

            # 모든 페이지를 순회했는지 확인
            if page >= data['total_pages']:
                break  # 마지막 페이지일 경우 종료
            page += 1  # 다음 페이지로 이동

    # 홈팀으로 경기한 모든 데이터 조회
    get_goals_home_from_url(f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}")

    # 원정팀으로 경기한 모든 데이터 조회
    get_goals_away_from_url(f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}")

    return total_goals  # 최종 합산된 득점 반환

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    team = input()

    year = int(input().strip())

    result = getTotalGoals(team, year)

    fptr.write(str(result) + '\n')

    fptr.close()
