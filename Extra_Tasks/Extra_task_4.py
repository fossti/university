import re
import urllib.request
import csv
address = 'https://msk.spravker.ru/avtoservisy-avtotehcentry/'
response = urllib.request.urlopen(address)
html = response.read().decode('utf-8')

pattern = r"(?:-link\">)(?P<Name>[^<]+)"\
    r"(?:[^o]*[^l]*.*\n *(?P<Address>[^\n]+))"\
    r"(?:\s*.*>\s*.*>\s*.*>(?:\s*<d[^>]*>(?:\s*.*\s*.*>(?P<Phone_Number>[^<]+))?.*>\s*</dl>)"\
    r"(?:\s*<.*>(?:\s*<.*\s*<.*>(?P<WorkHours>[^<]+))?</dd>)?)?"
matches = re.findall(pattern, html)

result = 'add_info.csv'
with open(result, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Адрес', 'Номер Телефона', 'Часы работы'])
    writer.writerows(matches)

print(f"Данные сохранены в файл {result}.")
