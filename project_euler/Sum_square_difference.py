def sum_of_first_n_number(n):
    ans = (n*(n+1)) / 2
    print(ans*ans)
    return int(ans*ans)

def sum_of_first_n_number_squre(n):
    mul = n*(n+1)*((2*n)+1)
    print(mul)
    print(mul/n)
    ans = (n*(n+1)*(2*n+1)) / n
    print(ans)
    return ans


def solve(n):
    first_diff  = sum_of_first_n_number(n)
    second_diff = sum_of_first_n_number_squre(n)
    print(first_diff-second_diff)

solve(10)