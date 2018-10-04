def mysum(data):
    '''return the sum of the elements of data'''
    result = 0
    for value in data:
        result += value
    return result

def main(m=100000, n=10000):

    # create a list of floats from 0 to m
    data = [float(i) for i in range(m)]

    # compute the sum of the list n times
    result = 0.0
    for _ in range(n):
        result += mysum(data)

    # print summary and exit
    result /= m * n
    print(f'computed the sum of {m} floats {n} times. normalized result={result}')
    return

if __name__ == '__main__':
    main()
