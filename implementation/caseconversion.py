for _ in range(int(input())):

     s=input();t=s[0].lower()

     for i in s[1:]:

          if(i.isupper()):t+="_"+i.lower()

          else:t+=i.lower()  

     print(t)