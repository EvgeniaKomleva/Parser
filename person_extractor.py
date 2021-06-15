from natasha import (
    Segmenter,
    NewsEmbedding,
    NewsNERTagger,
    Doc
)

text = '''
Иисус ходил по воде. Простите, еще несколько цитат из приговора. «…Отрицал существование
Иисуса и пророка Мухаммеда», «наделял Иисуса Христа качествами
ожившего мертвеца — зомби» [и] «качествами покемонов —
представителей бестиария японской мифологии, тем самым совершил
преступление, предусмотренное статьей 148 УК РФ
'''

emb = NewsEmbedding()
segmenter = Segmenter()
ner_tagger = NewsNERTagger(emb)

doc = Doc(text)
doc.segment(segmenter)
doc.tag_ner(ner_tagger)
doc.ner.print()
for span in doc.spans:
    print(span)