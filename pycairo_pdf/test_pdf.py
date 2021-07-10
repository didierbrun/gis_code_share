import cairo

with cairo.PDFSurface("test.pdf", 100, 100) as surface:
    context = cairo.Context(surface)
    context.set_line_width(0.1)
    for i in range (10, 95, 5):
        context.move_to(10, i)
        context.line_to(i, 90)
        context.move_to(i, 10)
        context.line_to(90,i)
    context.stroke()