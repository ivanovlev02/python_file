list_file = ['sorted/1.txt', 'sorted/2.txt','sorted/3.txt']
list_new_file = ['sorted/n_1.txt', 'sorted/n_2.txt','sorted/n_3.txt']
new_data_file = []
step = 0


while step < len(list_file):
     with open(list_file[step], encoding='utf-8') as f:
          data = f.readlines()
          qvon_str = len(data)

     with open(list_file[step], encoding='utf-8') as f:
          data_text = f.read()

     with open(list_new_file[step], 'w', encoding='utf-8') as f:
         f.write(f'{list_file[step]}\n')
         f.write(f'{qvon_str}\n')
         f.write(f'{data_text}\n')
     step +=1

for some_file in list_new_file:
     with open(some_file, encoding='utf-8') as f:
         new_data = f.read()
         new_data_file.append(new_data)

new_data_file.sort(key=len)

with open('sorted/out.txt', 'w', encoding='utf-8') as f:
    for some_pat in new_data_file:
          f.write(f'{some_pat}')