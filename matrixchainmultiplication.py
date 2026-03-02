def matrix_chain_multiplications(p):
    n = len(p) - 1
    
    dp = [[0]*(n+1) for _ in range(n+1)]

    for l in range(2, n+1):   
        for i in range(1, n-l+2):
            j = i + l - 1
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                q = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]
                
                if q < dp[i][j]:        
                    dp[i][j] = q

    return dp[1][n]


p = [2,10,50,20,4]
print(matrix_chain_multiplications(p))