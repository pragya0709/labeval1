#!/usr/bin/env python
# coding: utf-8

# In[ ]:


student = {}
# dietplan = {}
sportmap= {}
def addstud(student):
    name=input("Enter the name of the student:")
    classe=input("Enter the class of the student:")
    height=int(input("Enter the height of the student:"))
    weight=int(input("Enter the weight of the student:"))
    sport=input("Enter the preferred sport:")
    speed=weight/height
    student[name]={"classe":classe,"height":height,"weight":weight,"sport":sport,"speed":speed}
    





# def diet():
#     name=input("Enter the name of the student:")
#     agility=int(input("Enter the agility of the student:"))
#     speed=int(input("Enter the speed of the student:"))
#     strength=int(input("Enter the strength of the student:"))
#     dietplan={"name":name, "agilty":agility, "speed":speed,"strength":strength}
    

def mapping(sportmap):
    sportname=input("Enter the name of the sport")
    sagility=int(input("Enter the agility of the sport:"))
    sspeed=int(input("Enter the speed of the sport:"))
    sstrength=int(input("Enter the strength of the sport:"))
    
    sportmap[sportname]={"sagility":sagility, "sspeed":sspeed, "sstrength":sstrength}
    
    
def find(name , student, sportm):
    for i in sportm:
        if student[name][speed]>=sportm[i][sspeed]:
            print(sportm[i])
            break
            
            
            
            

addstud()
addstud()
addstud()
print()
# diet()
# diet()
# diet()
#print(dietplan)
mapping()
mapping()
mapping()

x=input("Enter the name of the student you want the diet plan of")

find(x,dietplan,sportmap)





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




