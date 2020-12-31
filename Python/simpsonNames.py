""" Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'. """

def namelist(names):
    if names is []:
        return ''
    else: 
        x = len(names)
        str = ""
        while x > 0: 
            if x == 1:
                str = str + names[-1]['name']
            elif x == 2: 
                str = str + names[-2]['name'] + " & "
            else: 
                str = str + names[-x]['name'] + ", "
            x = x - 1
        return str