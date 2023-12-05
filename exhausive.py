def exhausive(amount, stock_values):
    best = None
    for candidates in combinations(stock_values):
        if verify(amount, stock_values, candidates):
            if best is None or total_value(candidates) > total_value(best):
                best = candidates
    return best
        
def combinations(stock_values):
    n = len(stock_values)
    subset_size = 2**n
    new_list = []
    for i in range(subset_size):
        join = []
        for j in range(n):
            if (i >> j) & 1:
                join.append(stock_values[j])
        new_list.append(join)
    return new_list

def verify(amount, stock_values, candidates):
    total_amount = 0
    total_stock = 0
    for item in candidates:
        total_amount += item[1]
        total_stock += item[0]
    if total_amount <= amount and total_stock <= amount:
        return True
    else:
        return False
        
def total_value(candidates):
    total_value = 0
    for item in candidates:
        total_value += item[1]
    return total_value
    
def read_input_from_file(file_path):
    # split up input into seperate instances
    instances = []
    with open(file_path, 'r') as file:
        while True:
            N_line = file.readline()
            if not N_line:
                break
            N = int(N_line.strip())
            stocks_values_str = file.readline().strip()
            stocks_values = [list(map(int, stock.strip('[]').split(','))) for stock in stocks_values_str[1:-1].split('],[')]
            amount = int(file.readline().strip())
            instances.append((N, stocks_values, amount))
    return instances
    
# read from input file to get input
file_path = 'input_project2.txt'
instances = read_input_from_file(file_path)

# open output file
output_file = open('output.txt', 'w')

# call dp max_stocks for each instamce set
for i, (instance_N, stocks_values, amount) in enumerate(instances, start=1):
    result = exhausive(amount, stocks_values)
    total_sum = 0
    for value in result:
        total_sum += value[0]
    output_file.write(f"Input #{i}: {total_sum}\n")

output_file.close()
