'''
Author: Kelly Sovacool
Email: kellysovacool@uky.edu
Sec: 006
Date: 28 Apr. 2015
Purpose: Simulate a Domain Name Server, which keeps track of the domain names assigned to IP addresses.
    It allows the user to add new domain names and IPs, change IPs of existing domain names,
    remove domain names and IPs, find the pair of a domain name or IP,
    and display the domain names and IPs in parallel array style
Preconditions: a file with one command per line; the first character of each line
    must represent a known command symbol, followed by a domain name, IP, 
    or sort order depending on the command
Postconditions: executes each known command, reports on success or failure of each,
    adds up total commands processed, adds up total invalid commands detected
'''
# main function
def main():
     # Display 'Domain Name System Simulator'
     print('Domain Name System Simulator')
     print()
     # Initialize the domain name and IP lists
     domTable = []
     ipTable = []
     # Initialize counter for total commands processed
     totCmds = 0
     # Initialize counter for invalid commands
     totInvalids = 0
     # Initialize valid file flag to False
     validFile = False
     # While the file name is not valid:
     while not validFile:
          # try:
          try:
               # Get the file name of the commands from the user and open it
               file = open(input('Enter filename of simulator commands: '), 'r')
               # Assign valid file flag to True (only executes if file opens without error)
               validFile = True
          # except if the file cannot be found:
          except FileNotFoundError:
               # Output error message
               print('The file could not be found. Please enter a valid file name.')
          # except if the file is not a text file:
          except UnicodeDecodeError:
               # Output error message
               print('The file could not be opened. This program only handles text files.')
     print()
     
     # For each line in the file:
     for line in file:
          # output 'Command ' and the line
          print('Command', line.strip('\n')) # must remove newline for correct ouput formatting
          # split the line by whitespaces
          line_split = line.split()          
          # if the first character is a '+' (adding domain name & IP pair):
          if line[0] == '+':
               # try:
               try:
                    # get the domain and IP strings
                    dom_str = line_split[1]
                    ip_str = line_split[2]
                    # call the put_in function
                    put_in(dom_str, ip_str, domTable, ipTable)
                    # output whether it was successful or not
                    if dom_str in domTable and ip_str in ipTable:
                         if domTable.index(dom_str) == ipTable.index(ip_str):
                              print('Addition successful')
                         else:
                              print('Addition not successful: domain or ip at incorrect index')
                    else:
                         print('Addition not successful: domain/ip not added')
               # except if domain/ip pair not specified (causes index error):
               except IndexError:
                    # output error message, 'domain/ip pair not specified'
                    print('Addition not successful: domain/ip pair not specified')
               # add 1 to the total commands counter
               totCmds += 1
               
          # else if the first character is a '-' (removing a domain name & IP pair):
          elif line[0] == '-':
               # try:
               try:
                    # get the domain name string
                    dom_str = line_split[1]
                    # call the take_out function
                    didRemove = take_out(dom_str, domTable, ipTable)
                    # if take_out returns True:
                    if didRemove:
                         # Output that the removal was successful
                         print('Domain name removed successfully')
                    # else:
                    else:
                         # Output that the removal was not successful
                         print('Removal not successful: Domain name not found')
               # except if the domain name string not specified (causes index error):
               except IndexError:
                    # output error message, 'domain name not specified'
                    print('Removal not successful: No domain name specified.')
               # add 1 to the total commands counter
               totCmds += 1
               
          # else if the first character is a '?' (searching the tables):
          elif line[0] == '?':
               # try:
               try:
                    # get the target string
                    target_str = line_split[1]
                    # call the table_lookup function
                    pair_indx = table_lookup(target_str, ipTable, domTable)
                    # if return of table_lookup function is -1:
                    if pair_indx == -1:
                         # output error message, 'Not found'
                         print('Search unsuccessful: Target string not found')
                    # else: (table_lookup was successful)
                    else:
                         # output domain name and IP pair
                         print('Domain name:', domTable[pair_indx])
                         print('IP address:', ipTable[pair_indx])
               # except if the target string not specified (causes index error)
               except IndexError:
                    # output error message: 'No target string specified'
                    print('Search unsuccessful: No target string specified')
               # add 1 to the total commands counter
               totCmds += 1
               
          # else if the first character is an 'L' (displaying tables in parallel array style):
          elif line[0] == 'L':
               # call the display_lists function
               display_lists(domTable, ipTable)
               # add 1 to the total commands counter
               totCmds += 1
               
          # else if the first character is an 'S' (sorting the tables):
          elif line[0] == 'S':
               # try:
               try:
                    # get the sort order string
                    sort_str = line_split[1]
                    # call the selection_sort function
                    selection_sort(domTable, ipTable, sort_str)
                    # output whether the data were sorted by domain or IP
                    if sort_str == 'Domain':
                         print('Data sorted by domain name')
                    elif sort_str == 'IP':
                         print('Date sorted by IP address')
                    else:
                         print('Sort unsuccessful: invalid sort order')
               # except if sort order string not specified (causes index error):
               except IndexError:
                    # output error message, 'No sort order specifed')
                    print('Sort unsuccessful: No sort order specified')
               # add 1 to the total commands counter
               totCmds += 1
          # else:
          else:
               # output an error message, 'Invalid commmand'
               print('Invalid command')
               # add 1 to the invalid commands counter
               totInvalids += 1
          print()
     print("***")
     # Output the total number of commands processed
     print(totCmds, 'commmands processed')
     # Output the number of invalid commands
     print(totInvalids, 'invalid commands detected')
     # Close the file
     file.close()

