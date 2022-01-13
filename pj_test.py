import cairo

ps = cairo.SVGSurface("svgfile.svg", 390, 60)
cr = cairo.Context(ps)

cr.set_source_rgb(0, 0, 0)
cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL,
                    cairo.FONT_WEIGHT_NORMAL)
cr.set_font_size(40)

cr.move_to(10, 50)
cr.show_text('What is this..?')
cr.show_page()
