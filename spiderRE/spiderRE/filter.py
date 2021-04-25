import html
import re


class FilterClass:

    def __init__(self):
        pass


    def general_filter(self, text_lis):
        text = ''.join(text_lis)
        text = text.strip().replace('\n', '').replace('\r', '')
        return text


    def general_sentence_filter(self, text_lis):
        text = ''.join(text_lis)
        text = text.strip().replace('\n', '').replace('\r', '')
        if len(text) < 6:
            text = ''
        if (len(text.split(' ')) < 3) and (len(re.findall('\W', text)) == 0):
            text = ''
        return text


    def en_sentence_filter(self, text_lis):
        """
        英语句子的过滤
        \u2E80-\u9FFF中文， \uAC00-\uD7A3韩语
        """
        text = ''.join(text_lis)
        if (text == '') or text is None:
            return ''
        # ---
        text = html.unescape(text)
        # ---
        text = text.strip().replace('\n', '').replace('\r', '').replace('\t', ' ').replace('\xa0', ' ').strip()
        # text = re.sub(r'[\t]{2,}', ' ', text)
        letterNum = re.findall(r'([a-z|A-Z]{1})', text)
        isSentence = re.findall(r'([a-z|A-Z]+)', text)
        isChinese = re.findall(r'[\u2E80-\u9FFF\|\uAC00-\uD7A3]+', text)
        #
        spaceNum = re.findall(r'[\xa0| |…]{5,}', text)
        pointNum = re.findall(r'[.|?|,]', text)
        #
        datatimeNum1 = re.findall(r'DD-MMM-YY', text)
        datatimeNum2 = re.findall(r'XXXXXXXX', text)
        if len(letterNum) == 0:
            text = ''
        elif len(isChinese) > 0:
            text = ''
        elif text[-4:] == '....':
            text = ''
        elif len(text) < 6:
            text = ''
        elif (len(datatimeNum1) > 0) and (len(datatimeNum2) > 0):
            text = ''
        elif len(isSentence) < 3:
            text = ''
        elif len(letterNum) < 10:
            text = ''
        elif len(set(letterNum)) < 6:
            text = ''
        elif len(letterNum)/len(text) <= 0.5:
            text = ''
        if len(text) < 20:
            str_list = text.split(' ')
            if len(str_list) < 3:
                text = ''
        if len(text) < 24:
            if (text[-1:] == ':') or (text[-1:] == '†') or (text[-1:] == ')'):
                text = ''
        if len(spaceNum) > 0:
            if len(pointNum) == 0:
                text = ''
        return text


    def fr_sentence_filter(self, text_lis):
        text = ''.join(text_lis)
        if (text.strip() == '') or text is None:
            return ''
        # ---
        """
        html_word_dict = {
            "&nbsp;": " ", "&#160;": " ", "&lt;": "<", "&#60;": "<", "&gt;": ">", "&#62;": ">", "&amp;": "&",
            "&#38;": "&",
            "&quot;": "\"", "&#34;": "\"", "&apos;": "\'", "&#39;": "\'", "&cent;": "￠", "&#162;": "￠",
            "&pound;": "£", "&#163;": "£", "&yen;": "¥", "&#165": "¥", "&euro;": "€", "&#8364;": "€",
            "&sect;": "§", "&#167;": "§", "&copy;": "©", "&#169;": "©", "&reg;": "®", "&#174;": "®",
            "&trade;": "™", "&#8482;": "™", "&times;": "×", "&#215;": "×", "&divide;": "÷", "&#247;": "÷",
        }
        for key in html_word_dict.keys():
            text = text.replace(key, html_word_dict[key])
        """
        text = html.unescape(text)
        # ---
        text = text.strip().replace('\n', '').replace('\r', '').replace('\t', ' ').replace('\xa0', ' ').strip()
        fr_world = '[àɑéəɛʒʃʁè]'
        # letterNum = re.findall(r'([a-z|A-Z]{1})', text)
        if len(text) < 6:
            return ''
        if len(text) < 20:
            symbol = re.search('[\(\)|…]+', text)
            if not symbol is None:
                return ''
            if text[0:2] == 'to':
                return ''
        return text


    def ru_sentence_filter(self, text_lis):
        text = ''.join(text_lis)
        if (text.strip() == '') or text is None:
            return ''
        text = html.unescape(text)
        text = text.strip().replace('\n', '').replace('\r', '').replace('\t', ' ').replace('\xa0', ' ').strip()
        if len(text) < 6:
            return ''
        if len(text.split(' ')) < 3:
            return ''
        return text


    def zh_sentence_filter(self, text_lis):
        if isinstance(text_lis, list):
            text_lis = [i.strip() for i in text_lis]
        text = ''.join(text_lis)
        text = html.unescape(text)
        text = text.strip().replace('\n', '').replace('\r', '').replace('\t', ' ').replace('\xa0', ' ').strip()
        zhChar = re.findall(r'[\u2E80-\u9FFF\|\uAC00-\uD7A3]{1}', text)
        tableNum = re.findall(r'│', text)
        if len(zhChar) == 0:
            text = ''
        elif len(tableNum) > 0:
            text = ''
        elif len(zhChar) < 5:
            text = ''
        if len(text) < 14:
            colon_num = re.findall('：', text)
            if len(colon_num) == 1:
                punct_num = re.findall('[\（\）\《\》\——\；\，\。\“\”\<\>\！]+', text)
                if len(punct_num) == 0:
                    return ''
        if len(text) > 40:
            if (len(zhChar)/len(text)) <= 0.4:
                text = ''
        return text


    def _words_filter(self, text_lis):
        text = ''.join(text_lis)
        text = text.strip().replace('\n', '').replace('\r', '')
        return text


    def get_filter_func_by_language(self, language):
        if language == 'zh':
            filter_func = self.zh_sentence_filter
        elif (language == 'en') or (language == 'ms') or (language == 'id'):
            filter_func = self.en_sentence_filter
        elif language == 'fr':
            filter_func = self.fr_sentence_filter
        elif language == 'ru':
            filter_func = self.ru_sentence_filter
        else:
            # print('Warning: googleTrans_inputText.py get_filter_func_by_language() 没有该语言的过滤方法, language=%s' % language)
            filter_func = self.general_sentence_filter
            return filter_func, 0

        return filter_func, 1


    def rewrite(self, inpath, outpath, lang):
        with open(inpath, 'r', encoding='utf-8')as fr, open(outpath, 'a', encoding='utf-8')as fw:
            filter_func, f_status = self.get_filter_func_by_language(lang)
            if f_status == 1:
                for line in fr:
                    data = filter_func(line)
                    if data:
                        fw.write(str(data) + '\n')
                        fw.flush()
            else:
                print('Warning: googleTrans_inputText.py  rewrite() 没有该语言的过滤方法, language=%s'%lang)


    def run(self):
        pass

