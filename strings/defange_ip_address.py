# Given a valid(IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".
# Example:
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

ip_address = '255.100.50.0'
new_ip_address = ip_address.replace('.', '[.]')
print(new_ip_address)