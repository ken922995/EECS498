#!/usr/bin/env python

import numpy as np

def solve_matrix(A,b):
    try:
        return np.linalg.solve(A,b)
    except np.linalg.LinAlgError:
        print("The matrix is singular, it can't be solved!")
def main():
    
    #Q5
    print("Q5\n")
    A_5a = np.array([[0,0,-1],[4,1,1],[-2,2,1]])
    b_5a = np.array([3,1,1])
    A_5b = np.array([[0,-2,6],[-4,-2,-2],[2,1,1]])
    b_5b = np.array([1,-2,0])
    A_5c = np.array([[2,-2],[-4,3]])
    b_5c = np.array([3,-2])
    print("(a) x = ")
    print (solve_matrix(A_5a,b_5a))
    print("(b) x = ")
    print (solve_matrix(A_5b,b_5b))
    print("(c) x = ")
    print (solve_matrix(A_5c,b_5c))
    print("")
    print("---------------------------------------")
    print("Q6\n")
    #Q6
    A_6 = np.array([[3,2],[1,-2]])
    B_6 = np.array([[-1,-2],[4,-2]])
    print ("(a)")
    print ("A + 2B =")
    print (A_6+2*B_6)
    print("")
    print ("(b)")
    print ("AB =")
    print (A_6.dot(B_6)) 
    print ("BA =") 
    print (B_6.dot(A_6))
    print("")
    print ("(c)")
    print ("At =")
    print (A_6.T)
    print("")
    print ("(d)")
    print ("BB =")
    print (B_6.dot(B_6))
    print("")
    print ("(e)")
    print ("AtBt =")
    print (A_6.T.dot(B_6.T))
    print ("(AB)t =")
    print ((A_6.dot(B_6)).T)
    print("")
    print ("(f)")
    print ("det(A) =")
    print (np.linalg.det(A_6))
    print("")
    print ("(g)")
    print ("B inv =")
    print (np.linalg.inv(B_6))
    print("")

if __name__ == "__main__":
    main()