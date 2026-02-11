import tkinter
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=800, height=600)
canvas.pack()
window.mainloop()

    # def load(self, url):
    #     body = url.request()
    #     text = lex(body)
    #     self.display_list = layout(text)
    #     self.draw()
        
        # cursor_x, cursor_y = HSTEP, VSTEP
        # for c in text:
        #     self.canvas.create_text(cursor_x, cursor_y, text=c)
        #     cursor_x +=HSTEP

        #     if cursor_x >= WIDTH - HSTEP:
        #         cursor_y += VSTEP
        #         cursor_x = HSTEP