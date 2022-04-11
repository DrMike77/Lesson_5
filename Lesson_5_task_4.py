#transl = {"One": "Один","Two": "Два","Three": "Три","Four": "Четыре", "Five": "Пять", "Six": "Шесть"}
#converted_rows = []
#with open("sample_numbers_eng.txt", encoding='cp1251') as input_data:
#    for row in input_data:
#       name, value = row.split(' - ')
#        converted_rows.append(f"{transl[name]} - {value}")
#with open("sample_numbers_ru.txt", "w", encoding='cp1251') as output_data:
#    output_data.writelines(converted_rows)
transl = {"One": "Один","Two": "Два","Three": "Три","Four": "Четыре", "Five": "Пять", "Six": "Шесть"}
converted_rows = []
with open("sample_numbers_eng.txt", encoding='utf-8') as input_data:
    for row in input_data:
        name, value = row.split(' - ')
        converted_rows.append(f"{transl[name]} - {value}")
with open("sample_numbers_ru.txt", "w", encoding='utf-8') as output_data:
    output_data.writelines(converted_rows)