current_movies = {
   'The Grinch': '10:00am',
   'Rudolph': '3:00pm',
   'Christmas Vacation': '5:00pm',
   'Frosty': '4:00pm'
}

print("We're currently showing the following movies:")
for key in current_movies:
   print(key)

movie = str(input('What movie would you like the times for?\n'))

showtimes = current_movies.get(movie)
if showtimes == None:
   print("the requested movie isn't playing.")
else:
   print(movie, "is playing at", showtimes)