'''
varbox is a variable dumping package, helps you to dump your variable in a file
which can be further accessible from anywhere.
'''
# Import the 'pickle' module for object serialization and deserialization, and 'varboxexceptions' module for exceptions
import pickle
from varboxexceptions import exception
import cipher


# Define a custom function to raise exceptions
def re(msg=None):
    if msg == None:
        raise exception.GenericException()
    raise exception.GenericException(msg)


# Define a function to dump variables to a file
def dump(*args, filepath, varnames=[], encryption_algo=None, encryption_key=None):
    '''

    :param args: variables
    :param filepath: variable file path
    :param varnames: variable name array
    :param encryption_algo: (not in use)
    :param encryption_key: (not in use)
    :return: nohting
    '''
    try:
        # Check if 'varnames' is a list
        if isinstance(varnames, list) is not True:
            re("'varnames' should be a list")

        # If 'varnames' is empty, dump all variables to the file
        if len(varnames) == 0:
            temp = {}
            # Generate unique variable names and store them in a dictionary
            for i in range(0, len(args)):
                temp['var' + str(i)] = args[i]
            # Dump the dictionary to the file using pickle
            with open(filepath, 'wb') as f:
                p_dump(temp, f, encryption_algo, encryption_key)

        # If 'varnames' is not empty and count matches with the variables to be dumped,
        # dump the variables to the file using the provided variable names
        elif len(varnames) == len(args):
            # Check for duplicates in 'varnames'
            if len(set(varnames)) != len(varnames):
                re("duplicates are present in 'varnames'")
            temp = {}
            count = 0
            for i in varnames:
                # Check for empty variable name in 'varnames'
                if i.strip() == "":
                    re("variable name in 'varnames' can not be empty string")
                temp[i] = args[count]
                count += 1
            # Dump the dictionary to the file using pickle
            with open(filepath, 'wb') as f:
                p_dump(temp, f, encryption_algo, encryption_key)

        # If 'varnames' count does not match with the variables to be dumped, raise an exception
        elif len(varnames) != len(args):
            re("'varnames' count -> {} not matched the dumping variables count -> {}".format(len(varnames), len(args)))

        # If none of the above conditions are met, raise an exception
        else:
            re()
    except Exception as ex:
        raise ex


# Define a function to load variables from a file
def load(filepath, encryption_algo=None, encryption_key=None, encryption_iv=None):
    '''

    :param filepath: variable file path
    :param encryption_algo: (not in use)
    :param encryption_key: (not in use)
    :param encryption_iv: (not in use)
    :return: loaded variable in a dictionary
    '''
    # Load the dictionary from the file using pickle
    with open(filepath, 'rb') as f:
        return p_load(f, encryption_algo, encryption_key, encryption_iv)


def p_dump(temp, f, encryption_algo, encryption_key):
    '''

    :param temp: variable dictionary
    :param f: variable file path
    :param encryption_algo: (not in use)
    :param encryption_key: (not in use)
    :return: nothing
    '''
    pickle.dump(temp, f)


def p_load(f, encryption_algo, encryption_key, encryption_iv):
    '''

    :param f: variable file path
    :param encryption_algo: (not in use)
    :param encryption_key: (not in use)
    :param encryption_iv: (not in use)
    :return: loaded variable in a dictionary
    '''
    return pickle.load(f)


'''
#Example
import varbox
class Glass:
    def __init__(self):
        self.amount = "500ml"
    def set_amount(self,a):
        self.amount = a
    def get_amount(self):
        return self.amount

g = Glass()
varbox.dump(1, 2, 3, g, filepath="var_file_path", varnames=["a", "b", "c", "g"])
k = varbox.load("var_file_path")
print(k["g"].amount)
'''
