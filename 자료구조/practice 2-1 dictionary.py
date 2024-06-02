dic = {"apple":"사과", "peach":"복숭아", "banana" : "바나나"}

print(dic)



dic['grape'] = "포도"
dic.update({"orange":"오렌지" , "mandarin": "귤"})

for key in dic:
    print("%s는 %s입니다" % (key, dic[key]))


print(dic)

print(dic.keys())
print(dic.values())