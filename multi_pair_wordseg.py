import argparse
import os
import time
from collections import Counter
import logging
from multiprocessing import Process, Queue
import datetime
import random
import PywordSeg.bin.pywordseg as WordSeg


class ProcessClass:
    def __init__(self, infile, src_lang, tgt_lang, p_num=10):
        print("Initializing ...... " + '\n')
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang
        self.infile = infile
        self.p_num = p_num

        WordSeg.WordSeg(self.src_lang)
        WordSeg.WordSeg(self.tgt_lang)

    def safe_readline(self, f):
        pos = f.tell()  # tell() 方法返回文件的当前位置，即文件指针当前位置
        while True:
            try:
                return f.readline()
            except UnicodeDecodeError:
                pos -= 1
                f.seek(pos)  # search where this character begins

    # 定位
    def find_offsets(self):
        with open(self.infile, 'r', encoding='utf-8') as f:
            # 文件大小
            size = os.fstat(f.fileno()).st_size
            # print('size=%s'%size)
            chunk_size = size // self.p_num
            # print('chunk_size=%s'%chunk_size)
            offsets = [0 for _ in range(self.p_num + 1)]

            for i in range(1, self.p_num + 1):
                f.seek(chunk_size * i)  # seek() 方法用于移动文件读取指针到指定位置
                self.safe_readline(f)
                # offsets = [0,1231,234232423,]
                offsets[i] = f.tell()  # tell() 方法返回文件的当前位置，即文件指针当前位置
            return offsets

    # 分词并保存结果到文件
    def token_and_save(self, offset=0, end=-1):
        with open(self.infile, 'r', encoding='utf-8') as f, open(self.infile + '.f', 'a', encoding='utf-8') as file:
            f.seek(offset)
            line = f.readline()
            # print(line)
            # time.sleep(111)
            while line:
                if end > 0 and f.tell() > end:
                    print('111' * 20)
                    break
                #res_src = WordSeg.token(line.split('\t')[0], self.src_lang)
                #res_tgt = WordSeg.token(line.split('\t')[1], self.tgt_lang)
                res_src = line.split('\t')[0]
                res_tgt = line.split('\t')[1]
                file.write(res_src + '\t' + res_tgt + '\n')
                file.flush()
                line = f.readline()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', '-i', type=str, required=True, help='Input file')
    parser.add_argument('--src_lang', '-sl', type=str, required=True, help="src language.")
    parser.add_argument('--tgt_lang', '-tl', type=str, required=True, help="tgt language.")
    parser.add_argument('--p_num', '-p', type=int, metavar='int', required=False, default=10,
                        help="the number of process")
    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    # 接收参数
    infile = args.infile
    src_lang = args.src_lang
    tgt_lang = args.tgt_lang
    p_num = args.p_num


    PC = ProcessClass(infile, src_lang, tgt_lang, p_num)
    offsets = PC.find_offsets()
    print(offsets)
    # time.sleep(111)
    start = time.time()
    
    j = 0
    proc_record = []
    for _ in range(p_num):
        # if j > len(offsets):
        #    break
        p = Process(target=PC.token_and_save, args=(offsets[j], offsets[j + 1]))
        p.start()
        #p.join()
        proc_record.append(p)
        j += 1

    for p in proc_record:
        p.join()

    end = time.time()
    print("Task runs %0.2f seconds." % (end - start))
