my_list=["hi","dad","3"]
my_list2=[""]
#kol mozoat sabt shode
my_list3=["33","hi dad"]
m=len(my_list)
l=m
n=0
TF=False
def list(scarf):
    global m
    global n
    global l
    global TF
    if m==0 and n==l:
        mr3=len(my_list3)
        print("boro marhale bad")
        #neshon dadan be karbar va analis
        for i in my_list3:
            if i in my_list2[0]:
                print("namayesh dade",i)
                TF=1
            elif my_list2[0] in i:
                print("namayesh dade", i)
                mr3=1


    else:
        if my_list[n] in scarf:
            if n==0:
                my_list2[0]=my_list2[0]+my_list[n]
            else:
                my_list2[0] = my_list2[0] +" "+ my_list[n]
            n+=1
            m-=1
            list(scarf)
        else:
            n += 1
            m -= 1
            list(scarf)
scarf=input("")
list(scarf)
if TF==False:
    print("motasefane natavanestam peyda konam,dobare talash konid")
