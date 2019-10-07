user = input("Would you like to Encode a message or Decode a message? ").upper()
number = input("What is your cipher number? ")
message = input("Please input your message: ")
altered_message = ""
if user == "ENCODE":
    for x in range(0, len(message)):
        if message[x] == message[x].upper():
            if ord(message[x]) + int(number) > 90:
                altered_message += (chr((ord(message[x]) + int(number)) - 25))
            elif message[x] in ":,;,',>,<,.,?,/,,,],[,},{,\,|,!, +,=,-,~,#,),(,&,^,%,$,@,`,\" ":
                altered_message += (chr(ord(message[x])))
            else:
                altered_message += (chr(ord(message[x]) + int(number)))
        elif message[x] == message[x].lower():
            if ord(message[x]) + int(number) > 122:
                altered_message += (chr((ord(message[x]) + int(number)) - 25))
            elif message[x] in ":,;,',>,<,.,?,/,,,],[,},{,\,|,!, +,=,-,~,#,),(,&,^,%,$,@,`, \" ":
                altered_message += (chr(ord(message[x])))
            else:
                altered_message += (chr(ord(message[x]) + int(number)))
    print(altered_message)
elif user == "DECODE":
    for x in range(0, len(message)):
        if message[x] == message[x].upper():
            if message[x] in ":,;,',>,<,.,?,/,,,],[,},{,\,|,!, +,=,-,~,#,),(,&,^,%,$,@,`, \" ":
                altered_message += (chr(ord(message[x])))
            elif (ord(message[x]) - int(number)) < 65:
                altered_message += (chr((ord(message[x]) - int(number)) + 25))
            else:
                altered_message += (chr(ord(message[x]) - int(number)))
        elif message[x] == message[x].lower():
            if message[x] in ":,;,',>,<,.,?,/,,,],[,},{,\,|,!, +,=,-,~,#,),(,&,^,%,$,@,`, \" ":
                altered_message += (chr(ord(message[x])))
            elif (ord(message[x]) - int(number)) < 97:
                altered_message += (chr((ord(message[x]) - int(number)) + 25))
            else:
                altered_message += (chr(ord(message[x]) - int(number)))
    print(altered_message)




