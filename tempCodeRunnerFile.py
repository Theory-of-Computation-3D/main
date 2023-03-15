# print(mm) #เช็คว่าเก็บเป็น string ได้

# # unicode พาสาทัย คือ \u0E01-\u0E5B
# wat = re.findall('วัด[\u0E01-\u0E5B]+',mm)  #เอาแค่พาสาทัย วัด.......

# for i in wat:
#     print(i)
# print(len(wat))

# pd.DataFrame(wat).to_csv('รายชื่อวัดในจังหวัดนครราชสีมา.csv',index=False,header=False)