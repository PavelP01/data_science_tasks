def calc_diff(sqs: list[str]):
    wd = {}
    for sq in sqs:
        sq_count = len(sq.split(" "))
        count = wd.get(sq_count)
        if count is None:
            wd[sq_count] = 1
        else:
            wd[sq_count] = count + 1
    sorted_wd = dict(sorted(wd.items()))
    for k, v in sorted_wd.items():
        freq = round(100 * v / len(sqs))
        if k % 10 == 1 & k != 11:
            print(f"{k} слово: {freq}%")
            continue
        if (k % 10 in [2, 3, 4]) & (k not in [12, 13, 14]):
            print(f"{k} слова: {freq}%")
            continue
        print(f"{k} слов: {freq}%")


if __name__ == "__main__":
    search_queries = [
        "watch new movies",
        "coffee near me",
        "how to find the determinant",
        "python",
        "data science jobs in UK",
        "courses for data science",
        "taxi",
        "google",
        "yandex",
        "bing",
        "foreign exchange rates USD / BYN",
        "Netflix movies watch online free",
        "Statistics courses online from top universities"
    ]
    calc_diff(search_queries)