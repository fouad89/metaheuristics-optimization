
import sys

f_name = "/Users/spydermac/My Drive/AI-Masters/Term 1/Metaheuristics/Lab5/Inst/uf20-01.cnf"
def readInstance(fName):
    file        = open(fName, 'r')
    tVariables  = -1
    tClauses    = -1
    clause      = []
    variables   = []

    current_clause = []

    for line in file:
        data = line.split()

        if len(data) == 0:
            continue
        if data[0] == 'c':
            continue
        if data[0] == 'p':
            tVariables  = int(data[2])
            tClauses    = int(data[3])
            continue
        if data[0] == '%':
            break
        if tVariables == -1 or tClauses == -1:
            print ("Error, unexpected data")
            sys.exit(0)

        ##now data represents a clause
        for var_i in data:
            literal = int(var_i)
            if literal == 0:
                clause.append(current_clause)
                current_clause = []
                continue
            var = literal
            if var < 0:
                var = -var
            if var not in variables:
                variables.append(var)
            current_clause.append(literal)

    if tVariables != len(variables):
        print ("Unexpected number of variables in the problem")
        print ("Variables", tVariables, "len: ",len(variables))
        print (variables)
        sys.exit(0)
    if tClauses != len(clause):
        print ("Unexpected number of clauses in the problem")
        sys.exit(0)
    file.close()
    return [variables, clause]

# print ("File: ",sys.argv[1])
sat = readInstance(f_name)
print(sat[1])

from genetic import genetic

genetic(sat[1],20,50,1000,0.2)