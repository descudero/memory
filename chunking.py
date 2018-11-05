import os
from random import randint

clear = lambda: os.system('cls')
import time


def chunk_test(chunk_size=3, chunk_numbers=2):
    clear = "\n" * 100
    results_good = 0
    results_bad = 0
    chunks = []

    for i in range(0, chunk_numbers):
        chunks.append(randint(0, pow(10, chunk_size) - 1))

    text = ""

    for chunk in chunks:
        text += " " + str(chunk)

    print(text)
    start = time.time()
    input("memorize en press any key")
    print(clear)
    results = []
    end = time.time()
    time_lapse = end - start
    result = 1
    for chunk in chunks:
        data = input("enter data:")
        results.append(str(chunk) == str(data))
        if result == 1 and str(chunk) != str(data):
            result = 0
    print(results)
    print(chunks)
    return result, time_lapse


initial_time = time.time()
results_good = 0
results_bad = 0
continue_game = "y"
games = 0
time_sum = 0
input("start enter")
while continue_game != "n":
    games += 1
    r, t = chunk_test(chunk_numbers=3)
    results_good += r
    time_sum += t
    minutes_b = (time.time() - initial_time) / 60
    print("GOODD!!! " if r else "BADD!!!!")
    print(
        "games " + str(games) + " so far good " + str(results_good) + " bad " + str(games - results_good) + " % " + str(
            round(results_good / (games), 4) * 100), " time lapse " + str(round(t, 2)))
    print("AVG TIME " + str(round(time_sum / games, 2)))
    print("minutes by " + str(minutes_b))
    continue_game = input("continue chunking practice?")
