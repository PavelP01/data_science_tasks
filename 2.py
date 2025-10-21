import math

def calc_dist(v1: list[int], v2: list[int]):
    if len(v1) != len(v2):
        print("vectors' sizes should be equal")
        return
    v1_norm = norm(v1)
    v2_norm = norm(v2)
    if (any([v1_norm == 0, v2_norm == 0])):
        print("vectors' norm should not be zero")
        return
    dot_mult = sum([a * b for a, b in zip(v1, v2)])
    return 1 - dot_mult / (v1_norm * v2_norm)

def norm(v: list[int]):
    return math.sqrt(sum([x * x for x in v]))

if __name__ == "__main__":
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    print(calc_dist(v1, v2))