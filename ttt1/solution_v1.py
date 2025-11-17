# ----------OPGAVE1----------

# example = input("enter data in mentioned format: ")       # e.g.: "Louis De Smet,10,14,A,13;"

# is_name = True
# name = ""

# current_num = ""
# total_score = 0
# number_of_courses = 0

# for char in example:

#     if is_name:
#         if char == ",":
#             is_name = False
#         else:
#             name += char

#     elif ord("0") <= ord(char) <= ord("9"):
#         current_num += char
    
#     elif char == "," and current_num != "":
#         total_score += int(current_num)
#         current_num = ""
#         number_of_courses += 1
    
#     elif char == ";" and current_num != "":
#         total_score += int(current_num)
#         number_of_courses += 1

# if number_of_courses == 0:
#     print(f"{name},0,0")
# else:
#     print(f"{name},{number_of_courses},{total_score},{total_score/number_of_courses:.2f}")

# ------------------------------------------------------------------------------------------






# ----------OPGAVE2----------

# example = input("enter data in mentioned format: ")         # e.g.: "Frank Neven,7;Hendrik Ivers,0;Jeroen Bollen,8,9;"

# current_num = ""
# total_score = 0
# number_of_courses = 0

# for char in example:

#     if ord("0") <= ord(char) <= ord("9"):
#         current_num += char
    
#     elif char == "," and current_num != "":
#         total_score += int(current_num)
#         current_num = ""
#         number_of_courses += 1
    
#     elif char == ";" and current_num != "":
#         total_score += int(current_num)
#         current_num = ""
#         number_of_courses += 1

# if number_of_courses == 0:
#     print(f"{number_of_courses},{total_score}")
# else:
#     print(f"{number_of_courses},{total_score},{total_score/number_of_courses:.2f}")

#------------------------------------------------------------------------------------