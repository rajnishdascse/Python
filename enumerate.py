ls = ['Pen', 'Paper','Ink','Eraser']

# i = 1
# for item in ls:
#     if i%2 != 0:
#         print(f'Buy this {item}')
#     i+=1

#the same above program can be easily done through enumerate functon

for i,items in enumerate(ls):
    if i%2 !=0:
        print(f'Buy this : {items}')
    
    
