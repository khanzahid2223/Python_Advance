"""
Open data.txt and read the entire content.
Write your name, age, and city into a file, each on a new line.
Read a file line by line and print each line separately.
Count the number of characters in a text file.
Count the number of words in a text file.
Count the number of lines in a text file.
Append "Learning File Handling" to an existing file without deleting its old content.
"""
#Create a file named data.txt and write "Hello Python" into it.
with open("data.txt","w") as f:
    f.write("Hello Python\n")
    