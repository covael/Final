days_of_christmas = (('first', 'A Partridge in a Pear Tree.'), ('second', 'Two Turtle Doves, and'),
           ('third', 'Three French Hens,'), ('fourth', 'Four Calling Birds,'),
           ('fifth', 'Five Golden Rings,'), ('sixth', 'Six Geese a Laying,'),
           ('seventh', 'Seven Swans a Swimming,'), ('eighth', 'Eight Maids a Milking,'),
           ('ninth', 'Nine Ladies Dancing,'), ('tenth', 'Ten Lords a Leaping,'),
           ('eleventh', 'Eleven Pipers Piping,'), ('twelfth', 'Twelve Drummers Drumming,'))

day = int(input('What day of Christmas is it? (1-12) ')) - 1 
print("\nOn the {} day of Christmas my true love sent to me: ".format(days_of_christmas[day][0]))
for gift in range(day, -1, -1):          
    print(days_of_christmas[gift][1])
  
