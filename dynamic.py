def dynamic_max_stocks(N, stock_values, amount):
    # placeholder for sub arrays
    dp = [[0] * (amount + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(amount + 1):
            stocks, value = stock_values[i - 1]
            if value > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - value] + stocks)

    return dp[N][amount]
    
def read_input_from_file(file_path):
    # split up input into seperate instances
    instances = []
    with open(file_path, 'r') as file:
        while True:
            N_line = file.readline()
            if not N_line:
                break
            while N_line.isspace():
                N_line = file.readline().strip()
            N = int(N_line.strip())
            stocks_values_str = file.readline().strip()
            if stocks_values_str.isspace():
                continue
            # get values by splitting up the lines
            stocks_values = [list(map(int, stock.strip('[]').split(','))) for stock in stocks_values_str[1:-1].split('],[')]
            amount = int(file.readline().strip())
            instances.append((N, stocks_values, amount))
    return instances

# read from input file to get input
file_path = 'input_project2.txt'
instances = read_input_from_file(file_path)

# call dp max_stocks for each instamce set
for i, (instance_N, stocks_values, amount) in enumerate(instances, start=1):
    result = dynamic_max_stocks(instance_N, stocks_values, amount)
    print(f"Input #{i}: {result}")
