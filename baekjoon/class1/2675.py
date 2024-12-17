n_testcase = int(input())

testcases = []
for i in range(n_testcase):
    n, case = map(str, input().split())
    n = int(n)
    testcases.append([n, case])
    
for item in testcases:
    n, case = item
    message = ''
    for i in case:
        message = message + i*n
    print(message)