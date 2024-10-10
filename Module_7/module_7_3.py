class WordsFinder:
    __file_names = ()
    __all_words = {}
    def __init__(self, *files):
        self.__file_names = files

    def get_all_words(self):
        return self.__all_words
    def find(self, word):
        for file_ in self.__file_names:
            with open(file_, encoding='utf_8') as file:
                if word.lower() in file:
                    return {f'{file_.name}: {file_.tell}'}
    def count(self,text):
        for file_ in self.__file_names:
            with open(file_, encoding='utf_8') as file:
                if text.lower() in file:
                    return {f'{file_.name}: {file_.tell}'}

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
