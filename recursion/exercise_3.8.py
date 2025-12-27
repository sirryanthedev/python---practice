def thanoi(n, source: list, source_name: str,  target: list, target_name: str, spare: list, spare_name: str):
    # base case: stop if n(umber of disks) is equal to 0
    if n == 0:
        return
    
    thanoi(n - 1, source, source_name, spare, spare_name, target, target_name)
    
    disk = source.pop()
    target.append(disk)

    print(f"Schijf {disk} van {source_name} naar {target_name}.")

    thanoi(n - 1, spare, spare_name, target, target_name, source, source_name)

# function call, e.g. for n = 3

# n = 3  number of disks
# A = [num for num in range(n, 0, -1)] # [3, 2, 1] = source list
# B = [] spare list
# C = [] target list
# thanoi(n, A, "A", C, "C", B, "B")

# output:
# Schijf 1 van A naar C.
# Schijf 2 van A naar B.
# Schijf 1 van C naar B.
# Schijf 3 van A naar C.
# Schijf 1 van B naar A.
# Schijf 2 van B naar C.
# Schijf 1 van A naar C.