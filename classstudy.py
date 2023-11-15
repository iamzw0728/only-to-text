f = open("D:\BaiduNetdiskDownload\stock_\\1645ab47-99b4-4715-8d2e-9bf73bafc162\stock_\stock\\text.txt","r+")
text1 = f.read()
text2 = []
data = ''
print(text1)
for i in text1:
    if i.islower():
        B=i.upper()
        text2.append(B)
    elif i.isupper():
        L=i.lower()
        text2.append(L)
f.seek(0)
f.writelines(text2)
f.seek(0)
print("更改后文本:",f.read())