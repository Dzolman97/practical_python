contacts = {
   'number': 4,
   'students':
   [
      {"name": "Sarah Holderness", "email": "sarah@example.com"},
      {"name": "Harry Potter", "email": "harrypott3r@example.com"},
      {"name": "Tony Stark", "email": "tonyst4rk@example.com"},
      {"name": "Ron Weasley", "email": "RonWeasley@example.com"}
   ]
}

for student in contacts["students"]:
   print(student["email"])