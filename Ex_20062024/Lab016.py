#list - shopping list
#milk, bread, butter, poha
#1. Add item
#2. Remove item
#3. Update item
#4. view item
#5. Exit

shopping_list = ['milk', 'bread', 'butter', 'poha']
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])
shopping_list.append("curd")
print(shopping_list)
shopping_list.insert(1,'jam')
print(shopping_list)
shopping_list.extend(['chips','salt'])
print(shopping_list)
shopping_list.remove('bread')
print(shopping_list)
shopping_list.pop()
print(shopping_list)
print(shopping_list.index('butter'))
print(shopping_list)
shopping_list.reverse()
print(shopping_list)
shopping_list.sort()
print(shopping_list)
shopping_list[0] ='Indu'
print(shopping_list)

#my_list = [1,2,3,4,True,3.14,"pramod"]
#print(type(my_list))