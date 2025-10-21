def extract_even(input: list[int]):
    filtered = [x for x in set(input) if x % 2 == 0]
    filtered.sort(reverse = True)
    return filtered

if __name__ == "__main__":
    l = [4, 1, 10, 1, 2, 3, 102, 4, 9]
    print(extract_even(l))