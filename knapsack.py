#knapsack problem. Algorithmic Thinking with Python: Diving Deeper Dynamic Programming challenge
from tabulate import tabulate

def knapsack(max_capacity,weight,value):
    
    num_items = len(value)
    
    result_tb = [[0 for _ in range(max_capacity+3)]for _ in range(num_items+1)]
    
    for i in range(num_items+1):      
        for j in range(max_capacity+3):
            if j == 2 or i == 0:
                result_tb[i][j] = 0
            elif weight[i-1] <= j-2:
                result_tb[i][j] = max(result_tb[i-1][j] , value[i-1] + result_tb[i-1][j-weight[i-1]])
            elif j > 2:
                result_tb[i][j] = result_tb[i-1][j]

        if i+1 <= len(weight):
                    result_tb[i+1][0] = weight[i]
                    result_tb[i+1][1] = value[i]            
    
        
    result_tb[0][0] = 'w'
    result_tb[0][1] = 'v'

    print(tabulate(result_tb,tablefmt='pretty'))
    return result_tb[num_items][max_capacity+2]
#     print(result_tb)

print(knapsack(6,[1,2,3,5],[10,5,20,35]))