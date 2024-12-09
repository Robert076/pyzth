class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self): 
        return self.title + " " + self.author
    def __len__(self):
        return len(self.title)
    def __del__(self):
        print('Just deleted the book')

#__str__ e ca o metoda predefinita care spune cum se transpune obiectul in string
#daca nu ai si dai print apare Object at memory ... 
#e o metoda speciala care exista deja pe chestiile built-in
#la fel e si __len__

b = Book('Python is great', 'Robert')

print(b)
print(len(b))
