from aoc.helper.loader import collect_arguments, solve_quiz


def main() -> None:
    args = collect_arguments()
    solve_quiz(args.day, args.year)


if __name__ == "__main__":
    main()
