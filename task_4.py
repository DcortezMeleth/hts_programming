from xml.dom import minidom
from xml.dom.expatbuilder import TEXT_NODE
import graphics
import Tkinter as tk


class Figure(object):
    def __init__(self, color='white'):
        self.color = color


class Line(Figure):
    def __init__(self, x_start=None, x_end=None, y_start=None, y_end=None, color='white'):
        super(Line, self).__init__(color)
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end


class Arc(Figure):
    def __init__(self, x_center=None, y_center=None, radius=None, arc_start=None, arc_extend=None, color='white'):
        super(Arc, self).__init__(color)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius
        self.arc_start = arc_start
        self.arc_extend = arc_extend

xmldoc = minidom.parse('example.xml')
line_nodes = xmldoc.getElementsByTagName('Line')
arc_nodes = xmldoc.getElementsByTagName('Arc')

lines = []
for line_node in line_nodes:
    line = Line()
    lines.append(line)
    for node in [x for x in line_node.childNodes if x.nodeType != TEXT_NODE]:
        if node.nodeName == 'YEnd':
            line.y_end = node.childNodes[0].nodeValue
        if node.nodeName == 'XEnd':
            line.x_end = node.childNodes[0].nodeValue
        if node.nodeName == 'XStart':
            line.x_start = node.childNodes[0].nodeValue
        if node.nodeName == 'YStart':
            line.y_start = node.childNodes[0].nodeValue
        if node.nodeName == 'Color':
            line.color = node.childNodes[0].nodeValue

arcs = []
for arc_node in arc_nodes:
    arc = Arc()
    arcs.append(arc)
    for node in [x for x in arc_node.childNodes if x.nodeType != TEXT_NODE]:
        if node.nodeName == 'Radius':
            arc.radius = node.childNodes[0].nodeValue
        if node.nodeName == 'ArcExtend':
            arc.arc_extend = node.childNodes[0].nodeValue
        if node.nodeName == 'ArcStart':
            arc.arc_start = node.childNodes[0].nodeValue
        if node.nodeName == 'XCenter':
            arc.x_center = node.childNodes[0].nodeValue
        if node.nodeName == 'YCenter':
            arc.y_center = node.childNodes[0].nodeValue
        if node.nodeName == 'Color':
            arc.color = node.childNodes[0].nodeValue

win = graphics.GraphWin("go_projekt", 1000, 1000)
win.setBackground('black')
for line in lines:
    l = graphics.Line(graphics.Point(float(line.x_end), 1000 - float(line.y_end)),
                      graphics.Point(float(line.x_start), 1000 - float(line.y_start)))
    l.setFill(line.color)
    l.draw(win)

for arc in arcs:
    win.create_arc(float(arc.x_center) - float(arc.radius),
                   1000 - float(arc.y_center) + float(arc.radius),
                   float(arc.x_center) + float(arc.radius),
                   1000 - float(arc.y_center) - float(arc.radius),
                   start=arc.arc_start, extent=arc.arc_extend, style=tk.ARC, outline=arc.color)
    win.flush()

win.getMouse()
win.close()