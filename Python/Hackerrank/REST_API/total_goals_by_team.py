#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#
import requests


def get_home_team_goals(team, year):
    goal_cnt = 0
    page_number = 1

    HOME_TEAM_URL = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page="

    result = requests.get(HOME_TEAM_URL + str(page_number)).json()

    per_page = result["per_page"]
    total = result["total"]
    total_pages = result["total_pages"]

    for data in result["data"]:
        goal_cnt += int(data["team1goals"])

    for page_number in range(2, total_pages + 1):
        result = requests.get(HOME_TEAM_URL + str(page_number)).json()

        for data in result["data"]:
            goal_cnt += int(data["team1goals"])

    return goal_cnt


def get_away_team_goals(team, year):
    goal_cnt = 0
    page_number = 1

    AWAY_TEAM_URL = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page="

    result = requests.get(AWAY_TEAM_URL + str(page_number)).json()

    per_page = result["per_page"]
    total = result["total"]
    total_pages = result["total_pages"]

    for data in result["data"]:
        goal_cnt += int(data["team2goals"])

    for page_number in range(2, total_pages + 1):
        result = requests.get(AWAY_TEAM_URL + str(page_number)).json()

        for data in result["data"]:
            goal_cnt += int(data["team2goals"])

    return goal_cnt


def getTotalGoals(team, year):
    return get_home_team_goals(team, year) + get_away_team_goals(team, year)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    team = input()

    year = int(input().strip())

    result = getTotalGoals(team, year)

    fptr.write(str(result) + '\n')

    fptr.close()
