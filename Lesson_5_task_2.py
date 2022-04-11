#a = open("sample1.txt", "w")
with open('sample1.txt') as a:
    rows = a.readlines()
    rows_2 = [row.split() for row in rows]
rows_count, words_count = len(rows), sum([len(word_list) for word_list in rows_2])

print(f"Всего строк - {rows_count}, всего слов - {words_count}")