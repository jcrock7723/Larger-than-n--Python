# Unit 7 page 335, #6 modified for user input
# Take a list and a number value
# Display only the numbers greater than the value given

def main():
    # Create an empty list
    user_list = []
    index = 0

    print('This program allows you to create a list and display')
    print('all numbers that are larger than a specified value.')
    print('(hit ENTER to continue)')
          
    input()
          
    # request upper range and list size from user
    qty_number=int(input('How many numbers do you want in your list?: '))
    upper_limit=int(input('What is the number that you ' \
                          'would like to be the limit?: '))
    # Explain how to input numbers
    print()
    print('Now type your list of numbers one at a time and hit ' \
              'ENTER after each.')
    
    # get the numbers for the list from the user
    while index < qty_number:
        
        numbers=int(input('Type a number, hit ENTER: '))

        # add the numbers to the list
        user_list.append(numbers)

        # accumulator, step through to get the reguired numbers from user
        index+=1
        

    # Display the number
    print()
    print('Limit number: ', upper_limit, '\n')

    # Display the list of numbers
    print('List of numbers:\n', user_list, sep='')

    # Display the list of numbers larger than the number
    print()
    print('List of numbers larger than ', \
          upper_limit, ':', sep='')

    # Call the display_larger_than_n_list function
    # Passing a number and list as arguments
    display_larger_than_n_list(upper_limit, user_list)

def display_larger_than_n_list(n, n_list):
    # Declare an empty list
    larger_than_n_list = []

    # loop throught the values in the list
    for value in n_list:

        # Define limiter for loop value
        if value > n:
            
            # Append the numbers greater than n
            larger_than_n_list.append(value)

    # Display the list
    print(larger_than_n_list)

# Call the main function
main()
