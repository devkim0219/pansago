def make_stopword():
    stopwords_kr = []

    with open('./stopwords_ko.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
        for line in lines:
            line = line.replace('\n', '')
            line = line.strip()
            stopwords_kr.append(line)

    return stopwords_kr