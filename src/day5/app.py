from demo1 import Book,Author,DigitalBook

author1 = Author(2123,"Fritzof Capra","fritzof@gmail","45454646")
book1 =  Book(1212,"Tao of Physics",author1,"12-Mar-2000")

print(book1.get_details())

book1.update_dop("12-Apr-2000")

print(book1.get_details())

author2 =Author(232,'Stephen H','step@gmail','554534')
book1 =DigitalBook(455,'On The Shoulders of the Giant',author2,'11-Nov-2000',45)

print(book1)

book1.update_dop('2-dec-1998')

print(book1)

