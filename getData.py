import requests
import re
import pandas as pd

url = 'https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดนครศรีธรรมราช'
response = requests.get(url)
# print(response.text)
# table = pd.read_html(response.text)
# for i in table:
#     print(f'{i}\n\n')
    
    
pattern = re.compile('<main[\u0000-\uFFFF]*id="ดูเพิ่ม">ดูเพิ่ม</span>')
result = re.findall(pattern, response.text)

pattern = re.compile('<li>.*</li>')
result = re.findall(pattern, '\n'.join(result))

# pattern = re.compile('สำนักสงฆ์[\u0E01-\u0E5B]*')
# samNak = re.findall(pattern, '\n'.join(result))

pattern = re.compile('>วัด[\u0E01-\u0E5B]*')
wat = re.findall(pattern, '\n'.join(result))

nn = 0
# print(len(samNak))
# for i in samNak:
#     print(i)
#     if nn==50:
#         break
#     nn+=1
nn=0
print(len(wat))
for i in wat:
    print(i)
    # if nn==200:
    #     break
    # nn+=1

# m = [] #เช็คจำนวนข้อมูล
# mm ='' #ไว้สร้าง String
# # for strr in result:  
# #     newstr = re.search(r"title=\".*\"",strr).group()

# #     newstr2 = re.search(r"\".*(\s|\")",newstr)

# #     if newstr2 != None: #กัน none error
# #         newstr2 = newstr2.group()
# #         # print(newstr2)
# #         m.append(newstr2)
# #         mm += ' '+str(newstr2)
# #     else:  
# #         print(f'{newstr} 1') 
# #         print(f'{newstr2} 2\n')
    
# #ไว้จำนวนดูข้อมูล
# print(m)        
# print(f'มี {len(m)} ชุด')  # 2155


# # print(mm) #เช็คว่าเก็บเป็น string ได้

# cc = re.sub('\([\u0E01-\u0E5B]*\)', '',mm) #เอาวงเล็บพร้อมคำที่อยู่ข้างในออก
# # unicode พาสาทัย คือ \u0E01-\u0E5B
# wat = re.findall('วัด[\u0E01-\u0E5B]+',cc)  #เอาแค่พาสาทัย วัด.......  [\u0E01-\u0E5B]+ คือ ภาษาที่ทำซ้ำอย่างน้อย 1 ครั้ง Ex = {ก,ข,ค, ... กก กข กขค คขก ...} ไม่มี string ว่าง
# for i in wat:
#     print(i)
# print(len(wat)) #2157 ทำไมมันเพิ่มขึ้นวะ
# # pd.DataFrame(wat).to_csv('รายชื่อวัดในจังหวัดนครราชสีมา.csv',index=False,header=False,encoding="utf-8-sig")
# #ไว้ดูข้อมูล
# # for i in m:
# #     print(f'{i}') 