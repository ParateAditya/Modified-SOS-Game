def fun(matrix , N ,  r1 , c1):
    p_score = [0,0]
    if matrix[r1][3+(c1-1)*2]=='S' :
        if r1+2 <= N and c1+2 <= N :
            if (matrix[r1+1][3+2*(c1-1)+2] == p1_choice or matrix[r1+1][3+2*(c1-1)+2] == p2_choice) and matrix[r1+2][3+2*(c1-1)+2+2] == 'S':
                if matrix[r1+1][3+2*(c1-1)+2] == p1_choice:
                    p_score[0] += 1 
                else :
                    p_score[1] += 1
            
            if (matrix[r1+1][3+(c1-1)*2] == p1_choice or matrix[r1+1][3+(c1-1)*2] == p2_choice) and matrix[r1+2][3+(c1-1)*2]=='S' :
                if matrix[r1+1][3+(c1-1)*2] == p1_choice:
                    p_score[0] += 1 
                else :
                    p_score[1] += 1
            if (matrix[r1][3+2*(c1-1)+2] == p1_choice or matrix[r1][3+2*(c1-1)+2] == p2_choice) and matrix[r1][3+2*(c1-1)+2+2] == 'S':
                if matrix[r1][3+2*(c1-1)+2] == p1_choice:
                    p_score[0] += 1 
                else :
                    p_score[1] += 1
        elif r1-2 >0 and c1+2 <= N :
            if (matrix[r1-1][3+2*(c1-1)+2] == p1_choice or matrix[r1-1][3+2*(c1-1)+2] == p2_choice) and matrix[r1-2][3+2*(c1-1)+2+2] == 'S':
                if matrix[r1-1][3+2*(c1-1)+2] == p1_choice:
                    p_score[0] += 1 
                else :
                    p_score[1] += 1
            if (matrix[r1][3+2*(c1-1)+2] == p1_choice or matrix[r1][3+2*(c1-1)+2] == p2_choice) and matrix[r1][3+2*(c1-1)+2+2] == 'S':
                if matrix[r1][3+2*(c1-1)+2] == p1_choice:
                    p_score[0] += 1 
                else :
                    p_score[1] += 1
            if (matrix[r1-1][3+(c1-1)*2] == p1_choice or matrix[r1-1][3+(c1-1)*2] == p2_choice) and matrix[r1-2][3+(c1-1)*2] == 'S':
                if matrix[r1-1][3+(c1-1)*2] == p1_choice:
                    p_score[0] += 1 
                else :
                    p_score[1] += 1
        elif r1-2 > 0 and c1-2>0 :
            if (matrix[r1-1][3+2*(c1-1)-2] == p1_choice or matrix[r1-1][3+2*(c1-1)-2] == p2_choice) and matrix[r1-2][3+2*(c1-1)-4] == 'S':
                if matrix[r1-1][3+2*(c1-1)-2] == p1_choice:
                    p_score[0] += 1 
                else :
                    p_score[1] += 1
            if (matrix[r1-1][3+(c1-1)*2] == p1_choice or matrix[r1-1][3+(c1-1)*2] == p2_choice) and matrix[r1-2][3+(c1-1)*2] == 'S':
                if matrix[r1-1][3+(c1-1)*2] == p1_choice:
                    p_score[0] += 1 
                else :
                    p_score[1] += 1
            if (matrix[r1][3+2*(c1-1)-2] == p1_choice or matrix[r1][3+2*(c1-1)-2] == p2_choice) and matrix[r1][3+2*(c1-1)-2-2]=='S':
                if matrix[r1][3+2*(c1-1)-2] == p1_choice:
                    p_score[0] += 1 
                else :
                    p_score[1] += 1
        elif r1+2 < N and c1-2 > 0 :
            if (matrix[r1+1][3+2*(c1-1)-2] == p1_choice or matrix[r1+1][3+2*(c1-1)-2] == p2_choice) and matrix[r1+2][3+2*(c1-1)-4]:
                if matrix[r1+1][3+2*(c1-1)-2] == p1_choice:
                    p_score[0] += 1 
                else :
                    p_score[1] += 1
            if (matrix[r1+1][3+(c1-1)*2] == p1_choice or matrix[r1+1][3+(c1-1)*2] == p2_choice) and matrix[r1+2][3+(c1-1)*2]=='S' :
                if matrix[r1+1][3+(c1-1)*2] == p1_choice:
                    p_score[0] += 1 
                else :
                    p_score[1] += 1
            if (matrix[r1][3+2*(c1-1)-2] == p1_choice or matrix[r1][3+2*(c1-1)-2] == p2_choice) and matrix[r1][3+2*(c1-1)-2-2]=='S':
                if matrix[r1][3+2*(c1-1)-2] == p1_choice:
                    p_score[0] += 1 
                else :
                    p_score[1] += 1
        elif r1+2 <= N :
            if (matrix[r1+1][3+(c1-1)*2] == p1_choice or matrix[r1+1][3+(c1-1)*2] == p2_choice) and matrix[r1+2][3+(c1-1)*2]=='S' :
                if matrix[r1+1][3+(c1-1)*2] == p1_choice:
                    p_score[0] += 1 
                else :
                    p_score[1] += 1
        elif r1-2 > 0:
            if (matrix[r1-1][3+(c1-1)*2] == p1_choice or matrix[r1-1][3+(c1-1)*2] == p2_choice) and matrix[r1-2][3+(c1-1)*2] == 'S':
                if matrix[r1-1][3+(c1-1)*2] == p1_choice:
                    p_score[0] += 1 
                else :
                    p_score[1] += 1
        elif c1-2 >0 :
            if (matrix[r1][3+2*(c1-1)-2] == p1_choice or matrix[r1][3+2*(c1-1)-2] == p2_choice) and matrix[r1][3+2*(c1-1)-2-2]=='S':
                if matrix[r1][3+2*(c1-1)-2] == p1_choice:
                    p_score[0] += 1 
                else :
                    p_score[1] += 1
        elif c1+2 <= N :
            if (matrix[r1][3+2*(c1-1)+2] == p1_choice or matrix[r1][3+2*(c1-1)+2] == p2_choice) and matrix[r1][3+2*(c1-1)+2+2] == 'S':
                if matrix[r1][3+2*(c1-1)+2] == p1_choice:
                    p_score[0] += 1 
                else :
                    p_score[1] += 1
    
    elif (c1==1 or c1==N) and (r1>1 and r1<N) :
        if (matrix[r1][3+(c1-1)*2]==p1_choice or matrix[r1][3+(c1-1)*2]==p2_choice) and matrix[r1-1][3+(c1-1)*2]=='S' and matrix[r1+1][3+(c1-1)*2]=='S' :
            if matrix[r1][3+(c1-1)*2]==p1_choice :
                p_score[0] += 1 
            else :
                p_score[1] += 1
        
    elif (r1==1 or r1==N) and (c1>1 and c1<N) :
        if (matrix[r1][3+(c1-1)*2]==p1_choice or matrix[r1][3+(c1-1)*2]==p2_choice) and matrix[r1][3+(c1-1)*2-2]=='S' and matrix[r1][3+(c1-1)*2+2]=='S' :
            if matrix[r1][3+(c1-1)*2]==p1_choice :
                p_score[0] += 1 
            else :
                p_score[1] += 1
    
    elif ((r1==1 or r1==N) and (c1==1 or c1==N)) :
        if matrix[r1][3+(c1-1)*2]=='O' or matrix[r1][3+(c1-1)*2]=='L':
            pass
        
    elif matrix[r1][3+(c1-1)*2]=='O' or matrix[r1][3+(c1-1)*2]=='L':
        if (matrix[r1-1][3+(c1-1)*2]=='S' and matrix[r1+1][3+(c1-1)*2]=='S') or (matrix[r1][3+(c1-1)*2-2]=='S' and matrix[r1][3+(c1-1)*2+2]=='S') or (matrix[r1-1][3+(c1-1)*2-2]=='S' and matrix[r1+1][3+(c1-1)*2+2]=='S') or (matrix[r1+1][3+(c1-1)*2-2]=='S' and matrix[r1-1][3+(c1-1)*2+2]=='S'):
            if matrix[r1][3+(c1-1)*2]==p1_choice :
                p_score[0] += 1 
            else :
                p_score[1] += 1

    else:
         return -1

    return p_score

