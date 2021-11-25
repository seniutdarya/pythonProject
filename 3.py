# Найдите сумму номеров минимального и максимального элементов.
#a = [5, 6, 6, 8, 4, 9, 2, 8]


#b = a.index(max(a))
#c = a.index(min(a))

#m = b+c
#print(m)

def dog_age2human_age(dog_age):
    """dog_age2human_age(dog_age)"""
    if dog_age == 1:
        human_age = 14
    elif dog_age == 2:
        human_age = 22
        print()
    else:
        human_age =  22 + (dog_age-2)*5
    return human_age

age = int(input("How old is your dog? "))
print(f"This corresponds to {dog_age2human_age(age)} human years!")
