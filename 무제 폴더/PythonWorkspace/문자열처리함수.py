python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python)) 
print(python.replace("Python","Java"))

index=python.index("n")
print(index)

index  = python.index("n", index + 1)
print(index)

print(python.find("Java"))
#find 함수에서 없는 문자를 찾을 경우 -1을 반환

#print(python.index("Java"))
#index 함수에서는 없는 문자를 찾을 경우 오류가 난다

print(python.count("n"))
#python 변수에서 n이 몇 개 있는지 세는 함수
