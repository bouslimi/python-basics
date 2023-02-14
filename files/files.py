"""
    Files
---
Mode	Meaning
'r'     open for reading (default)
'w'     open for writing, truncating the file first
'x'     create a new file and open it for writing
'a'     open for writing, appending to the end of the file if it exists
'b'     binary mode
't'     text mode (default)
'+'     open a disk file for updating (reading and writing)
'U'     universal newline mode (deprecated)
The default mode is 'rt' (open for reading text).
"""

# Writing to file
# test_file = open("files_test_data.csv", "w")
with open("files_test_data.csv", "w") as test_file:
    test_file.write("id;name;email" + "\n")
    test_file.write("1;Amine;amine@email.com" + "\n")
    test_file.write("2;Ala;ala@email.com" + "\n")
# test_file.close()

# Reading from file
# test_file = open("files_test_data.csv", "r")
with open("files_test_data.csv", "r") as test_file:
    # Read all line at once
    # print(test_file.read())
    # Read file line by line
    for line in test_file:
        print(line)
    # Read lines as a list
    # print(test_file.readlines())
# test_file.close()
