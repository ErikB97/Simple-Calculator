# Python Calculator

print "  _____      _            _       _             " #Unnecessary but cool ASCII art.
print " / ____|    | |          | |     | |            "
print "| |     __ _| | ___ _   _| | __ _| |_ ___  _ __ "
print "| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|"
print "| |___| (_| | | (__| |_| | | (_| | || (_) | |   "
print " \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   "
print "                  Version 1.0                   "
print ""
l = 0

while l == 0: #Creates a loop, so the process can repeat as long as l = 0.
	print "1 - Add"
	print "2 - Subtract"
	print "3 - Multiply"
	print "4 - Divide"
	print "5 - Quit"
	input = raw_input("What would you like to do? ")
	if float(input) == 1: #Addition
		float1 = raw_input("Enter the first number: ")
		float2 = raw_input("Enter the second number: ")
		float3 = float(float1) + float(float2)
		print "" #Extra spacing to make the result more visible
		print float3
		print ""
	elif float(input) == 2: #Subtraction
		float1 = raw_input("Enter the first number: ")
		float2 = raw_input("Enter the second number: ")
		float3 = float(float1) - float(float2)
		print ""
		print float3
		print ""
	elif float(input) == 3: #Multiplication
		float1 = raw_input("Enter the first number: ")
		float2 = raw_input("Enter the second number: ")
		float3 = float(float1) * float(float2)
		print ""
		print float3
		print ""
	elif float(input) == 4: #Division
		float1 = raw_input("Enter the first number: ")
		float2 = raw_input("Enter the second number: ")
		float3 = float(float1) / float(float2)
		print ""
		print float3
		print ""
	else: #When anything other than 1-4 is entered.
		l = 1 #Breaks the loop, causing the program to end.
