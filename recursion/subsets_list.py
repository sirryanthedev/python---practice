# def subsets(n: int) -> list[set[int]]:
#     if n == 0:
#         return [set()]
#     else:
#         subsets_n_min_1 = subsets(n - 1)
#         return subsets_n_min_1 + [x | {n} for x in subsets_n_min_1]