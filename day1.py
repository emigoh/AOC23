import re

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    sanitizedInput = [re.sub(r"[^\d]", "", string) for string in lines]
    # print(sanitizedInput)
    number = list_to_number(sanitizedInput)
    print(number)

def list_to_number(string_list):
    i=0
    sum=0
    while i < len(string_list):
        num_text = string_list[i][0] + string_list[i][len(string_list[i])-1]
        num = int(num_text)
        sum+= num
        i+=1

    return sum






main()