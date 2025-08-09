
from src.data import DATA_DIR


from typing import Union
from pathlib import Path
import json
import arabic_reshaper
from bidi.algorithm import get_display
from collections import Counter
from wordcloud import WordCloud


class ChatStatistics:
    def __init__(self, chat_json: Union[str, Path]):
        with open(chat_json) as f:
            self.chat_data = json.load(f)

        stop_words = open(DATA_DIR / 'stopwords.txt').readlines()
        stop_words = list(map(str.strip, stop_words))   
    def generate_word_cloud(self, output_dir):
        text_content = ''

        for msg in self.chat_data['messages']:
            if type(msg['text']) is str:
                text_content += f" {msg['text']}"

        text_content = arabic_reshaper.reshape(text_content)
        text_content = get_display(text_content)

        wordcloud = WordCloud(font_path=str(DATA_DIR / 'BHoma.ttf'), background_color='white',width=900,height=900).generate(text_content)

        wordcloud.to_file(str(Path(output_dir) / 'wordcloud.png'))




if __name__ == "__main__":
    chat_stats = ChatStatistics(chat_json = DATA_DIR / 'online.json')
    chat_stats.generate_word_cloud(output_dir = DATA_DIR)