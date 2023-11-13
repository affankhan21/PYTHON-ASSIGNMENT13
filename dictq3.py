data3={105:"RITA",106:"SITA",107:"DEVIKA"}
find=int(input("ENTER KEY TO SEARCH IN DICTIONARY  :"))
if find in data3.keys():
    print(find," is present in dictionary ")
else:
    print(find," is not  present in dictionary ")
