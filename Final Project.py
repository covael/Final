##Creates a list of days, and object of day
"""This programs takes an input 1-12 and outputs the listed days descending from the top. An invalid input will return the program.
        >>> 5
        On the fifth day of Christmas my true love sent to me: 
        Five Golden Rings,
        Four Calling Birds,
        Three French Hens,
        Two Turtle Doves, and
        A Partridge in a Pear Tree.
"""
days_of_christmas = (('first', 'A Partridge in a Pear Tree.'), ('second', 'Two Turtle Doves, and'),
           ('third', 'Three French Hens,'), ('fourth', 'Four Calling Birds,'),
           ('fifth', 'Five Golden Rings,'), ('sixth', 'Six Geese a Laying,'),
           ('seventh', 'Seven Swans a Swimming,'), ('eighth', 'Eight Maids a Milking,'),
           ('ninth', 'Nine Ladies Dancing,'), ('tenth', 'Ten Lords a Leaping,'),
           ('eleventh', 'Eleven Pipers Piping,'), ('twelfth', 'Twelve Drummers Drumming,'))
##Takes input 1-12 
day = int(input('What day of Christmas is it? (1-12) ')) - 1 
##Returns message with listed days in the return message
print("\nOn the {} day of Christmas my true love sent to me: ".format(days_of_christmas[day][0]))
##Cycles down through days list
for gift in range(day, -1, -1):          
    print(days_of_christmas[gift][1])
    
if __name__=='__main__':
    import doctest
    doctest.testmod()
  
