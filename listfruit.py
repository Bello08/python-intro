listfruit=["orange","apple","banana","pineapple","mango","pawpaw","groundnut"]
listme=["orange","yam","chiz","chiz","pineapple","pineapple","mango","pawpaw","groundnut"]

for i in listme:
    if i=="mango":
          print(i)
          listme.remove(i)
        
print(listme)   

item_list = ['item', 5, 'foo', 3.14, True]
item_list.remove('item')
item_list.remove('foo') 
print(item_list)