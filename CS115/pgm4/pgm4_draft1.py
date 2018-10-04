'''
Author: Kelly Sovacool
Email: kellysovacool@uky.edu
Sec: 006
Date: 10 Apr. 2015
Purpose: Simulate a Domain Name Server, which keeps track of the domain names assigned to IP addresses.
    It allows the user to add new domain names and IPs, change IPs of existing domain names,
    remove domain names and IPs, find the pair of a domain name or IP,
    and display the domain names and IPs in parallel array style
Preconditions: a file with one command per line; the first character of each line
    must represent a known command symbol, followed by either a domain name, IP, 
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
     # Initialize an accumulator for total commands processed
     totCmds = 0
     # Initialize an accumulator for invalid commands
     totInvalids = 0
     # Get the file name of the commands from the user and open it
     file = open(input('Enter filename of simulator commands: '), 'r')
     print()
     # For each line in the file:
     for line in file.readlines():
          # output 'Command ' and the line
          print('Command', line.rstrip('\n'))
          # if the first character is a '+' (adding domain name & IP pair):
          if line[0] == '+':
               # split the string to make command, domain name, and IP strings
               cmd_str, dom_str, ip_str = line.split()
               # call the put_in function
               put_in(dom_str, ip_str, domTable, ipTable)
               # output whether it was successful or not
               if dom_str in domTable and ip_str in ipTable:
                    if domTable.index(dom_str) == ipTable.index(ip_str):
                         print('Addition successful')
                    else:
                         print('Addition not successful: domain or ip at incorrect index')
               else:
                    print('Addition not successful: domain or ip not found')
               # add 1 to the total commands accumulator
               totCmds += 1
               
          # else if the first character is a '-' (removing a domain name & IP pair):
          elif line[0] == '-':
               # split the string to make command and domain name strings
               cmd_str, dom_str = line.split()
               # call the take_out function
               didRemove = take_out(dom_str, domTable, ipTable)
               # if take_out returns True:
               if didRemove:
                    # Output that the removal was successful
                    print('Domain name removed successfully')
               # else:
               else:
                    # Output that the removal was not successful
                    print('Domain name not found')
               # add 1 to the total commands accumulator
               totCmds += 1
               
          # else if the first character is a '?' (searching the tables):
          elif line[0] == '?':
               # split the string to make command and target strings
               cmd_str, target_str = line.split()
               # call the look_up function
               pair = table_lookup(target_str, ipTable, domTable)
               # if return of look_up function is -1:
               if pair == -1:
                    # output error message, 'Not found'
                    print('Target string not found')
               # else:
               else:
                    # output domain name and IP pair
                    if target_str in domTable:
                         domain_name = target_str
                         ip_address = pair
                    elif target_str in ipTable:
                         domain_name = pair
                         ip_address = target_str
                    print('Domain name:', domain_name)
                    print('IP address:', ip_address)
               # add 1 to the total commands accumulator
               totCmds += 1
               
          # else if the first character is an 'L' (displaying tables in parallel array style):
          elif line[0] == 'L':
               # call the display_lists function
               display_lists(domTable, ipTable)
               # add 1 to the total commands accumulator
               totCmds += 1
               
          # else if the first character is an 'S' (sorting the tables):
          elif line[0] == 'S':
               # split the string into command and sort order strings
               cmd_str, sort_str = line.split()
               # call the selection_sort function
               selection_sort(domTable, ipTable, sort_str)
               # output whether the data were sorted by domain or IP
               if sort_str == 'Domain':
                    print('Data sorted by domain name')
               elif sort_str == 'IP':
                    print('Date sorted by IP address')
               # add 1 to the total commands accumulator
               totCmds += 1
               
          # else:
          else:
               # output an error message, 'Unknown commmand'
               print('Unknown command')
               # add 1 to the invalid commands accumulator
               totInvalids += 1
          print()
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
     Postconditions: Returns the target string's pair; if not found, returns -1
     '''
     # Design:
     # if input is in the IP list:
     if targ_str in ip_list:
          # get the index of the IP, and get the domain at that same index in the domain list
          result = domain_list[ip_list.index(targ_str)]
     # else if input is in the domain name list:
     elif targ_str in domain_list:
          # get the index of the domain name, and get the IP at that same index in the IP list
          result = ip_list[domain_list.index(targ_str)]
     else:
     # else:
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
     # if domain name is in domain name list:
     if domain in domain_list:
          # find the index of the domain name
          indx = domain_list.index(domain)
          # remove the domain name from the domain name list
          del domain_list[indx]
          # remove the IP address at the same index from the IP list
          del ip_list[indx]
          # assign result to True
          result = True
     # else:
     else:
          # assign result to False
          result = False
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
     # if the domain name is in the domain name table:
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
     Preconditions: the domain name and IP lists, the sort order as a string (must be 'Domain' or 'IP'
     Postconditions: returns none; sorts the lists in ascending order
     '''
     # Design:
     # make a copy of the unsorted domain_list
     old_dom_list = domain_list.copy()
     # make a copy of the unsorted ip list
     old_ip_list = ip_list.copy() 
     # if user sorts by domain:
     if sort_var == 'Domain':
          # sort the domain_list in ascending order
          domain_list.sort()
          # for elements in the domain name list:
          indx = 0
          for ele in domain_list:
               # get the element at its new index
               ele = domain_list[indx]
               # find the position of the element in the unsorted list
               old_pos = old_dom_list.index(ele)
               # assign the ip from the unsorted list to its new index in the sorted list
               ip_list[indx] = old_ip_list[old_pos]
               indx += 1
     # else if user sorts by IP:
     elif sort_var == 'IP':
          # sort the ip_list in ascending order
          ip_list.sort()
          # for elements in the IP list:
          indx = 0
          for ele in ip_list:
               # get the element at its new index
               ele = ip_list[indx]
               # find the position of the element in the unsorted list
               old_pos = old_ip_list.index(ele)
               # assign the domain from the unsorted list to its new index in the sorted lsit
               domain_list[indx] = old_dom_list[old_pos]
               indx += 1
     # else:
     else:
          # output an error message, 'Sort order not recognized'
          print('Sort order not recognized')

# function: display_lists
def display_lists(domain_list, ip_list):
     '''
     Purpose: Output the content of the two lists
     Preconditions: the domain name and IP lists
     Postconditions: returns none; outputs the lists to standard output in parallel array style
     '''
     # Design:
     prev_len = 0
     largest_len = 0
     for ele in domain_list:
          curr_len = len(ele)
          if curr_len > prev_len:
               largest_len = curr_len
          prev_len = curr_len
     spaces = ' ' * (largest_len - len('Domain Name'))
     print('Domain Name', spaces, 'IP Number')
     print('--------------------------------------------------')
     for ele in domain_list:
          spaces = ' ' * (largest_len - len(ele))
          print(ele, spaces, ip_list[domain_list.index(ele)])
     print('--------------------------------------------------')
main()