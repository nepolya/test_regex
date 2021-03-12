import re
with open("proceedings.txt", mode='r', encoding='utf-8') as f:
    names_find=r'References\n([A-Za-z]+.\s\w+)'
    lines=f.readlines()
    smth=''.join(lines)
    allresults=re.findall(names_find, smth)
    articles_find=r'References\n[A-Za-z]+.\s\w+.(\s.*[a-z]\W)'
    print(allresults)
with open('proceedings.txt', mode='r', encoding='utf-8') as filename:
    rows=filename.readlines()
    articles=''.join(rows)
    all_articles=re.findall(articles_find, articles)
    print(all_articles)