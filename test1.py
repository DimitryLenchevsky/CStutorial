import random
while True:
  print ("Игра \"Русская рулетка\"")
  print ("Всего 5 попыток, играете вы и компьютер")
  raund = 0
  ver = 0
  while True:
    ver = ver + 1
    u1 = random.randint (ver,6)
    c1 = random.randint (ver,6)
    s1 = random.randint (ver,6)
    raund = raund + 1
    if raund > 5:
      print ("Игра окончена, ничья")
      break;
    print (str(raund) + " Раунд")
    kk = int(input("Для выстрела нажмите 1:"))
    if kk != 1:
      print ("Ошибка")
      break;
    elif kk == 1:
      if u1 == s1 and c1 != u1:
        print ("У вас патрон, у компьютера нет патрона, вы проиграли, игра окончена")
        break ;
      elif c1 == s1 and u1 != s1:
        print ("У комьютера патрон, у вас нет патрона, вы выиграли, игра окончена")
        break ;
      elif c1 != s1 and u1 != s1:
        print ("Ничья, у вас у обоих нет патрона")
      elif c1 == s1 and u1 == s1:
        print ("Ничья, у вас у обоих по патрону, игра окончена")
        break ;
  q = int(input("Хотите ли вы играть снова? Нажмите 1 если да, 2 если нет:"))
  if q == 1:
    print ("Перезапускаем игру... \n")
  elif q == 2:
    print ("Спасибо за игру!")
    break ;
  else:
    print ("Ошибка, неверный формат")
    break ;
