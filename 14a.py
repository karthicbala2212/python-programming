x,y=map(int,input().split())
if(x<y):
  for i in range(x+1,y,1):
     if i%2!=0:
        print(i,end=' ')
