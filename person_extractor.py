from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsNERTagger,
    NamesExtractor,
    NewsSyntaxParser,
    Doc
)

result_per = {}

# -*- coding: latin-1 -*-


lines = ['справка от Иванова Павла Петровича',
    'мои отчеты c портала',
         'отчет Ивана Иванова за предыдущий месяц',
         'приказ Павлова',

         'квитанции Иванова '
         ]


def per(line):
    result_per = {}
    emb = NewsEmbedding()
    segmenter = Segmenter()
    morph_vocab = MorphVocab()
    ner_tagger = NewsNERTagger(emb)
    syntax_parser = NewsSyntaxParser(emb)
    names_extractor = NamesExtractor(morph_vocab)
    doc = Doc(line)
    doc.segment(segmenter)
    doc.tag_ner(ner_tagger)
    doc.parse_syntax(syntax_parser)
    for span in doc.spans:
        span.normalize(morph_vocab)
        name , surname, patronymic_name = '','', ''
        if span.type == 'PER':
            span.extract_fact(names_extractor)
            try:
                name = span.fact.as_dict['first']
            except:
                pass
            try:
                surname = span.fact.as_dict['last']
            except:
                pass
            try:
                patronymic_name = span.fact.as_dict['middle']
            except:
                pass
            result_per = {
                "line": line,
                "text": span.text,
                "firstname": name,
                "surname": surname,
                "patronymic_name": patronymic_name,
                "start": span.start,
                "stop": span.stop,
            }
            # print(result_per)
    if line.find("мои ") or line.find("мой ") or line.find("моё ") :
        result_per["surname"] = '@Me'
    return result_per


if __name__ == "__main__":
    for line in lines:
        map = per(line)
        print(map)
