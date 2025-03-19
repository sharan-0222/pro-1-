def cu(num) :
   return  num**3

def check(n) :
   if n%3==0 :
      return cu(n)
   else :
      print("please enter a perfect cube ")


n=int(input("please enter a cube- "))
print("the answer is",check(n))