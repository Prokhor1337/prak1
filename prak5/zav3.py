age= int(input("Введіть свій вік:"))
year_exp= int(input("Введіть кількість років досвіду:"))
ed= str(input("Введіть чи є у вас освіта(true/false):")).strip().lower() == "true"

if (age<=50 and age>=25) and (year_exp>=3 or ed):
    print("вас прийнято")
else:
    print("ти в пролете")
