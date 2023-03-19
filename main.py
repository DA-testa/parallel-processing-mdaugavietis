# python3

def parallel_processing(n, m, data):
    output = []

    # thread tiems
    thread = [0] * n

    job = 0
    time_elapsed = 0
    # start simulation
    while job < m:
        # step of time forward
        step = 10**9

        for num, time in enumerate(thread):
            # check free threads
            if (time <= 0):
                output.append((num, time_elapsed))
                thread[num] = data[job]
                job += 1

            # find the timestep value
            if thread[num] < step:
                step = thread[num]
        # do the time step
        for num, time in enumerate(thread):
            thread[num] = time - step
        time_elapsed += step
    return output

def main():
    # n - thread count 
    # m - job count
    [n, m] = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    result = parallel_processing(n,m,data)
    
    for i, j in result:
        print(i, j)



if __name__ == "__main__":
    main()
