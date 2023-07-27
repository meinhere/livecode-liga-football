# LIVE CODE - WARGALAB 2023
listTeam = [['Team AA', 'Bundesliga', 50, 103], ['Team FF', 'Serie A', 52, 97], ['Team M', 'La Liga', 49, 97], ['Team C', 'Premier', 32, 94], ['Team LL', 'Serie A', 23, 94], ['Team B', 'Premier', 21, 91], ['Team CC', 'Bundesliga', 26, 87]]
listLiga = ['Bundesliga', 'Serie A', 'La Liga', 'Premier']

def sortTeam(listData):
  swap = True

  while swap:
    swap = False
    for i in range(len(listData)-1):
      if listData[i+1][3] == listData[i][3]:
        if listData[i+1][2] < listData[i][2]:
          temp = listData[i+1]
          listData[i+1] = listData[i]
          listData[i] = temp
          swap = True
      else:
        if listData[i+1][3] < listData[i][3]:
          temp = listData[i+1]
          listData[i+1] = listData[i]
          listData[i] = temp
          swap = True
  print("!! Data Telah Diurutkan !!")
  return listData


def tampilkanTeam(data) :
  print()
  #Menampilkan Kolom Header Table
  headers = ["Nama Team", "Nama Liga", "GD", "Points"]
  col_widths = [max(len(str(row[i])) for row in data) for i in range(len(headers))]
  header_row = "|".join(f"{headers[i]:{col_widths[i]}}" for i in range(len(headers)))
  print(header_row)
  print("-" * len(header_row))

  #End Menampilkan Kolom Header Table
  for row in data:
    row_str = "|".join(f"{str(row[i]):{col_widths[i]}} " for i in range(len(row)))
    print(row_str)

def searchTeam(ligaName):
  filterTeam = []
  for team in listTeam:
    if team[1] == ligaName:
      filterTeam.append(team)
  return filterTeam

def menuDua(listTeam) :
  print()
  print()

  space = 46
  index = 0
  menuList = ["", "MENU TAMPILKAN DATA TEAM", "", "Tampilkan Semua Data Team", "Kembali ke Menu Program"]
  for i in range(len(menuList) + len(listLiga)):
    if i == 0 or i == 2:
      print("+" + "-" * (space) + "+")
    elif i == 1:
      print("|" + " " * int((space - len(menuList[i])) / 2) + menuList[i] + " " * int((space - len(menuList[i])) / 2) + "|")
    elif i < 5:
      print("| " + str(i-2) + ". " + menuList[i] + " " * int(space - len(menuList[i]) - 4) + "|")
    else:
      printTeam = "Tampilkan data Team dari Liga " + listLiga[i-5]
      print("| " + str(i-2) + ". " + printTeam + " " * int(space - len(printTeam) - 4) + "|")
    index = i

  inp = int(input("=> Pilih Menu : "))
  start = True

  while start:
    if (inp == 1):
      tampilkanTeam(listTeam)
      menuDua(listTeam)
      return
    elif (inp == 2):
      start = False
      return
    elif (inp < 1 or inp > index-2):
      print("!! Mohon Pilih Nomer Menu yang Ada !!")
      menuDua(listTeam)
      return
    else:
      team = searchTeam(listLiga[inp-3])
      tampilkanTeam(team)
      menuDua(listTeam)
      return


def menuTiga(listTeam):
  print("--> Tambah Liga")
  namaLiga = input("Nama Liga : ")
  jumlahTeam = int(input("Jumlah Team yang akan ditambah : "))

  if namaLiga not in listLiga:
    listLiga.append(namaLiga)

  for i in range(jumlahTeam):
    print()
    print()

    namaTeam = input("Nama Team : ")
    jumlahGD = int(input("Jumlah GD : "))
    jumlahPoint = int(input("Jumlah Point : "))

    listTeam.append([namaTeam, namaLiga, jumlahGD, jumlahPoint])

  print("!! Data Liga & Team Berhasil ditambahkan !!")


def startProgram() :
  print()
  print()

  space = 46
  menuList = ["", "MENU PROGRAM", "", "Rangking Data Team berdasarkan aturan", "Tampilkan Data Team", "Tambah Liga Team", "Keluar Program"]
  for i in range(len(menuList)):
    if i == 0 or i == 2:
      print("+" + "-" * (space) + "+")
    elif i == 1:
      print("|" + " " * int((space - len(menuList[i])) / 2) + menuList[i] + " " * int((space - len(menuList[i])) / 2) + "|")
    else:
      print("| " + str(i-2) + ". " + menuList[i] + " " * int(space - len(menuList[i]) - 4) + "|")

  inp = int(input("=> Pilih Menu : "))
  start = True

  while start:
    if (inp == 1):
      sortTeam(listTeam)
      startProgram()
      return
    elif (inp == 2):
      menuDua(listTeam)
      startProgram()
      return
    elif (inp == 3):
      menuTiga(listTeam)
      startProgram()
      return
    elif (inp == 4):
      start = False
      return
    else:
      print("!! Mohon Pilih Nomer Menu yang Ada !!")
      startProgram()
      return

startProgram()