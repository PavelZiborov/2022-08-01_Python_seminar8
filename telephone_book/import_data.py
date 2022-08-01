def Import(file_path, data): # где "file_path" это название файла который необходимо добавить в базу "data" 
    with open(file_path, 'r') as file:
        for line in file:
            data.append(line.split(';'))
    return data