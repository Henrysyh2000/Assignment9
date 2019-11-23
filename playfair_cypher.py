# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:52:39 2019

@author: Henry
"""

def play_fair(s):
    #----------------convert the original pair of characters into 
    #the targeted pair------------------------------------
    def convert(CIPHER, node):
        loc = []
        for k in range(2):
            for i in range(len(CIPHER)):
                for j in range(len(CIPHER[i])):
                    if CIPHER[i][j] == node[k]:
                        loc.append([i, j])
        res = ''
        if loc[0][0] == loc[1][0]:
            loc[0][1] += 1
            loc[1][1] += 1
            loc[0][1] %= len(CIPHER)
            loc[1][1] %= len(CIPHER)
            res += CIPHER[loc[0][0]][loc[0][1]]
            res += CIPHER[loc[1][0]][loc[1][1]]
        elif loc[0][1] == loc[1][1]:
            loc[0][0] += 1
            loc[1][0] += 1
            loc[0][0] %= len(CIPHER)
            loc[1][0] %= len(CIPHER)
            res += CIPHER[loc[0][0]][loc[0][1]]
            res += CIPHER[loc[1][0]][loc[1][1]]
        else:
            loc[0][1], loc[1][1] = loc[1][1], loc[0][1]
            res += CIPHER[loc[0][0]][loc[0][1]]
            res += CIPHER[loc[1][0]][loc[1][1]]
        
        return res
            
            
    #------------------handling of the string data----------------------        
    CIPHER = (("P", "L", "A", "Y", "F"), 
              ("I", "R", "E", "X", "M"), 
              ("B", "C", "D", "G", "H"), 
              ("K", "N", "O", "Q", "S"), 
              ("T", "U", "V", "W", "Z"))
    s = s.upper()
    lst = []
    new = []
    res = ''
    for i in range(len(s)):
        if s[i].isalpha():
            lst.append(s[i])
            if i < len(s) - 1:
                if s[i + 1] == s[i]:
                    lst.append('X')
                
    for i in range(len(lst)):
        if lst[i] == 'J':
            lst[i] = 'I'
    if len(lst) % 2 != 0:
        lst.append('X')
    for i in range(len(lst) // 2):
        mid = lst[2*i:2*i+2]
        new += [mid]
    for i in range(len(new)):
        mid = convert(CIPHER, new[i])
        res += mid
    return res


#-----------------------test case------------------------
def main():
    res = play_fair("Do not forget all the deadlines!")
    print(res)
        
if __name__ == "__main__":
    main()