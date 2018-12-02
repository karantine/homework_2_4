import json


def frequent_words_json():

    with open("newsafr.json", encoding="utf-8") as datafile:
        json_data = json.load(datafile)
        news_list = json_data['rss']['channel']['items']

        word_dict = {}

        for news_item in news_list:
            words = news_item["description"].split()
            for word in words:
                if len(word) > 6:
                    if word in word_dict.keys():
                        word_dict[word] += 1
                    else:
                        word_dict[word] = 1

        word_len = []
        for key, value in word_dict.items():
            word_to_add = [value, key]
            word_len.append(word_to_add)

        word_len_sorted = sorted(word_len)

        print('10 наиболее часто встречающихся слов с количеством повторений:')
        for entity in reversed(word_len_sorted[-10::]):
            print('{} - {}'.format(entity[1], entity[0]))

if __name__ == "__main__":
    frequent_words_json()
