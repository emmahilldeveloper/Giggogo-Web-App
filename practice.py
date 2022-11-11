# problem
def main():
    raw_numbers: str = input('Please enter a list of comma separated numbers e.g. 1,2,3: ')
    string_list: list[str] = raw_numbers.split(',')
    numbers_list: list[int] = [int(i) for i in string_list]

    even_nums = []

    for num in numbers_list:
        if num % 2 == 0:
            print(num)
            even_nums.append(num)

    return even_nums

if __name__ == '__main__':
    main()

# buggy
def main():
    raw_numbers: str = input('Please enter a list of comma separated numbers e.g. 1,2,3: ')
    string_list: list[str] = raw_numbers.split(',')
    numbers_list: list[int] = [int(i) for i in string_list]
    even_numbers: list[int] = []
    for num in numbers_list:
        if num / 2 == 0:
            print(num)
            even_numbers.append(num)

    print("The even numbers are:", ', '.join(str(number) for number in even_numbers))


if __name__ == '__main__':
    main()

# problem
# Find Maximum

# Write a method that returns the largest integer in the list. 
# You can assume that the list has at least one element.
# ```

# ### Feature Request Suggestions
# * Find the minimum
# * Assume it has no elements
# * Find the minimum with negative numbers
# * Change it use double/long
def main():
    raw_numbers: str = input('Please enter a list of comma separated numbers e.g. 1,2,3: ')
    string_list: list[str] = raw_numbers.split(',')
    numbers_list: list[int] = [int(i) for i in string_list]
    max_num: int = 0
    for num in numbers_list:
        max_num: int = 0
        if num > max_num:
            max_num = num

    print('The max number in the array is:', max_num)


if __name__ == '__main__':
    main()

# Population Tracker

### Problem
# Population Tracker

# Write a function that given a country x and it’s population y, will store the combination and print out all the values stored.
# ```

# ### Feature Request Suggestions
# * Separate the printing and the adding
# * Remove an element from the list
# * Sort the list (hard)
# * Add a third value (hard)
def population_tracker(country: str, population: int):
    # your code here
    pass


def main():
    population_tracker()


if __name__ == '__main__':
    main()

tracker: dict[str, str] = {}


def population_tracker(country: str, population: int):
    temp: dict[str, str] = {}
    temp[country] = population
    tracker = temp


def main():
    population_tracker('USA', 331002651)
    population_tracker('China', 1439323776)
    population_tracker('India', 1380004385)
    print(tracker)


if __name__ == '__main__':
    main()

