import sys

transliterate_words_table = {}
with open(sys.argv[1], 'r', encoding='utf-8') as table_f:
    for line in table_f:
        transliteration, word = line.rstrip().split('\t')
        transliterate_words_table[word] = transliteration

transliterate_chars_table = {}
back_transl_table = {}
with open(sys.argv[2], 'r', encoding='utf-8') as char_table_f:
    for line in char_table_f:
        c_transl, c = line.rstrip().split()
        if c not in transliterate_chars_table.keys():
            transliterate_chars_table[c] = []
        transliterate_chars_table[c].append(c_transl)
        back_transl_table[c_transl] = c

def transliterate_lem(wf, orig_lem):
    l = []
    for c in wf:
        l.append((back_transl_table[c], c))
    
    tgt_lem = ''
    for idx, c in enumerate(orig_lem):
        assert l[idx][0] == c
        tgt_lem += l[idx][1]
    return tgt_lem

with open(sys.argv[3], 'r', encoding='utf-8') as src_f, \
     open(sys.argv[4], 'w', encoding='utf-8') as tgt_f :
    for line in src_f:
        lang, wf, lem, pos, analysis = line.rstrip().split('\t')
        transliterated_wf = transliterate_words_table[wf]
        try:
            transliterated_lem = transliterate_lem(transliterated_wf, lem)
        except:
            transliterated_lem = lem

        print(lang, transliterated_wf, transliterated_lem, pos, analysis, file=tgt_f)
        
