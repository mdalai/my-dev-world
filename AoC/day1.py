


def read_file(filepath):
    lines = []
    with open(filepath) as f:
        lines = f.read().splitlines()
    return lines

def get_expense(input_arr):
    """a+b=2020"""
    p =[]

    for i in range(len(input_arr)):
        for j in range(i, len(input_arr)):
            if ( i != j and input_arr[i] + input_arr[j] == 2020):
                p.append(input_arr[i]*input_arr[j])

    return max(p)

def get_expense3(input_arr):
    """a+b+c=2020"""
    p =[]

    for i in range(len(input_arr)):
        for j in range(i, len(input_arr)):
            for k in range(j, len(input_arr)):
                if ( i != j and j!=k and k!=i and input_arr[i] + input_arr[j] + input_arr[k]== 2020):
                    p.append(input_arr[i]*input_arr[j]*input_arr[k])

    return max(p)


def main():
    vals = read_file('day1_input.txt')
    results = list(map(int, vals))
    val = get_expense3(results)
    print(val)

    

if __name__ == "__main__":
    main()
