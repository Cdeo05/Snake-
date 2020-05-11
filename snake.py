from os import system, name 
from time import sleep 
import keyboard
import random


matrix=[]
initialpos=[[5,5],[5,6],[5,7],[5,8]]
rows=20
cols=40
movement=['d']*len(initialpos)
key='d'
f1=0
f2=0
def move():
    updated=[]
    for i in range(len(initialpos)):
        if(movement[i]=='d'):
            initialpos[i][1]=initialpos[i][1]+1
        if(movement[i]=='a'):
            initialpos[i][1]=initialpos[i][1]-1
        if(movement[i]=='w'):
            initialpos[i][0]=initialpos[i][0]-1
        if(movement[i]=='s'):
            initialpos[i][0]=initialpos[i][0]+1

def clear_matrix():
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            matrix[i][j]=0

def initialize_matrix(rows,cols):
    global matrix
    matrix= [[0 for i in range(cols)] for j in range(rows)] 

    for j in range(cols):
        matrix[0][j]='-'
        matrix[rows-1][j]='-'

    for i in range(rows):
        matrix[i][0]='|'
        matrix[i][cols-1]='|'

    

def print_matrix():
    clear_matrix()
    matrix[f1][f2]='o'
    for i in initialpos:
        matrix[i[0]][i[1]]='*'

    for i in matrix:
        for j in range(len(i)):
            if(i[j]==0):
                print(" ",end="")
            else:
                print(i[j],end="")
            
            
        print()
    
    sleep(0.1)

def clear(): 
    _ = system('cls') 

def check():
    if(initialpos[-1][0]==f1 and initialpos[-1][1]==f2):
        food()
        if(movement[0]=='d'):
            initialpos.insert(0,[initialpos[0][0],initialpos[0][1]-1])
        if(movement[0]=='w'):
            initialpos.insert(0,[initialpos[0][0]+1,initialpos[0][1]])
        if(movement[0]=='a'):
            initialpos.insert(0,[initialpos[0][0],initialpos[0][1]+1])
        if(movement[0]=='s'):
            initialpos.insert(0,[initialpos[0][0]-1,initialpos[0][1]])   
        movement.insert(0,movement[0])
    if(initialpos[-1][0]==rows-1 or initialpos[-1][0]==0):
        return True
    if(initialpos[-1][1]==cols-1 or initialpos[-1][1]==0):
        return True
    if(initialpos[-1] in initialpos[0:len(initialpos)-1]):
        return True
    return False

def onkeypress(event):
    global key
    if event.name == 'w':
        key='w'
    if event.name == 'a':
        key='a'
    if event.name == 's':
        key='s'
    if event.name == 'd':
        key='d'

def food():
    global f1,f2
    f1=random.randint(1,rows-2) 
    f2=random.randint(1,cols-2)
    
    
def main():
    global rows,cols,key
    initialize_matrix(rows,cols)
    clear()
    print_matrix()
    c=1
    valid={'d','a','s','w'}
    keyboard.on_press(onkeypress)
    food()
    while(c):
        while(key in valid):
            if(check()):
                print("You lose")
                c=0
                break
            move()
            clear()
            print_matrix()
            movement.append(key)
            movement.pop(0)
                
    
main()
