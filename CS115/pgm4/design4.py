'''
Author: Kelly Sovacool
Email: kellysovacool@uky.edu
Sec: 006
Date: 21 Apr. 2015
Purpose: Simulate a Domain Name Server, which keeps track of the domain names assigned to IP addresses.
    It allows the user to add new domain names and IPs, change IPs of existing domain names,
    remove domain names and IPs, find the pair of a domain name or IP,
    and display the domain names and IPs in parallel array style
Preconditions: a file called 'DNScommands.txt' with one command per line; 
    the first character of each line must represent a known command symbol 
    followed by either a domain name, IP, or sort order (all separated by whitespace), 
    depending on the command
Postconditions: executes each known command, reports on success or failure of each,
    adds up total commands processed, adds up total invalid commands detected
'''
# main function
     # Display 'Domain Name System Simulator'
     # Initialize the domain name and IP lists
     # Initialize counter for total commands processed
     # Initialize counter for invalid commands
     # Initialize valid file flag to False
     # While the file name is not valid:
          # try:
               # Get the file name of the commands from the user and open it
               # Assign valid file flag to True (only executes if file opens without error)
          # except if the file cannot be found:
               # Output error message
          # except if the file is not a text file:
               # Output error message
     
     # For each line in the file:
          # output 'Command ' and the line
          # split the line by whitespaces
          # if the first character is a '+' (adding domain name & IP pair):
               # try:
                    # get the domain and IP strings
                    # call the put_in function
                    # output whether it was successful or not
               # except if domain/ip pair not specified (causes index error):
                    # output error message, 'domain/ip pair not specified'
               # add 1 to the total commands counter
               
          # else if the first character is a '-' (removing a domain name & IP pair):
               # try:
                    # get the domain name string
                    # call the take_out function
                    # if take_out returns True:
                         # Output that the removal was successful
                    # else:
                         # Output that the removal was not successful
               # except if the domain name string not specified (causes index error):
                    # output error message, 'domain name not specified'
               # add 1 to the total commands counter
               
          # else if the first character is a '?' (searching the tables):
               # try:
                    # get the target string
                    # call the table_lookup function
                    # if return of table_lookup function is -1:
                         # output error message, 'Not found'
                    # else: (table_lookup was successful)
                         # output domain name and IP pair
               # except if the target string not specified (causes index error)
                    # output error message: 'No target string specified'
               # add 1 to the total commands counter
               
          # else if the first character is an 'L' (displaying tables in parallel array style):
               # call the display_lists function
               # add 1 to the total commands counter
               
          # else if the first character is an 'S' (sorting the tables):
               # try:
                    # get the sort order string
                    # call the selection_sort function
                    # output whether the data were sorted by domain or IP
               # except if sort order string not specified (causes index error):
                    # output error message, 'No sort order specifed')
               # add 1 to the total commands counter
          # else:
               # output an error message, 'Invalid commmand'
               # add 1 to the invalid commands counter
     # Output the total number of commands processed
     # Output the number of invalid commands
     # Close the file

# function: table_lookup
'''
Purpose: When given an IP or Domain Name, searches for its
     pair (opposite type) in the appropriate table and outputs it. 
Preconditions: IP or domain name target as a string, the IP and domain tables
Postconditions: Returns the index of the target string's pair; if not found, returns -1
'''
     # Design:
     # split the target string by periods
     # split the target string by colons
     # if the target string characters up to the first period are all digits (IPv4)
     # or splitting the target string by colons yields more than three elements (IPv6)
     # the target string is an IP number:
          # try:
               # assign the result to the index of the IP number
          # except if the ip or domain is not in the list:
               # assign result to -1
     # else (target string is a domain):
          # try:
               # assign the result to the index of the domain name
          # except if the ip or domain is not in the list:
               # assign result to -1
     # return result

# function: take_out
'''
Purpose: To remove a domain name and IP pair from the tables
Preconditions: The domain name as a string, the IP and domain lists
Postconditions: Removes the pair from the tables; Returns boolean value
     to indicate success or failure
'''
     # Design:
     # try:
          # find the index of the domain name
          # remove the domain name from the domain name list
          # remove the IP address at the same index from the IP list
          # assign result to True
     # except if the domain is not in the list:
          # assign result to False
     # return the result

# function: put_in
'''
Purpose: Insert a new Domain Name and IP pair into the tables, 
    or change the IP of an existing domain name
Preconditions: domain name and IP pair as strings, the IP and domain lists
Postconditions: Returns none; inserts new domain name & IP pair 
    or changes IP of existing domain name
'''
     # Design:
     # if the domain name is in the domain name list:
          # find the index of the domain name
          # change the IP at the same index in the IP table to the IP given
     # else:
          # append the domain name to the domain name table
          # append the IP to the IP table

# function: selection_sort
'''
Purpose: Sort the tables to ascending order according to either IP or domain name
Preconditions: the domain name and IP lists, the sort order as a string (must be 'Domain' or 'IP')
Postconditions: returns none; sorts the lists in ascending order
'''
     # Design:
     # make a copy of the unsorted domain_list
     # make a copy of the unsorted ip list
     # if user sorts by domain:
          # sort the domain_list in ascending order
          # for indices in the domain name list:
               # find the position of the element in the unsorted list
               # move the corresponding ip to its new index in the sorted list
     # else if user sorts by IP:
          # sort the ip_list in ascending order
          # for indices in the IP list:
               # find the position of the element in the unsorted list
               # assign the corresponding domain to its new index in the sorted lsit

# function: display_lists
'''
Purpose: Output the content of the two lists
Preconditions: the domain name and IP lists
Postconditions: returns none; outputs the lists to standard output in parallel array style
'''
     # Design:
     # Output the 'Domain Name' and 'IP' headers
     # for each element in the domain name list:
          # print the domain and its corresponding ip on the same line

# call the main function