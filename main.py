# denary to binary and binary to denary calculator

def dtb():
  # denary to binary
  # 128	64 32 16 8 4 2 1
  run = True

  while run == True:
    number = int(input("What number would you like to convert to binary?\n")) + 1
    alist = []
    if number >= 255:
      print("error")
      exit()
    if number - 128 > 0:
      number = number - 128
      alist.insert(0, 1)
    else:
      alist.insert(0, 0)
    if number - 64 > 0:
      number = number - 64
      alist.insert(1, 1)
    else:
      alist.insert(1, 0)
    if number - 32 > 0:
      number = number - 32
      alist.insert(2, 1)
    else:
      alist.insert(2, 0)
    if number - 16 > 0:
      number = number - 16
      alist.insert(3, 1)
    else:
      alist.insert(3, 0)
    if number - 8 > 0:
      number = number - 8
      alist.insert(4, 1)
    else:
      alist.insert(4, 0)
    if number - 4 > 0:
      number = number - 4
      alist.insert(5, 1)
    else:
      alist.insert(5, 0)
    if number - 2 > 0:
      number = number - 2
      alist.insert(6, 1)
    else:
      alist.insert(6, 0)
    if number - 1 > 0:
      number = number - 1
      alist.insert(7, 1)
    else:
      alist.insert(7, 0)
    print("Your binary is", alist)
    kRun = input("Would you like to convert another number? y/n\n")
    if kRun == "y":
      run = True
    elif kRun == "n":
      run = False
      os = input("Would you like to make another selection? y/n\n")
      if os == "y":
        selection()
      if os == "n":
        quit()
      else:
        print("error")
        exit()
    else:
      print("error")
      exit()

def btd():
  # binary to denary
  # 128	64 32 16 8 4 2 1
  run = True
  while run == True:
    a0 = int(input("What is your first number"))
    a1 = int(input("What is your second number"))
    a2 = int(input("What is your third number"))
    a3 = int(input("What is your forth number"))
    a4 = int(input("What is your fifth number"))
    a5 = int(input("What is your sixth number"))
    a6 = int(input("What is your seventh number"))
    a7 = int(input("What is your eighth number"))
    alist = [a0, a1, a2, a3, a4, a5, a6, a7]
    number = 0

    if alist[0] == 1:
      number = number + 128
    if alist[1] == 1:
      number = number + 64
    if alist[2] == 1:
      number = number + 32
    if alist[3] == 1:
      number = number + 16
    if alist[4] == 1:
      number = number + 8
    if alist[5] == 1:
      number = number + 4
    if alist[6] == 1:
      number = number + 2
    if alist[7] == 1:
      number = number + 1
    print("Your denary number is", number)
    krun = input("Would you like to input another number? y/n\n")
    if krun == "y":
      run = True
    if krun == "n":
      run = False
      os = input("Would you like to make another selection? y/n\n")
      if os == "y":
        selection()
      if os == "n":
        quit()
      else:
        print("error")
        exit()
    else:
      print("error")
      exit()
def selection():
  yn = input("Would you like to use binary to denary or denary to binary? btd/dtb\n")
  if yn == "btd":
    btd()
  if yn == "dtb":
    dtb()
  else:
    print("error")
    exit()

selection()