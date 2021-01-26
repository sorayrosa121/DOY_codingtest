### students list sorted by grades

n = int(input())
dic = {}
for _ in range(n):
    name, grade = input().split()
    dic[name] = int(grade) # dic = {'hong':95, 'lee':77}

grade_list = list(dic.values()) # grades(values) only; [95, 77]
grade_list.sort() # [77, 95]
print(grade_list)

for i in range(len(grade_list)):
    for key, value in dic.items(): # dict_items([('hong', 95), ('lee', 77)])
        if value == grade_list[i]:
            print(key, end = ' ') # lee hong