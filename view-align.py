#!/usr/bin/env python

"""
入力フォーマット
対訳文のペアひとつが以下のかたまりに対応．空行区切りでいくつでも書ける．
----------------
日本語文（単語を空白区切り）
中国語文（単語を空白区切り）
x1 y1 # 日本語の x1 番目の単語と中国語の y1 番目の単語が対応
x2 y2 # 日本語の x2 番目の単語と中国語の y2 番目の単語が対応
...
xn yn # 日本語の xn 番目の単語と中国語の yn 番目の単語が対応
<空行>
"""

import sys

def read_input(f):
    while True:
        js = f.readline()
        if js == "":
            return # EOF
        js = js.rstrip().split()

        cs = f.readline().rstrip().split()

        aligns = []
        for line in f:
            if line.rstrip() == "":
                break
            x, y = line.rstrip().split()
            aligns.append([int(x), int(y)])
    
        yield (js, cs, aligns)

def render(ix, js, cs, aligns):
    # これを変えるとアラインメント線部分の幅が変わる
    height = 140

    # width は後で自動的に調整される
    svg = '<svg id="p{}" width="800" height="{}">\n'.format(ix, height)

    jids = []
    for i, w in enumerate(js):
        word_id = "j{}.{}".format(ix, i)
        svg += '  <text id="{}" x="0" y="20">{}</text>\n'.format(word_id, w)
        jids.append(word_id)

    cids = []
    for i, w in enumerate(cs):
        word_id = "c{}.{}".format(ix, i)
        svg += '  <text id="{}" x="0" y="{}">{}</text>\n'.format(word_id, height - 10, w)
        cids.append(word_id)

    svg += "</svg>"

    code = 'show_align("p{}", {}, {}, {});'.format(ix, repr(jids), repr(cids), repr(aligns));

    return code, svg

#----- main
codes = []
svgs = []
for i, (js, cs, aligns) in enumerate(read_input(sys.stdin)):
    code, svg = render(i, js, cs, aligns)
    codes.append(code)
    svgs.append(svg)

print("<!DOCTYPE html>")
print('<html lang="en">')
print('<head>')
print('<meta charset="utf-8"/>')
print('<script type="text/javascript" src="show-align.js"></script>')
print('<script type="text/javascript">')
print("window.onload = function() {")
print("\n".join(codes))
print("}")
print('</script>')
print("</head>")
print("<body>")
print("\n<br/>\n".join(svgs))
print("</body>")
print("</html>")