N = int(input("Enter the size of the board :\n"))

p1 = input("ENter name of player 1 : ")
p2 = input("ENter name of player 2 : ")

print(p1,", enter your choice O/L : ")

p1_choice = input()
if p1_choice=='O' or p1_choice=='o':
    p2_choice = 'L'
else :
    p2_choice = 'O'

global p1_score
global p2_score
p1_score = 0
p2_score = 0

matrix = []

for i in range(0,N+1):
    a = []
    for j in range(0 , (N+1)+(N+2)):
        if j%2==0:
            a.append('|')
        elif i>0 and j==1:
            a.append( i)
        
        elif i==0 and j>=3:
            if j%2==1:
                a.append(1+int((j-3)/2))
        else :
            a.append(' ')
    matrix.append(a)
        
        
matrix[0][1]='X'  

# for i in range(0,N+1):
#     for j in range(0 , (N+1)+(N+2)):
#         print(matrix[i][j] ,end =  " ")
#     print()



print('----------------------------------------------------')
print(p1+"'s choice : "+p1_choice+"      Score of "+p1+" : ",p1_score)
print(p2+"'s choice : "+p2_choice+"      Score of "+p2+" : ",p2_score)
print('----------------------------------------------------')
print()

print('----------------------------------------------------')

for k in range(0,N+1):
    for j in range(0 , (N+1)+(N+2)):
        print(matrix[k][j] ,end =  " ")
    print()   
    
print('----------------------------------------------------')


for i in range(1,N*N + 1):
    if i%2==1:
        print()
        print("Your move" , p1 , ": ")
        print("Choose" , p1_choice ,"or S :" , end = " ")
        choose_char = input()
        r1 = int(input("Enter row number : "))
        c1 = int(input("Enter column number : "))
        matrix[r1][3+2*(c1-1)] = choose_char
        z = fun(matrix , N   , r1 , c1)
        p1_score += z[0]*10 
        p2_score += z[1]*10 
    else:
        print()
        print("Your move" , p2 , ": ")
        print("Choose" , p2_choice ,"or S :" , end = " ")
        choose_char = input()
        r1 = int(input("Enter row number : "))
        c1 = int(input("Enter column number : "))
        matrix[r1][3+2*(c1-1)] = choose_char
        z = fun(matrix , N   , r1 , c1)
        p1_score += z[0]*10 
        p2_score += z[1]*10
    
    print()
    print('------------------------------------------------')
    print(p1+"'s choice : "+p1_choice+"      Score of "+p1+" : ",p1_score)
    print(p2+"'s choice : "+p2_choice+"      Score of "+p2+" : ",p2_score)
    print('------------------------------------------------')
    print() 
 
    print('------------------------------------------------')
    for k in range(0,N+1):
        for j in range(0 , (N+1)+(N+2)):
            print(matrix[k][j] ,end =  " ")
        print()   
    
    print('------------------------------------------------')


if p1_score > p2_score :
    print(p1 , "You Won !!")
elif p1_score < p2_score:
    print(p2 , "You Won !!")
else:
    print("Match tied")