from pywhatkit import pw


exit()
# List of phone numbers
phone_numbers = [
    "+201003565463",  # Replace with actual phone numbers
    "+201098564982",
    "+201067564589"
    # Add more phone numbers as needed
]

# Message to be sent
message = "Hello! This is a test message sent using PyWhatKit."

# Sending messages to multiple numbers
for number in phone_numbers:
    # Sending message to each number
    # 15 is the hour and 0 is the minute
    pw.sendwhatmsg(number, message, 18, 34)
