*****targil 2:
    
exercize = input("please enter exercize: ")
ls_ex = exercize.split()
a = int(ls_ex[0].replace(' ',''))
b = int(ls_ex[2].replace(' ',''))
c = int(ls_ex[4].replace(' ',''))

if a + b == c:
    print("TRUE")
else:
    print("FALSE")

    


*****targil 3:

ls = [1,2,3,4,5,6]
for i in range(0,len(ls)//2):
    print(ls[i])





*****targil 4:


ls1 = ['hello', 'python', 'pen', 'world of coding']
for element in ls1:
    print(element.upper())
    
    
*****targil 5:

ls1 = ['hello', 'python', 'pen', 'world of coding']
for element in ls1:
    if len(element) < 4:
        break
    print(element.upper())
    

*****targil 6:

fullname = 'Julie Sigal'

print(fullname[-5:len(fullname)])

print(fullname[0:(len(fullname)//3)])

print(fullname.count('a'))

if fullname.count('b') > 0:
    print("true")
else:
    print("false")
    
ls_fullname = fullname.split()

ls_fullname = [ls_fullname[1] , ls_fullname[0]]

print(ls_fullname)

ls_fullname[0] = ls_fullname[0].upper()

ls_fullname[1] = ls_fullname[1].replace('l',"")

fullname_2 = ' '.join(ls_fullname)

print(fullname_2)


*****targil 7:
    
hello = 'hello world'

for i in range(len(hello)):
    if hello[i] == 'o':
        print(i)

print(hello[0:5])
print(hello[5:len(hello)])

*****targil 8:
    
hello = 'hello world!'

print(hello.replace('o',''))
   

***** targil 9:


new_list = [8,1000,-3,2,5]

print(sum(new_list))

print((max(new_list)))

print(min(new_list))

print(sum(new_list) / len(new_list))

print(new_list.remove(-3))

new_list.sort()
print(new_list)

print(new_list*5)

new2 = new_list[1:len(new_list)]

last_ls = []
for i in new_list:
    if i < avg:
        last_ls.append(i)
        print(last_ls)
            
**** targil 10:
    
ls = [1,5,7,8,100]
max = ls[0]
for element in ls:
    if element > max:
        max = element
print(max)

#### second solution:

ls.sort()
print(ls[-1])

*****targil 11:
    
main_ls = [[4, 8, 200], [4, 3000, -1], [5, 87, 12]]
min_val = main_ls[0][0]

for i in range(len(main_ls)):
    for j in main_ls[i]:
        if j < min_val:
            min_val = j

print(min_val)
