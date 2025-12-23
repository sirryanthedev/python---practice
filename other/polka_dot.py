# (ex. Polka Dot - Dodona)

def polka(input_list) -> list:
    end_list = [None for _ in range(len(input_list))]

    if not isinstance(input_list, list):
        input_list = list(input_list)

    empty_value = 2
    full_break = False

    # if len(input_list) == 1:
        # return

    while True:
        for index, value in enumerate(end_list):
            if value is None and empty_value != 2:
                empty_value += 1
            if empty_value == 2 and len(input_list) > 0:
                end_list[index] = input_list[0]
                del input_list[0]
                empty_value = 0
            elif value is None and len(input_list) == 1:
                end_list[index] = input_list[0]
                full_break = True
                break
        if full_break:
            break

    return end_list

def delen(input_list) -> list:
    if not isinstance(input_list, list):
        input_list = list(input_list)

    end_list = []

    while len(input_list) > 0:
        end_list.append(input_list[0])
        del input_list[0]

        if len(input_list) > 0:
            input_list.append(input_list[0])
            del input_list[0]

    return end_list