Kilo = input("enter kilos")
pounds = input("enter pounds")
choice = input("which would you like to convert into the other?")
if choice == "kilo":
    answer = int(Kilo) / 2.20462218
    print(answer)
elif choice == "pounds":
    answer = int(pounds) * 2.20462218
    print(answer)
