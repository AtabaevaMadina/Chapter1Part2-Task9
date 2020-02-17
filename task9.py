num_n = int(input('Input an integer N = '))
count = 1
for i in range(1, num_n + 1):
    count *= i
    # print(i)
    print('FACTORIAL = {}'.format(count) )