str1 = str(input ("введите слово = ", ))
sl = list(str1) #разобрали слово по буквам
sl.sort(); #отсортировали буквы по возрастанию

for i in range(len(sl)):
  if sl[i]== sl[i+1]:
      print (sl[i])
      break

