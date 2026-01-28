def mutation_distance(str1: str, str2: str) -> int:
    len_diff = abs(len(str1) - len(str2))
    if len(str1) < len(str2):
        shortest_str = str1
    elif len(str1) > len(str2):
        shortest_str = str2
    else:
        shortest_str = str1 # or str2 since they have equal length
    for index, value in enumerate(shortest_str):
        if str1[index] != str2[index]:
            len_diff += 1
    return len_diff

def generate_variants(mutation: str, diff: int):
    subset = []
    def dfs():
        if mutation_distance("".join(subset), mutation) == diff and len(subset) >= len(mutation):
            print("".join(subset))
        if (len(subset) > (len(mutation) + diff)):
            if mutation_distance("".join(subset), mutation) == diff:
                print("".join(subset))
            return
        for option in "ACTG":
            subset.append(option)
            dfs()
            subset.pop()
    dfs()