4
def is_odd(number):         
     if number%2 == 1:       #number의값이 2로 나누었때 나머지가 1인가 
          return True		#그러면 True(odd홀수) 인것이다
     elif number%2 == 0:    # 어렵게 적었지만 간단하게 else 라고 적으면 된다 
          return False	#False 는 짝수라는 뜻이다
print(is_odd(3))
print(is_odd(4))
#위에 두 print 값은 True 와 False 가 나오면 된다 .

4
def avg_numbers(*args):   # *는 숫자가 여러개 나와도 된다는 뜻 
     result = 0       #결과는 0부터
     for i in args:	#for문을 통해 i 를 전부다 더해준다
          result = result + i 
     return result/len(args)	#더해서 나오게 된수를 길이(갯수)로 나누어 평균을 구한다
print(avg_numbers(1,3,4,5))	# avg_numbers에 더하고 싶은 값을 넣어준다 .

4
input1 = input("첫번째 숫자를 입력하세요:") # 문제  3 + 6을 했을떄 36이나오는 식 
input2 = input("두번째 숫자를 입력하세요:") 

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)
#숫자또한 문자열로 포함되기에 int 정수형을 꼭 사용해준다  

4
print("you" "need" "python")    #youneedpython
print("you"+"need"+"python")	#youneepython
print("you", "need", "python")	#you need python # -->,  콤마는 띄어쓰기로 간주 
print("".join(["you", "need", "python"]))	#youneedpython

4
f1 = open("test.txt", 'w')
f1.write("Life is too short!")
f1.close() # 열린 파일 객체를 닫는다.

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()    
# 객체를 닫지 않으면 다시 읽을수가 없다 .  close를 사용해야한다 

4
user_input = input("저장할 내용을 입력하세요:")
f = open('test.txt', 'a')   # 내용을 추가하기 위해서 'a'를 사용
f.write(user_input)		#저장된 내용을 적어주면서
f.write("\n")               # 입력된 내용을 줄 단위로 구분하기 위해 줄 바꿈 문자 삽입
f.close()

4
f = open("새파일.txt" , "r")
body = "Life is too short"+"\n"+"you need java"	#body 값
f.close()				#반드시 닫아줘야한다
	
body = "Life is too short"+"\n"+"you need python"	#body 값을 바꿔준다 
f = open("새파일.txt" , "w")			#쓰기모드로 바꿔서 다시 body를 작성한다.
f.write(body)		
f.close()

이렇게 어렵게 안하고 replace 로 단어들만 바꿔주는것도 생각해야한다 ..
body = body.replace('java', 'python')
