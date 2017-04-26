str1 = str(input ("введите строку = ", ))

strL = "abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM"
str1.isupper()
str1.isalnum()
for i in strL:
  while str1.find(i) != -1:
      str1 = str1[0:str1.find(i)]+str1[str1.find(i)+1:]

print (str1)
print ("иначе если строка выводится пустой, то она состоит только из латинских букв")
input()
