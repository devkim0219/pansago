from urllib.request import urlopen
import urllib
import xml.etree.ElementTree as et
import csv

with open('law_list.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['no', 'title', 'name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for page in range(1, 2501, 1):
        oc_value = 'ssalbae1986'
        url = 'http://www.law.go.kr/DRF/lawSearch.do?target=prec&OC=' + oc_value + '&type=XML&page=' + str(page)

        request = urllib.request.Request(url)

        response = urlopen(request).read().decode('utf-8')
        print(response)
        print(type(response))

        tree = et.fromstring(response)

        no_list = []
        title_list = []
        name_list = []

        no = tree.findall('./prec/판례일련번호')
        title = tree.findall('./prec/사건명')
        name = tree.findall('./prec/사건종류명')

        for tmp in no:
            no_list.append(tmp.text)

        for tmp in title:
            title_list.append(tmp.text)

        for tmp in name:
            name_list.append(tmp.text)

        print(no_list)
        print(title_list)
        print(name_list)

        for i in range(0, len(no_list), 1):
            writer.writerow({'no': no_list[i], 'title': title_list[i], 'name': name_list[i]})