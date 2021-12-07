# view-align
## Usage
1. Make a file including sentence pairs and word-to-word alignments. See `test-input.txt` for an example.
2. Input the file to `view-align.py` and save the output to an HTML file. E.g.,
```sh
$ python view-align.py < test-input.txt > a.html
```
3. Put the HTML file and `show-align.js` in the same directory. Open the HTML file in a WEB browser.


## 使い方
添付の test-input.txt のフォーマットで訳文・原文・アラインメントを入力するとHTMLが出ます．
show-align.js と同じディレクトリにHTMLを置いてブラウザで開くとアラインメントが見られます．

入力フォーマットは view-align.py の先頭にも書いてあります．

例：
$ python view-align.py < test-input.txt > a.html
