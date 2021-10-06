import sys

def read_input(file):
    with open(file, 'r') as f:
        contents = f.readlines()
    clauses = []
    for line in contents:
        data = line.split()
        if data[0] == 'c':
            continue
        elif data[0] == 'p':
            vars_num = data[1]
            clauses_num = data[2]
        elif data[0] == '%':
            break
        else:
            clauses.append(data[:-1])

    return clauses

def read_solution(file):
    with open(file, 'r') as f:
        content = f.readlines()
    solution = []
    for line in content:
        data = line.split()
        if data[0] == 'c':
            continue
        elif data[0] == 'v' and data[1]!='0':
            for num in data[1:]:
                solution.append(num)

    return solution

def clause_counter(clauses, solution):
    counter = 0
    for c in clauses:
        if len(set(c).intersection(set(solution)))==0 :
            counter+=1

    return counter


if __name__ == '__main__':
    input_file = sys.argv[1]
    solution_file = sys.argv[2]

    clauses = read_input(input_file)
    sol = read_solution(solution_file)
    output = clause_counter(clauses, sol)
    print(f"Number of Unsatisfied clauses: {output}")

        