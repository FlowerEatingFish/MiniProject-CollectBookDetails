# coding=UTF-8
from simpleparser import *
from read import *
from book import *
import write
import time

isbn = IsbnCollection()
database = []

for i in isbn.isbnList:
    if type(i) is int:
        parser = SimpleParser(i)
        data = Book(parser.data)
        database.append(data)
        time.sleep(10)

write.ExportResult(database)
