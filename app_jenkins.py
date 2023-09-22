"""
A python program to test jenkins CI/CD 
It reverses a list and displays it 

"""


def inverse_list(lista):
    """
    A python program to reverse a list

    """
    lista.reverse()

    return print(f"The reversed List : {lista}")


my_list = [14, 6, 48, 56, 7.2]

inverse_list(lista=my_list)
