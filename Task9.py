# Task 9 Cat problem
# You've collected too many cats. Write a program to count how
# many cats you have by reading in their names. All your cats only
# have first names, with no spaces.

def main():
    #Write your code here
    cats_name = input('Cats: ')

    var = cats_name.split() 
    count = len(var)
    print(f'You have {count} cats.')



    # End of your code here





if __name__ == '__main__':
    main()