# function: table_lookup
def table_lookup(targ_str, ip_list, domain_list):
     '''
     Purpose: When given an IP or Domain Name, searches for its
          pair (opposite type) in the appropriate table and outputs it. 
     Preconditions: IP or domain name target as a string, the IP and domain tables
     Postconditions: Returns the index of the target string's pair; if not found, returns -1
     '''
     # Design:
     # split the target string by periods
     targ_split_dot = targ_str.split('.')
     # split the target string by colons
     targ_split_colon = targ_str.split(':')
     # if the target string characters up to the first period are all digits (IPv4)
     # or splitting the target string by colons yields more than three elements (IPv6)
     # the target string is an IP number:
     if targ_split_dot[0].isdigit() or len(targ_split_colon) > 3:
          # try:
          try:
               # assign the result to the index of the IP number
               result = ip_list.index(targ_str)
          # except if the ip or domain is not in the list:
          except ValueError:
               # assign result to -1
               result = -1
     # else (target string is a domain):
     else:
          # try:
          try:
               # assign the result to the index of the domain name
               result = domain_list.index(targ_str)
          # except if the ip or domain is not in the list:
          except ValueError:
               # assign result to -1
               result = -1
     # return result
     return result

# function: take_out
def take_out(domain, domain_list, ip_list):
     '''
     Purpose: To remove a domain name and IP pair from the tables
     Preconditions: The domain name as a string, the IP and domain lists
     Postconditions: Removes the pair from the tables; Returns boolean value
          to indicate success or failure
     '''
     # Design:
     # try:
     try:
          # find the index of the domain name
          indx = domain_list.index(domain)
          # remove the domain name from the domain name list
          del domain_list[indx]
          # remove the IP address at the same index from the IP list
          del ip_list[indx]
          # assign result to True
          result = True
     # except if the domain is not in the list:
     except ValueError:
          # assign result to False
          result = False
     # return the result
     return result

# function: put_in
def put_in(domain, ip, domain_list, ip_list):
     '''
     Purpose: Insert a new Domain Name and IP pair into the tables, 
         or change the IP of an existing domain name
     Preconditions: domain name and IP pair as strings, the IP and domain lists
     Postconditions: Returns none; inserts new domain name & IP pair 
         or changes IP of existing domain name
     '''
     # Design:
     # if the domain name is in the domain name list:
     if domain in domain_list:
          # find the index of the domain name
          indx = domain_list.index(domain)
          # change the IP at the same index in the IP table to the IP given
          ip_list[indx] = ip
     # else:
     else:
          # append the domain name to the domain name table
          domain_list.append(domain)
          # append the IP to the IP table
          ip_list.append(ip)

# function: selection_sort
def selection_sort(domain_list, ip_list, sort_var):
     '''
     Purpose: Sort the tables to ascending order according to either IP or domain name
     Preconditions: the domain name and IP lists, the sort order as a string (must be 'Domain' or 'IP')
     Postconditions: returns none; sorts the lists in ascending order
     '''
     # Design:
     # For each index except for the last:
     for i in range(len(domain_list) - 1):
          # if the user wants to sort by domain:
          if sort_var == 'Domain':
               # Find the smallest element in the unsorted part of the domain list:
               small = min(domain_list[i:])
               pos = domain_list.index(small, i)
               # Swap that element to index i in both lists
               domain_list[i], domain_list[pos] = domain_list[pos], domain_list[i]
               ip_list[i], ip_list[pos] = ip_list[pos], ip_list[i]               
          # if the user wants to sort by ip:
          elif sort_var == 'IP':
               # Find the smallest element in the unsorted part of the ip list:
               small = min(ip_list[i:])
               pos = ip_list.index(small, i)
               # Swap that element to index i in both lists
               domain_list[i], domain_list[pos] = domain_list[pos], domain_list[i]
               ip_list[i], ip_list[pos] = ip_list[pos], ip_list[i]
               
     
# function: display_lists
def display_lists(domain_list, ip_list):
     '''
     Purpose: Output the content of the two lists
     Preconditions: the domain name and IP lists
     Postconditions: returns none; outputs the lists to standard output in parallel array style
     '''
     # Design:
     # Output the 'Domain Name' and 'IP' headers
     print('Domain Name \t IP Number')
     print('--------------------------------------------------')
     # for each element in the domain name list:
     for i in range(len(domain_list)):
          # print the domain and its corresponding ip on the same line
          print(domain_list[i], '\t', ip_list[i])
     print('--------------------------------------------------')

main()