my_dictionary={'Host':'gbl06673,gbl06663','Ip_Address':'172.17.6.10','SuperStack_Version':'Rhel_2.7.3','Operating_System':'Linux'}
print("My dictionary Host Names", my_dictionary['Host'])
my_dictionary['Host'] = my_dictionary['Host'] +',' +'gbl9972l'
print("Host Names :", my_dictionary['Host'])
print("IP Address :",my_dictionary['Ip_Address'])
del my_dictionary['Host']
print("After deleting Host from Dictionary :",my_dictionary)
my_dictionary.clear()
print("Printing Dictionary :",my_dictionary)
my_dictionary={'Host':'gbl06673,gbl06663','Ip_Address':'172.17.6.10','SuperStack_Version':'Rhel_2.7.3','Operating_System':'Linux'}
print("Dictionary Items :", my_dictionary.items())
print("Dictionary Keys :", my_dictionary.keys())
print("Dictionary Values :", my_dictionary.values())
print("Length of Dictionary :",len(my_dictionary))