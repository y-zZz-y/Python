# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('test.txt', 'r') as f:
    content = f.readlines()
    print(f'Строк в файле {len(content)}')
    statistic = [f'В строке {i}: {len(line.split())} слов' for i, line in enumerate(content)]
    for _ in statistic:
        print(_)
