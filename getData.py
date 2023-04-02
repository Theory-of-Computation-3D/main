import requests
import re
import pandas as pd


class Wat():
    def __init__(self, province=0):
        self.data = None
        self.province = province
        self.provinceName = ''
        self.select_province(province)

    def select_province(self, province = 0):
        if 1 <= province <= 5:
            self.province = province
        # นครศรีธรรมราช
        if (self.province == 1):
            self.provinceName = 'รายชื่อวัดในจังหวัดนครศรีธรรมราช'
            return self.__nonTablePattern('https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดนครศรีธรรมราช')
        # นครสวรรค์
        elif (self.province == 2):
            self.provinceName = 'รายชื่อวัดในจังหวัดนครสวรรค์'
            return self.__nonTablePattern('https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดนครสวรรค์')
        # นนทบุรี
        elif (self.province == 3):
            self.provinceName = 'รายชื่อวัดในจังหวัดนนทบุร'
            return self.__tablePattern('https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดนนทบุรี')
        # นราธิวาส
        elif (self.province == 4):
            self.provinceName = 'รายชื่อวัดในจังหวัดนราธิวาส'
            return self.__nonTablePattern('https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดนราธิวาส')
        # อุทัยธานี
        elif (self.province == 5):
            self.provinceName = 'รายชื่อวัดในจังหวัดอุทัยธานี'
            return self.__nonTablePattern('https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดอุทัยธานี')
        # เชี่ยไรไม่รู้ที่ไม่ได้อยู่ข้างบน
        else:
            print('ไอ้สัส!! กูไม่ได้ทำจังหวัดนี้')

    #private # นครศรีธรรมราช , นครสวรรค์ , นราธิวาส , อุทัยธานี
    def __nonTablePattern(self, url):
        response = requests.get(url)

        # กำหนดช่วงที่จะหาให้อยู่ตั้งแต่ <main ..................... id="ดูเพิ่ม">ดูเพิ่ม</span>
        pattern = re.compile('<main[\u0000-\uFFFF]*id="ดูเพิ่ม">ดูเพิ่ม</span>')
        result = re.findall(pattern, response.text)

        # กำหนดให้หาแค่ในเฉพาะ <li>.............</li>
        pattern = re.compile('<li>.*</li>')
        result = re.findall(pattern, '\n'.join(result))

        # กำหนดให้หาแค่ชื่อวัด
        pattern = re.compile('>วัด[\u0E01-\u0E5B]*')
        self.wat = re.sub(">", "", str(result))
        self.wat = re.findall(pattern, ''.join(result))

        # ลบ > ออกไป
        # เอา array data ไปใช้ต่อได้เลย
        self.data = self.__groupData()

        # print เช็ค data
        # print(self.data)

        # เช็คจำนวน
        print('วัด = ' + str(len(self.data)))

    #private # นครสวรรค์
    def __tablePattern(self, url):
        response = requests.get(url)

        # กำหนดช่วงที่จะหาให้อยู่ตั้งแต่ <div id= ..................... title="ประเทศไทย">ประเทศไทย</a>แบ่งตามจังหวัด</div>
        pattern = re.compile('<div id=[\u0000-\uFFFF]*title="ประเทศไทย">ประเทศไทย</a>แบ่งตามจังหวัด</div>')
        result = re.findall(pattern, response.text)

        # กำหนดให้หาแค่ในเฉพาะ <td>.............</td>
        pattern = re.compile('<td>.*</td>')
        result = re.findall(pattern, '\n'.join(result))

        # กำหนดให้หาแค่ชื่อวัด
        pattern = re.compile('>วัด[\u0E01-\u0E5B]*')
        self.wat = re.findall(pattern, '\n'.join(result))

        # ลบ > ออกไป
        # เอา array data ไปใช้ต่อได้เลย
        self.data = self.__groupData()

        # print เช็ค data
        # print(self.data)

        # เช็คจำนวน
        print('วัด = ' + str(len(self.data)))
    #private # นครสวรรค์
    def __groupData(self):
        templeList = []
        for i in self.wat:
            templeList.append(re.sub(">", "", i))
        return templeList

    def saveCSV(self):
        df = pd.DataFrame(self.data)
        df.drop_duplicates(inplace=True)
        #เช็คหลังลบตัวซ้ำ
        #print(len(df))
        df.to_csv(f'{self.provinceName}.csv', index=False, header=False, encoding="utf-8-sig")

if __name__ == '__main__':
    print("===== Select one of them =====")
    print("1. จังหวัดนครศรีธรรมราช")
    print("2. จังหวัดนครสวรรค์")
    print("3. จังหวัดนนทบุรี")
    print("4. จังหวัดนราธิวาส")
    print("5. จังหวัดอุทัยธานี")
    province = int(input("Select(number) : "))
    wat = Wat(province)
    wat.saveCSV()

# วิธีใช้
# 1. จังหวัดนครศรีธรรมราช"
# 2. จังหวัดนครสวรรค์
# 3. จังหวัดนนทบุรี"
# 4. จังหวัดนราธิวาส"
# 5. จังหวัดอุทัยธานี"
# wat = Wat(เลข 1-5 เลือกจังหวัด)
# wat.select_province(เลข 1-5 เลือกจังหวัด)
# wat.saveCSV()  save เป็น CSV
