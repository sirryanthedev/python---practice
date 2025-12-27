# (ex. 3.9. - leetcode 282 equivalent)

def sum_to_100(digits="123456789"):
    def dfs(pos: int, expr: str, total: int, last: int):
        if pos == len(digits):
            if total == 100:
                print(expr)
            return

        for i in range(pos + 1, len(digits) + 1):
            num_str = digits[pos:i]
            num = int(num_str)

            if pos == 0:
                # first number, must be positive
                dfs(i, num_str, num, num)
            else:
                # add '+'
                dfs(i, expr + "+" + num_str, total + num, num)
                # add '-'
                dfs(i, expr + "-" + num_str, total - num, -num)
                # concatenate last number
                new_last = int(str(abs(last)) + num_str)
                if last >= 0:
                    dfs(i, expr + num_str, total - last + new_last, new_last)
                else:
                    dfs(i, expr + num_str, total - last - new_last, -new_last)

    dfs(0, "", 0, 0)