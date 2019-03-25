import sys


# translit_files = {lang:lang+"_transliterator.txt" for lang in ["kaz","kir","tat","tur","bak","crh"]}
translit_files = {lang:lang+"-transliteration" for lang in ["cat","fra","ita","por","spa", "srd", "ast"]}

translit_tables = {}
for lang, translit_file in translit_files.items():
    table = {}
    with open(translit_file, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip('\n')
            items = line.split(' ')
            key, table[key] = items[0], items[1]
    translit_tables[lang] = table


src_file = sys.argv[1]
tgt_file = sys.argv[2]
with open(src_file, 'r', encoding="utf-8") as c, open(tgt_file, 'w', encoding="utf-8") as d:
    for line in c:
        line = line.rstrip()
        lang, wf, lem, pos, analysis = line.split('\t')
        print(f"lang {lang}, wf {wf}, lem {lem}, pos {pos}, analysis {analysis}")
        transliterated_wf = ''
        transliterated_lem = ''
        for letter in wf:
            transliterated_wf += translit_tables[lang].get(letter, letter)
        
        for letter in lem:
            transliterated_lem += translit_tables[lang].get(letter, letter)

        print('\t'.join((lang, transliterated_wf, transliterated_lem, pos, analysis)), file=d)



