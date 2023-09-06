import qwiic_micro_oled
import pyqrcode

class Display:

    def __init__(self):
        self.oled_display = qwiic_micro_oled.QwiicMicroOled()
        self.oled_display.begin()
        self.oled_display.clear(self.oled_display.PAGE)
        
    def display_temperature(self, temperature):
        temperature = 9.0 * temperature / 5.0 + 32.0
        self.oled_display.clear(self.oled_display.PAGE)
        self.oled_display.set_font_type(2)
        self.oled_display.set_cursor(10,0)
        self.oled_display.print(f'{temperature:.1f}')
        self.oled_display.display()

    def draw_qrcode(self, uri, pincode):
        self.oled_display.clear(self.oled_display.PAGE)
        text_rep = pyqrcode.create(uri).text()
        row = 0
        column_offset = 14
        column = column_offset
        for c in text_rep:
            if c == '1':
                self.oled_display.pixel(column, row)
                column += 1
            elif c == '0':
                column += 1
            elif c == '\n':
                row += 1
                column = column_offset

        self.oled_display.set_font_type(0)
        self.oled_display.set_cursor(0, 39)
        self.oled_display.print(pincode)
        self.oled_display.display()
            
