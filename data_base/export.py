import json

def DataExport(file_path, data): # где "file_path" это название файла в котором нужно экспортировать, Data - база которую нужно экспортировать

    with open(file_path, 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)

