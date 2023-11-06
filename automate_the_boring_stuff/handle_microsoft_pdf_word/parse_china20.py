import os

import imageio
import matplotlib.pyplot as plt
from pathlib import Path

import wordcloud
from imageio import imread
from PyPDF2 import PdfWriter, PdfReader
import jieba
from wordcloud import WordCloud, ImageColorGenerator

"""
Task: parse china20.pdf
    1. pdf2 obtain the designate range.
    2. pdf2 extract text from pdf
    3. jieba handle chinese word
    4. wordcloud generate img which text appear most frequently
"""


class CPC:
    def __init__(self):
        self._result_fd = None
        self._data_fd = Path.cwd()
        self.jieba_list = []

    @property
    def data_fd(self):
        return self._data_fd

    @data_fd.setter
    def data_fd(self, value):
        if os.path.exists(value) and os.path.isfile(value):
            self._data_fd = value

    def merge_pdf(self, start=0, end=0, filename='result.pdf'):
        self._result_fd = self._data_fd.parent / Path(filename)
        with open(self._data_fd, "rb") as origin:
            with open(self._result_fd, "wb") as result:
                with PdfWriter() as merger:
                    merger.append(fileobj=origin, pages=(start, end))
                    merger.write(result)

    def extract_text_from_pdf(self):
        reader = PdfReader(self._result_fd)
        for i in range(len(reader.pages)):
            yield reader.pages[i].extract_text()

    def text_segmentation_chinese(self):
        for text in self.extract_text_from_pdf():
            self.jieba_list.extend(jieba.lcut(text))

    def word_cloud(self, maskbg, filename='result.png'):
        mask = imageio.v2.imread(maskbg)
        wc = wordcloud.WordCloud(width=1000,
                                 height=700,
                                 background_color='white',
                                 font_path='msyh.ttc',
                                 mask=mask,
                                 scale=15,
                                 stopwords={'和', '的', '地', '是', '在', '了', '以', '等', '从', '对'})
        wc.generate(" ".join(self.jieba_list))
        wc.to_file(filename)


if __name__ == '__main__':
    data_dir = Path().cwd() / Path('data')
    cpc = CPC()
    cpc.data_fd = data_dir / Path('china20.pdf')
    cpc.merge_pdf(start=150, end=176)
    cpc.text_segmentation_chinese()
    cpc.word_cloud(maskbg=data_dir / Path('chinamap.png'),
                   filename=str(data_dir / Path('result.png')))
