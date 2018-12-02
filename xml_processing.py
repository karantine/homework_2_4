import xml.etree.ElementTree as ET


def frequent_words_xml():

    tree = ET.parse("newsafr.xml")
    root = tree.getroot()
    words_freq = {}
    xml_items = root.findall("channel/item")
    for item in xml_items:
        word_list = item.find("description").text.split(' ')
        for word in word_list:
            if len(word) > 6:
              if word not in words_freq:
                words_freq[word] = 1
              else:
                words_freq[word] += 1
    # print('10 наиболее часто встречающихся слов:')
    # sorted_by_value = sorted(words_freq.items(), key=lambda kv: kv[1], reverse=True)
    # for entity in range(0, 10):
    #     print(sorted_by_value[entity])

    word_len = []
    for key, value in words_freq.items():
        word_to_add = [value, key]
        word_len.append(word_to_add)

    word_len_sorted = sorted(word_len)
    print('10 наиболее часто встречающихся слов с количеством повторений:')
    for entity in reversed(word_len_sorted[-10::]):
        print('{} - {}'.format(entity[1], entity[0]))

if __name__ == "__main__":
    frequent_words_xml()
