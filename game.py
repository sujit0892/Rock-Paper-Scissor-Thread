import random
player=input("rock(r),paper(p),scissor(s),thread(t)? ")
comp=random.randint(1,4)
if comp==1:
  comp="0"
elif comp==2:
  comp="__"
elif comp==3:
   comp="8<"
else:
   comp="--"
if player=="r":
   player="0"
elif player=="p":
   player="__"
elif player=="s":
   player="8<"
else:
   player="--"

print(player,"vs",comp)

if player==comp:
 print("draw !")
elif player=="0" and comp=="8<":
 print("player win !")
elif player=="__" and comp=="0":
 print("player win !")
elif player=="8<" and (comp=="__" or comp=="--"):
 print("player win !")
elif player=="--" and (comp=="0" or comp=="__"):
 print("player win !")
else :
 print("computer win !")
