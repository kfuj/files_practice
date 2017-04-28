""" This file is part of the File I/O exercise.

It should be used with the two input files, fruits_1.txt and fruits_2.txt."""

def open_and_read_file(filename):
    """Opens file as a file object and returns list of contents."""

    our_New_File = open(filename)
    our_New_File = our_New_File.read()
    our_New_File = our_New_File.split()
    return our_New_File
    

   


def compare(lst1, lst2):
    """Takes in two lists and returns a list of items in common. """
    bonnie = []
    for item in lst1:
        if item in lst2:
            bonnie.append(item)
    return bonnie


# Call your functions all the way at the bottom, after they've been defined.
Kathy = open_and_read_file("fruits_2.txt")


Monica = open_and_read_file("fruits_1.txt")


Bonnie = compare(Kathy, Monica)
print Bonnie
