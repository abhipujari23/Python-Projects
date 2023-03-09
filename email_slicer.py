'''
Email Slicer is a tool which will take an email id as an input and will perform slicing operations on it to return the username and the domain of the email id.
'''

email = input("Enter your email address: ")

email_slices = email.split('@')

print("Your user name is: {}\nYour domain is: {}".format(email_slices[0], email_slices[1]))