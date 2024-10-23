#!/bin/python3

import math
import os
import random
import re
import sys
import requests


#
# Complete the 'getNumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
#

def getNumDraws(year):
    # Write your code here
    total_draws_game = 0

    def get_draw_game_from_url(url):
        nonlocal total_draws_game
        page = 1
        while True:
            response = requests.get(url + f"&page={page}")
            data = response.json()

            for match in data['data']:
                if match['team1goals'] == match['team2goals']:
                    total_draws_game += 1
            if data['total_pages'] == page:
                break
            page+=1
        return total_draws_game

    get_draw_game_from_url(f"https://jsonmock.hackerrank.com/api/football_matches?year={year}")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = getNumDraws(year)

    fptr.write(str(result) + '\n')

    fptr.close()
