import ipaddress as ipx # imports module, using an alias 
from pathlib import Path # making code portable 
import sys

#This is REspomreponsible for all the validation , and appedind to correct list than we based our result file on 
def version_checker(var_sample):
    list_valid_ip = []
    list_invalid_ip = []
    list_ipv6 = []

    for i in var_sample:
        try:
            var_ip = ipx.ip_interface(i)
            if var_ip.version == 4:
                list_valid_ip.append(var_ip)

            elif var_ip.version == 6:
                list_ipv6.append(var_ip)

        except ValueError:
            list_invalid_ip.append(i)

        
    return list_valid_ip, list_invalid_ip, list_ipv6

# Gives all the info, about validated ip 
def all_info(selected_ip):
    var_net = selected_ip.network
    #all specxs using ipaddress modules, utility 
    var_network_address = var_net.network_address
    var_subnet_mask = var_net.netmask
    var_broadcast_address = var_net.broadcast_address
    list_hosts = list(var_net.hosts())
    var_usable_hosts = len(list_hosts) #no oh hosts, excluded na&ba 
    
    #created another object to keep explicity and a little diffrentiation in code aswell (kri_ip)
    kri_ip = selected_ip.ip
    if kri_ip.is_loopback:
        ip_class = "Loopback"
    elif kri_ip.is_private:
        ip_class = "Private"
    elif kri_ip.is_global:
        ip_class = "Public/Global"
    elif kri_ip.is_multicast:
        ip_class = "Multicast"
    elif kri_ip.is_link_local:
        ip_class = "Link-local"
    elif kri_ip.is_reserved:
        ip_class = "Reserved"
    elif kri_ip.is_unspecified:
        ip_class = "Unspecified"
    else:
        ip_class = "Other/Special"

  # #returns a tuple of ipobjects 

    return kri_ip, var_net, var_network_address, var_broadcast_address, var_subnet_mask, var_usable_hosts, ip_class, var_net, var_network_address, var_broadcast_address, var_subnet_mask, var_usable_hosts

print(f"Validates & Analyze ip in format:(host/cidr)")
print()

#____________________________FILE IO ____________________________________________________________________________________________#

BASE_DIR = Path(__file__).resolve().parent
input_path = BASE_DIR / "list_ips.txt" # Please put your files , name here :)   [# $ # $ # $ # $ # $ ] 📝📝📝📝📝📝
output_path = BASE_DIR / "Results.txt" # Custom, you may replace with desired name :) [# $ # $ # $ # $ # $ ] 📝📝📝📝📝📝

if not input_path.exists():
    print(f"Error: {input_path}, not found in {BASE_DIR}")
    print()
    print(f"Exiting the code, Please use defined file")
    sys.exit(1)

with input_path.open("r", encoding="utf-8") as f:
    #makes a list of strings, strips white spaces!
    var_data = f.read()
    var_sample = [line.strip() for line in var_data.splitlines()]

    list_valid_ip, list_invalid_ip, list_ipv6 = version_checker(var_sample)

with output_path.open("w", encoding="utf-8") as k:
    k.write("The list of valid ip's is:✅")
    k.write("\n")

    for ip in list_valid_ip:
       k.write(str(ip) + "\n")

    k.write("\n")
 
    k.write("The list of invalid ip's is:❌")
    for a in list_invalid_ip:
       k.write("\n")
       k.write(a)

print(f"Results successfully written to: {output_path}")

#using enumerate to print a presentable list 
print(f"The final list of the valid ips is:")
for idx, var_tup in enumerate(list_valid_ip, start=1):
    # print(f"The final list of the valid ips is:")
    print(f"{idx} > {var_tup}")
print()
print("Further, select the number of ip in the list you want information about")

#now that we can select ips, we would perform operations
#Taking input + calling all_info function 
#loop for error handling and prompt completion 

while True:
    try:
        var_input_choice = int(input(f"Proceed with choice(Egs:1)>"))
        selected_ip = list_valid_ip[var_input_choice-1]
        if 0 < var_input_choice <= len(list_valid_ip):
            kri_ip, var_net, var_network_address, var_broadcast_address, var_subnet_mask, var_usable_hosts, ip_class, var_net, var_network_address, var_broadcast_address, var_subnet_mask, var_usable_hosts = all_info(selected_ip) #unpacked my tupl in ipoobjects
        #printing all specs 
            print(f"Network_Address = {str(var_network_address)} ")
            print(f"Broadcast_Address = {str(var_broadcast_address)} ")
            print(f"Subnet_mask = {str(var_subnet_mask)} ")
            print(f"Number of Hosts = {var_usable_hosts} ")
            print(f"Class: {str(ip_class)}")
            print()
            print("Exiting the code, Thanks for your time 😊")
            break
        else:
            print("Please, Enter a valid index of list ")
    except IndexError:
        print("Please refer the insexing of the list ")
    except ValueError:
        print("Please, enter a no refreing list of the valid ip's ")

