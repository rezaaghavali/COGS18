# This program uses a dictionary to keep friends'
# names and birthdays.
# The dictionary is empty in the beginning of the program

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# main function


def main():
    """This is the main function for calling the
       other functions
    """
    # Create an empty dictionary.
    birthdays = {}

    # Initialize a variable for the user's choice.
    choice = 0

    while choice != QUIT:
        # Get the user's menu choice.
        choice = get_menu_choice()

        # Process the choice.
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)


def get_menu_choice():
    """The get_menu_choice function displays the menu
    and gets a validated choice from the user.

    Parameters
    ----------
    input : int
        User's choice in the menu

    Returns
    -------
    output : string
        Shows the validated choice."""

    print()
    print('Friends and Their Birthdays')
    print('---------------------------')
    print('1. Look up a birthday')
    print('2. Add a new birthday')
    print('3. Change a birthday')
    print('4. Delete a birthday')
    print('5. Quit the program')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice



def look_up(birthdays, testmode = False):
    """The look_up function looks up a name in the
       birthdays dictionary.

    Parameters
    ----------
    input : string
        Get the name to look up

    Returns
    -------
    output : string
        Name and the corresponding birthday"""
        
    if testmode:
        name = 'Dave'
        output = birthdays.get(name)
        print(birthdays.get(name, 'Not found.'))    # Look it up in the dictionary.
        return output
    else: 
        name = input('Enter a name: ')              # Get a name to look up.
        output = birthdays.get(name)
        print(birthdays.get(name, 'Not found.'))    # Look it up in the dictionary.
        return output

def add(birthdays,testmode = False):
    """The add function adds a new entry into the 
       birthdays dictionary.
       
    Parameters
    ----------
    input : string
        Get the name and the corresponding birthday

    Returns
    -------
    output : string
        stores the name and the corresponding birthday and 
        if the name exists it would show it as an output"""
       
    if testmode:
        name = 'Dave'
    
    else:
        # Get a name and birthday.
        name = input('Enter a name: ')                      
        bday = input('Enter a birthday: ')

    # If the name does not exist, add it.   
    if name not in birthdays:                           
        birthdays[name] = bday
        output = bday
    else:
        output = 'That entry already exists.'
    return output


def change(birthdays, testmode = False):
    """ The change function changes an existing 
        entry in the birthdays dictionary.
       
    Parameters
    ----------
    input : string
        Get the name

    Returns
    -------
    output : string
        If the name exists, it would just update the corresponding birthday. 
        If the name does not exist, it would simply show 'That name is not found.' as an output"""


    if testmode:
        name = 'Dave'
        if name in birthdays:
            bday = '08/26/1996'
            birthdays[name] = bday                          
            output = bday            
    else:
        # Get a name to look up.
        name = input('Enter a name: ')                      

        if name in birthdays:
            # Get a new birthday.
            bday = input('Enter the new birthday: ')        

            # Update the entry.
            birthdays[name] = bday
            output = bday                         
        else:
            output = print('That name is not found.')
    return output
        


def delete(birthdays):
    """The delete function deletes an entry from the
       birthdays dictionary.

    Parameters
    ----------
    input : string
        Get the name

    Returns
    -------
    output : string
        If the name exists, it would just delete the corresponding birthday. 
        If the name does not exist, it would simply show 'That name is not found.' as an output"""
       
    # Get a name to look up.
    name = input('Enter a name: ')                      

    # If the name is found, delete the entry.   
    if name in birthdays:                               
        del birthdays[name]
    else:
        print('That name is not found.')


