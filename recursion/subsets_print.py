# def subsets_print(n: int, elements: set[int] = None) -> None:
#     if elements == None:
#         elements = set()
#     if n == 0:
#         print(elements)
#     else:
#         subsets_print(n - 1, elements)
#         subsets_print(n - 1, elements.union({n}))