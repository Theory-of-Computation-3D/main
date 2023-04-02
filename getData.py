import requests
import re
import pandas as pd

def select_province(province):
    # นครศรีธรรมราช
    if (province == 1):
        return nonTablePattern('https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดนครศรีธรรมราช')
    # นครสวรรค์
    elif (province == 2):
        return nonTablePattern('https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดนครสวรรค์')
    # นนทบุรี
    elif (province == 3):
        return tablePattern('https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดนนทบุรี')
    # นราธิวาส
    elif (province == 4):
        return nonTablePattern('https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดนราธิวาส')
    # อุทัยธานี
    elif (province == 5):
        return nonTablePattern('https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดอุทัยธานี')
    # เชี่ยไรไม่รู้ที่ไม่ได้อยู่ข้างบน
    else:
        print('ไอ้สัส!! กูไม่ได้ทำจังหวัดนี้')

# นครศรีธรรมราช , นครสวรรค์ , นราธิวาส , อุทัยธานี
def nonTablePattern(url):
    response = requests.get(url)

    # กำหนดช่วงที่จะหาให้อยู่ตั้งแต่ <main ..................... id="ดูเพิ่ม">ดูเพิ่ม</span>
    pattern = re.compile('<main[\u0000-\uFFFF]*id="ดูเพิ่ม">ดูเพิ่ม</span>')
    result = re.findall(pattern, response.text)

    # กำหนดให้หาแค่ในเฉพาะ <li>.............</li>
    pattern = re.compile('<li>.*</li>')
    result = re.findall(pattern, '\n'.join(result))

    # กำหนดให้หาแค่ชื่อวัด
    pattern = re.compile('>วัด[\u0E01-\u0E5B]*')
    wat = re.sub(">", "", str(result))
    wat = re.findall(pattern, ''.join(result))

    # ลบ > ออกไป
    # เอา array data ไปใช้ต่อได้เลย 
    data = groupData(wat)

    # print เช็ค data
    print(data)

    # เช็คจำนวน
    print('วัด = ' + str(len(data)))

# นครสวรรค์
def tablePattern(url):
    response = requests.get(url)

    # กำหนดช่วงที่จะหาให้อยู่ตั้งแต่ <div id= ..................... title="ประเทศไทย">ประเทศไทย</a>แบ่งตามจังหวัด</div>
    pattern = re.compile('<div id=[\u0000-\uFFFF]*title="ประเทศไทย">ประเทศไทย</a>แบ่งตามจังหวัด</div>')
    result = re.findall(pattern, response.text)

    # กำหนดให้หาแค่ในเฉพาะ <td>.............</td>
    pattern = re.compile('<td>.*</td>')
    result = re.findall(pattern, '\n'.join(result))

    # กำหนดให้หาแค่ชื่อวัด
    pattern = re.compile('>วัด[\u0E01-\u0E5B]*')
    wat = re.findall(pattern, '\n'.join(result))

    # ลบ > ออกไป
    # เอา array data ไปใช้ต่อได้เลย 
    data = groupData(wat)

    # print เช็ค data
    print(data)

    # เช็คจำนวน
    print('วัด = ' + str(len(data)))

def groupData(wat):
    templeList = []
    for i in wat:
        templeList.append(re.sub(">", "", i))
    return templeList

if __name__ == '__main__':
    print("===== Select one of them =====")
    print("1. จังหวัดนครศรีธรรมราช")
    print("2. จังหวัดนครสวรรค์")
    print("3. จังหวัดนนทบุรี")
    print("4. จังหวัดนราธิวาส")
    print("5. จังหวัดอุทัยธานี")
    province = int(input("Select(number) : "))
    select_province(province)
    

# table = pd.read_html(response.text)
# for i in table:
#     print(f'{i}\n\n')

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