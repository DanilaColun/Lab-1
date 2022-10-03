import csv
from operator import itemgetter

search = input("Поиск книги по автору, выпуск до 2002 года: ")

bibl_tags = open("bibl_tags.txt", "w", encoding="windows-1251")
publisher_file = open("publisher_file.txt", "w", encoding="windows-1251")
bp = open("20_popular_books.txt", "w", encoding="windows-1251")

publisher_file.write("\n" + "Перечень издательств без повторений." + "\n" + "\n")

publishers = []
books_popular = []
pl = set()
flag = 0
count = -1
row_symbols_counter = 0

with open("books-en.csv","r", encoding="windows-1251") as csvfile:
    table = list(csv.reader(csvfile, delimiter=";"))


    for row in table: # Всего сколько записей
        count +=1
        row_symbols = []
        for s in row:
            row_symbols.append(s)

        if len(row[1]) > 30: # Записи больше 30 символов
            row_symbols_counter += 1

        lower_case = row[2].lower()
        index = lower_case.find(search.lower())
        book_date = ""

        if index != -1: # Поиск книги по автору, ограничение до 2002 года
            book_date = book_date + row[3]
            if int(book_date) < 2002:
                print("Название книги: " + row[1] + ". " + "Автор: " + row[2] + ". " + "Дата выпуска: " + row[3])
                flag = 1



    for row in table:  # Все издательства без повторений
        if row[4] not in publishers:
            publishers.append(row[4])
    publisher_file.write(str(publishers))



    bp.write("\n 20 самых популярных книг: \n") # 20 самых популярных книг
    for row in table:
        row[5] = int(row[5])
    table_sorted = sorted(table, key=itemgetter(5), reverse=True)[:30]
    for i in range(1,21):
        bp.write(str(i) + ". " + str(table_sorted[i][1]) + ". " + str(table_sorted[i][2]) + ". " + str(table_sorted[i][3]) + " " + "Downloads: " + str(table_sorted[i][5]) + "\n")



    for i in range(15, 35): # 20 ссылок библиографических
        bibl_tags.write(str(i - 14) + ". " + table[i][2] + ". " + table[i][1] + " - " + table[i][3] + "\n")

    if (flag == 0):
        print("Nothing found.")






print("Всего записей: "+str(count)+"\n"+"Записи длиннее 30 символов: "+str(row_symbols_counter))
print('20 ссылок библиографических находятся в "bibl_tags.txt", все издательства находятся в "publisher_file.txt"')
print('20 самых популярных книжек по количеству скачиваний находятся в "20_popular_books.txt"')

bibl_tags.close()
publisher_file.close()
bp.close()


