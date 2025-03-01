
lines = []
while True:
    line = input("Nhập dòng (nhập 'stop' để dừng): ")
    if line.lower() == 'stop':
        break
    lines.append(line)


for line in lines:
    print(line.upper())
