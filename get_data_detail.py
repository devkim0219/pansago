from urllib.request import urlopen
import urllib
import xml.etree.ElementTree as et
import csv
import re

#html 태그 제거 메서드
def substringTags(text):
    result = re.sub('<(/)?([a-zA-Z]*)(-[a-zA-Z]*)?(-[a-zA-Z]*)?(-[a-zA-Z]*)?(\\s[a-zA-Z]*(\\s)?(\\s)?=[^>]*)?(\\s)*(/)?>', '', text)

    return result

with open('law_list.csv', 'r', encoding='utf-8') as f:
    rdr = csv.reader(f)
    
    law_no_list = []

    for line in rdr:
        law_no_list.append(line[0])

    del law_no_list[0]

    # print(law_no_list)

with open('law_list_detail_2.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['law_no', 'law_title', 'law_event_no', 'law_date', 'law_seongo', 'law_court_name', 'law_court_code', 'law_event_type', 'law_event_code', 'law_result', 'law_judge', 'law_judge_summary', 'law_ref', 'law_ref_precedent', 'law_content']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for law_no in law_no_list:
        oc_value = 'ssalbae1986'
        url = 'http://www.law.go.kr/DRF/lawService.do?target=prec&OC=' + oc_value + '&type=XML&ID=' + str(law_no)

        request = urllib.request.Request(url)

        response = urlopen(request).read().decode('utf-8')
        print(response)
        print(type(response))

        tree = et.fromstring(response)

        # no_list = []
        # title_list = []
        # name_list = []

        law_no = tree.findtext('./판례정보일련번호')
        law_title = tree.findtext('./사건명')
        law_event_no = tree.findtext('./사건번호')
        law_date = tree.findtext('./선고일자')
        law_seongo = tree.findtext('./선고')
        law_court_name = tree.findtext('./법원명')
        law_court_code = tree.findtext('./법원종류코드')
        law_event_type = tree.findtext('./사건종류명')
        law_event_code = tree.findtext('./사건종류코드')
        law_result = tree.findtext('./판결유형')
        law_judge = tree.findtext('./판시사항')
        law_judge_summary = tree.findtext('./판결요지')
        law_ref = tree.findtext('./참조조문')
        law_ref_precedent = tree.findtext('./참조판례')
        law_content = tree.findtext('./판례내용')

        law_judge = substringTags(law_judge)
        law_judge_summary = substringTags(law_judge_summary)
        law_ref = substringTags(law_ref)
        law_ref_precedent = substringTags(law_ref_precedent)
        # law_content = substringTags(law_content)

        writer.writerow({'law_no' : law_no, 'law_title': law_title, 'law_event_no': law_event_no, 'law_date': law_date, 'law_seongo': law_seongo, 'law_court_name': law_court_name, 'law_court_code': law_court_code, 'law_event_type': law_event_type, 'law_event_code': law_event_code, 'law_result': law_result, 'law_judge': law_judge, 'law_judge_summary': law_judge_summary, 'law_ref': law_ref, 'law_ref_precedent': law_ref_precedent, 'law_content': law_content})



