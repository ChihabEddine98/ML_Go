

import math



# This function takes a sequent of numbers `seq` and 
# returns the length of the longest increasing subsequent
# for example : [5,2,8,6,3,6,5] => 
def lis_solver(seq):
    L = [1]*len(seq)
    
    for i in range(1,len(L)):
        sub_problems = [L[k] for k in range(i) if seq[k] < seq[i]]
        print(sub_problems)
        L[i] = 1 + max(sub_problems,default=0)
    
    return max(L,default=0)


if __name__ == '__main__':
    seq = [5,2,8,6,3,6,5]
    print(f'The Longest increasing subsequent in {seq} has length {lis_solver(seq)}')
    