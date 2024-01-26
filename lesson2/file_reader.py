# напиши код для выполнения заданий здесь

# with open('./lesson2/my_file.txt') as file:
    # 1
    # data = file.read()
    # total = 0
    # for i in data:
    #     if i == '1':
    #         total += 1
    # print(total)

    # 2
    # data = file.readlines()
    # data = list(map(str.split,data))
    # print(data[14][8])

    # 3
    # total = 0
    # for row in file:
    #     for i in row.split(' '):
    #         total += int(i)
    #         # print(total, row)
    # print(total)


    # ---------------------------------
    #задание 1
count = 0
with open('my_file.txt','r') as file:
   for string in file:            
       string_list = string.split(' ')
       for symbol in string_list:
           if int(symbol) == 1:
               count = count+1
print(count)


#задача 2
with open('my_file.txt','r') as file:
   lines = file.readlines()
   second_line = lines[13].split(' ')
   item = int(second_line[7])
   print(item)


#задача 3
count = 0
with open('my_file.txt','r') as file:
 lines = file.readlines()
 for i in range(len(lines)):
     string_list = lines[i].split(' ')
     for j in range(len(string_list)):
          count = count + int(string_list[j])
print(count)


#задача 4
count = 0
with open('my_file.txt','r') as file:
   lines = file.readlines()
   for i in range(len(lines)):
       string_list = lines[i].split(' ')
       for j in range(len(string_list)):
           if i == 2 or i == 5 or i == 8 or i ==11 :
               count = count + int(string_list[j])
print(count)


#задача 5
count = 0
max_elem = 0
with open('my_file.txt','r') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        string_list = lines[i].split(' ')
        for j in range(len(string_list)):
            if int(string_list[j]) > max_elem:
                max_elem = int(string_list[j])
        count = count + max_elem
        max_elem = 0
print(count)
