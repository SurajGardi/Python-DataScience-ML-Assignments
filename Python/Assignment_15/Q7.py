# 7. Write a lambda function using filter() which accepts a list of strings and returns a list of strings
# having length greater than 5.

CheckGreater = lambda string : len(string) > 5

def main():
    Data = ['suraj', 'baramati', 'pune', 'maharashtra', 'india']

    FData = list(filter(CheckGreater, Data))

    print("list of strings having length greater than 5 is : ",FData)


if __name__ == "__main__":
    main()