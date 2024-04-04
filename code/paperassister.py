import tkinter as tk
from tkinter import ttk
import tkinter.font as font

import os
import csv
import sys
import time
import json

class Paper():
    def __init__(self, title="", url="", abstract="", author="", year="", keywords="", memo=""):
        self.title = title
        self.url = url
        self.abstract = abstract
        self.author = author
        self.year = year
        self.keywords = keywords
        self.memo = memo

    def __str__(self):
        return f"TITLE:{self.title},MEMO:{self.memo}"

    def __repr__(self):
        return self.title

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        # ウィンドウタイトル
        self.master.title("Paper Assister")

        #サイズを決定
        self.master.geometry("950x800")
        #サイズを固定
        self.master.resizable(width=False, height=False)

        # フォント
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(size=12)

        ######呪文
        self.master.update_idletasks()
        #########

        # タブを作成
        self.notebook = ttk.Notebook(self.master)
        # 記録タブ
        self.archive_tab = tk.Frame(self.notebook,bd=10,bg="white",width=self.master.winfo_width(),height=self.master.winfo_height())
        self.notebook.add(self.archive_tab,text="論文を記録する")
        # 検索タブ
        self.search_tab = tk.Frame(self.notebook,bd=10,bg="white",width=self.master.winfo_width(),height=self.master.winfo_height())
        self.notebook.add(self.search_tab,text="論文を検索する")
        # タブを配置
        self.notebook.pack(side=tk.TOP,expand=True)


        # 論文情報入力フレーム
        self.archive_frame = tk.Frame(self.archive_tab)

        # タイトルフレーム
        self.title_frame = tk.Frame(self.archive_frame)
        # タイトル入力ラベル
        self.title_label = tk.Label(self.title_frame, text="タイトル")
        self.title_label.pack(side=tk.LEFT, padx=10, pady=5)
        # タイトル入力テキストボックス
        self.title_box = tk.Entry(self.title_frame,bd=5,relief="ridge",width=135)
        self.title_box.pack(side=tk.RIGHT)
        # タイトルフレームを配置
        self.title_frame.pack(side=tk.TOP,expand=True,fill=tk.X)

        # URLフレーム
        self.url_frame = tk.Frame(self.archive_frame)
        # URL入力ラベル
        self.url_label = tk.Label(self.url_frame, text="URL")
        self.url_label.pack(side=tk.LEFT, padx=10, pady=5)
        # URL入力テキストボックス
        self.url_box = tk.Entry(self.url_frame,bd=5,relief="ridge", width=135)
        self.url_box.pack(side=tk.RIGHT)
        # URLフレームを配置
        self.url_frame.pack(side=tk.TOP,expand=True,fill=tk.X)

        # 著者フレーム
        self.author_frame = tk.Frame(self.archive_frame)
        # 著者入力ラベル
        self.author_label = tk.Label(self.author_frame, text="著者")
        self.author_label.pack(side=tk.LEFT, padx=10, pady=5)
        # 著者入力テキストボックス
        self.author_box = tk.Entry(self.author_frame,bd=5,relief="ridge", width=135)
        self.author_box.pack(side=tk.RIGHT)
        # 著者フレームを配置
        self.author_frame.pack(side=tk.TOP,expand=True,fill=tk.X)

        # 年フレーム
        self.year_frame = tk.Frame(self.archive_frame)
        # 年入力ラベル
        self.year_label = tk.Label(self.year_frame, text="年")
        self.year_label.pack(side=tk.LEFT, padx=10, pady=5)
        # 年入力テキストボックス
        self.year_box = tk.Entry(self.year_frame,bd=5,relief="ridge", width=135)
        self.year_box.pack(side=tk.RIGHT)
        # 年フレームを配置
        self.year_frame.pack(side=tk.TOP,expand=True,fill=tk.X)

        # キーワードフレーム
        self.keywords_frame = tk.Frame(self.archive_frame)
        # キーワード入力ラベル
        self.keywords_label = tk.Label(self.keywords_frame, text="キーワード")
        self.keywords_label.pack(side=tk.LEFT, padx=10, pady=5)
        # キーワード入力テキストボックス
        self.keywords_box = tk.Entry(self.keywords_frame,bd=5,relief="ridge", width=135)
        self.keywords_box.pack(side=tk.RIGHT)
        # キーワードフレームを配置
        self.keywords_frame.pack(side=tk.TOP,expand=True,fill=tk.X)

        # 要約フレーム
        self.abstract_frame = tk.Frame(self.archive_frame)
        # 要約入力ラベル
        self.abstract_label = tk.Label(self.abstract_frame, text="要約")
        self.abstract_label.pack(side=tk.TOP)
        # 要約入力テキストボックス
        self.abstract_box = tk.Text(self.abstract_frame,bd=5,relief="ridge",height=16)
        self.abstract_box.pack(side=tk.TOP,expand=True,fill=tk.X)
        # 要約フレームを配置
        self.abstract_frame.pack(side=tk.TOP,expand=True,fill=tk.X)

        # メモフレーム
        self.memo_frame = tk.Frame(self.archive_frame)
        # メモ入力ラベル
        self.memo_label = tk.Label(self.memo_frame, text="メモ")
        self.memo_label.pack(side=tk.TOP)
        # メモ入力テキストボックス
        self.memo_box = tk.Text(self.memo_frame,bd=5,relief="ridge",height=18)
        self.memo_box.pack(side=tk.TOP,expand=True,fill=tk.X)
        # メモフレームを配置
        self.memo_frame.pack(side=tk.TOP,expand=True,fill=tk.X)

        # ボタンフレーム
        self.button_frame = tk.Frame(self.archive_frame)
        # 整形ボタン
        self.format_button = tk.Button(self.button_frame, text="整形", width=30,command=self.format_paper)
        self.format_button.pack(side=tk.LEFT, padx=10,pady=5)
        # 保存ボタン
        self.save_button = tk.Button(self.button_frame, text="保存", width=30,command=self.save_paper)
        self.save_button.pack(side=tk.RIGHT, padx=10,pady=5)
        # ボタンフレームを配置
        self.button_frame.pack(side=tk.TOP,expand=True,anchor=tk.CENTER)

        # 論文情報入力フレームを配置
        self.archive_frame.pack(side=tk.TOP,fill=tk.BOTH)

    def format_paper(self):
        # 著者
        author = self.author_box.get()
        if author != "":
            self.author_box.delete(0.0,tk.END)
            self.author_box.insert(0.0,author)
            self.author_box.update()
        # タイトル
        title = self.title_box.get()
        if title != "":
            self.title_box.delete(0.0,tk.END)
            self.title_box.insert(0.0,title)
            self.title_box.update()
        # URL
        url = self.url_box.get()
        if url != "":
            self.url_box.delete(0.0,tk.END)
            self.url_box.insert(0.0,url)
            self.url_box.update()
        # 年
        year = self.year_box.get()
        if year != "":
            self.year_box.delete(0.0,tk.END)
            self.year_box.insert(0.0,year)
            self.year_box.update()
        # キーワード
        keywords = self.keywords_box.get()
        if keywords != "":
            self.keywords_box.delete(0.0,tk.END)
            self.keywords_box.insert(0.0,keywords)
            self.keywords_box.update()
        # 要約
        # 改行削除、タブ削除、ピリオドで改行
        abstract = self.abstract_box.get(0.0,tk.END).replace("\n","").replace("\t","").replace(". ",".\n")
        if abstract != "":
            self.abstract_box.delete(0.0,tk.END)
            self.abstract_box.insert(0.0,abstract)
            self.abstract_box.update()
        # メモ
        memo = self.memo_box.get(0.0,tk.END)
        if memo != "":
            self.memo_box.delete(0.0,tk.END)
            self.memo_box.insert(0.0,memo)
            self.memo_box.update()

        paper = Paper(title,url,abstract,author,year,keywords,memo)
        return paper

    # 記録済みの論文を読み込む
    def load_papers(self):
        papers = []

        # ディレクトリ内の全てのjsonを読み込む
        for file in os.listdir("./saved_papers"):
            if file.endswith(".json"):
                with open("./saved_papers/"+file, "r", encoding="utf-8") as f:
                    # jsonとして読み込む
                    paper = json.load(f)
                    # Paperクラスに変換
                    papers.append(Paper(paper["title"],paper["url"],paper["abstract"],paper["author"],paper["year"],paper["keywords"],paper["memo"]))

        return papers

    # 論文を保存する
    def save_paper(self):
        # 論文情報を整形
        paper = self.format_paper()
        # ファイル名
        file_name = "./saved_papers/"+paper.title+".json"
        # Paperクラスを辞書に変換
        paper_dict = {"title":paper.title,"url":paper.url,"abstract":paper.abstract,"author":paper.author,"year":paper.year,"keywords":paper.keywords,"memo":paper.memo}
        # jsonとして保存
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(paper_dict, f, ensure_ascii=False)


def main():
    root = tk.Tk()
    app = Application(root)
    app.mainloop()

if __name__ == "__main__":
    main()