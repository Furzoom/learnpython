#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_input(s):
    while True:
        score = raw_input("Input score(<ENTER to stop>): ")
        if len(score.strip()) <= 0:
            break
        s.append(float(score))

    return s


def get_average(s):
    return sum(s) / len(s)


def get_rating(s):
    if s > 100 or s < 0:
        return None
    elif s >= 90:
        return 'A'
    elif s >= 80:
        return 'B'
    elif s >= 70:
        return 'C'
    elif s >= 60:
        return 'D'
    else:
        return 'E'


def main():
    scores = []
    get_input(scores)
    print 'Average is', get_average(scores)
    for x in scores:
        print get_rating(x)


if __name__ == '__main__':
    main()
