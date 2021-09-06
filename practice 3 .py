1.
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

#첫번쨰 거짓
#두번쨰 거짓
#세번쨰 참
#네번째 참

#그래서 가장 처음에 나오는 세번째 값을 출력한다  
#정답은 shirt 

2
result =0
a = 0
while a<=1000:
    if  a%3==0:
        result += a
    a = a+1
print(result)

3
#for 문 사용했을때 
a="*"
for i in range(1,6):
    print(a*i)

#while 문을 사용했을때
a = 0
while True:
    a += 1
    if a>5 : break
    print("*" * a) 

4
for i in range (1,101):
    print(i)
    
5
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
result = 0
for i in A:
    result += i
print(result/10)    #print(result/len(A))로 하는게 더 효율적임



4.
for a in range(1,101):
    print(a)

5
numbers = [1, 2, 3, 4, 5]
result = [n *2 for n in numbers if n % 2 == 1 ]
print(result)
