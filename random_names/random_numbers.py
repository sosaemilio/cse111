import random
from re import I

def main():
    numbers = [16.2, 75.1, 52.3]
    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers, 3)
    print(numbers)

    words_list= ["Florida", "Texas", "Icecream"]
    append_random_words(words_list, 2)
    print(words_list)



def append_random_numbers(numbers_list, quantity = 1):
    for i in range(quantity):
        new_number =  random.uniform(1, 100)
        numbers_list.append(round(new_number, 1))
    
def append_random_words(words_list, quantity = 1):
    random_words = ["Apple", "Orange", "Pear" , "Cherry", "Watermelon"]
    for i in range(quantity):
        new_word = random.choice(random_words)
        words_list.append(new_word)


if __name__ == "__main__":
    main()