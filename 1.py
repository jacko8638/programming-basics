#gets inputs
Kilo = input("enter kilos")
pounds = input("enter pounds")
choice = input("which would you like to convert into the other?")

#if statement to find if pounds or kilos
if choice == "kilo":
    #converts kilo to pounds
    answer = int(Kilo) / 2.20462218
    print(answer)
elif choice == "pounds":
    #converts pounds to kilos
    answer = int(pounds) * 2.20462218
    print(answer)
