import os
from random import randint

clear = lambda: os.system('cls')
import time


def chunk_test(chunk_size=3, chunk_numbers=2):
    clear = "\n" * 100
    center = "\n" * 15
    chunks = []
    print(clear)

    for i in range(0, chunk_numbers):
        rand_value = 0
        while rand_value < 100:
            rand_value = randint(0, pow(10, chunk_size) - 1)
        chunks.append(rand_value)

    text = ""

    for chunk in chunks:
        text += " " + str(chunk)

    print(text)
    print(center)
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


chunk_numbers = 3
chunk_size = 3
initial_time = time.time()
results_good = 0
results_bad = 0
continue_game = "y"
games = 0
time_sum = 0
input("start enter")
while continue_game != "n":
    games += 1
    r, t = chunk_test(chunk_numbers=chunk_numbers, chunk_size=chunk_numbers
                      )
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
print("final score:")
print(str(chunk_size) + "," + str(chunk_numbers) + "," + str(games) + "," + str(results_good) + "," + str(
    games - results_good) + "," + str(minutes_b)
      + "," + str(round(time_sum / games, 2)) + "," + str(round(results_good / (games), 4) * 100))
