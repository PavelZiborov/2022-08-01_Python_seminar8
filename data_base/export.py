import json

# где "file_path" это название файла в который нужно экспортировать, Data - база которую нужно экспортировать
def DataExport(file_path, data):

    with open(data, 'r', encoding='utf8') as file:
        BD = json.load(file)

    with open(file_path, 'w', encoding='utf8') as file:
        for i in BD:
            for (j, row) in enumerate(list(i.values())):
                if j != len(list(i.values()))-1:
                    file.write(f'{row};')
                else:
                    file.write(f'{row}')
            file.write('\n')
