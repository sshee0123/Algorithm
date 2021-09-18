#구현-08 문자열 재정렬
s = input()
result = []
value = 0

for i in s:
    if i.isalpha():
        result.append(i)
    else:
        value += int(i)

result.sort()

if value!=0:
    result.append(str(value))

print(''.join(result))