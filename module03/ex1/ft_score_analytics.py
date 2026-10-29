#!/usr/bin/env python3
import sys


def ft_score_analytics() -> None:

    print("=== Player Score Analytics ===")
    scores: list[int] = []
    for args in sys.argv[1::]:
        try:
            scores.append(int(args))
        except ValueError:
            print(f"Invalid parameter: '{args}'")
    if not len(scores):
        print("No scores provided. Usage: python3"
              " ft_score_analytics.py <score1> <score2> ...")
        print()
        return

    print("Scores processed:", scores)
    print("Total players:", len(scores))
    print("Total score:", sum(scores))
    print("Average score:", sum(scores) / len(scores))
    print("High score:", max(scores))
    print("Low score:", min(scores))
    print("Score range:", max(scores) - min(scores))
    print()


if __name__ == "__main__":
    ft_score_analytics()
