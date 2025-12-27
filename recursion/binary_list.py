# def binary_list(n: int) -> list[str]:
#     if n == 0:
#         return [""]
#     else:
#         binary_list_n_min_1 = binary_list(n - 1)
#         binary_list_n_min_1_with_0 = ["0" + x for x in binary_list_n_min_1]
#         binary_list_n_min_1_with_1 = ["1" + x for x in binary_list_n_min_1]
#         return binary_list_n_min_1_with_0 + binary_list_n_min_1_with_1