// tb = "top"    -> 単語の上端の中点位置を返す
// tb = "bottom" -> 単語の下端の中点位置を返す
function spacing(svg, words, tb) {
    var sep_len = 10; // 単語と単語の間隔
    var init_x = 50;  // 左端の単語の開始位置
    var x = init_x;
    var midpoints = [];
    var last_w;
    for (i in words) {
        w = document.getElementById(words[i]);
        w.setAttribute("x", x);
        bbox = w.getBBox();
        x += sep_len + bbox.width;
        mid_x = bbox.x + bbox.width / 2;
        // NOTE: text 要素の座標は左下．BBox の座標は右上．
        mid_y = (tb == "top") ? bbox.y : bbox.y + bbox.height;
        midpoints.push([mid_x, mid_y]);
        last_w = w;
    }
    width = svg.getAttribute("width");
    last_bb = last_w.getBBox();
    if (width < last_bb.x + last_bb.width) {
        svg.setAttribute("width", last_bb.x + last_bb.width);
    }
    return midpoints;
}

function draw_edges(svg, jpoints, cpoints, edges) {
    var colors = ["red", "green", "orange", "blue", "magenta", "black"];
    for (var i in edges) {
        var ji = edges[i][0];
        var ci = edges[i][1];
        line = document.createElementNS("http://www.w3.org/2000/svg", "line")
        line.setAttribute("x1", jpoints[ji][0]);
        line.setAttribute("y1", jpoints[ji][1]);
        line.setAttribute("x2", cpoints[ci][0]);
        line.setAttribute("y2", cpoints[ci][1]);
        // ひとつの日本語の単語から出るエッジは全て同じ色
        line.setAttribute("stroke", colors[ji % colors.length]);
        svg.appendChild(line);
    }
}

function show_align(svg_id, jwords, cwords, edges) {
    svg = document.getElementById(svg_id);
    jpoints = spacing(svg, jwords, "bottom");
    cpoints = spacing(svg, cwords, "top");
    draw_edges(svg, jpoints, cpoints, edges);
}
