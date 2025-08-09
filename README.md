# Telegram Statistics
this program will create a word cloud png image to show which words has The most frequent words in a telegram group chat as json file.

## How to Run
first, in main repo directory , run the following code to add `src` to your `PYTHONPATH`:
```
export PYTHONPATH=${PWD}
```
then run :
```
python src/chat_statistics/stats.py
```
to generate a word cloud of json data in `DATA_DIR`

![Farsi Word Cloud from Telegram Chat](https://github.com/matinrasooli/TelegramBot/blob/main/src/data/wordcloud.png?raw=true)
