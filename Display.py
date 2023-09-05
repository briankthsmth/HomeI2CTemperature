import qwiic_micro_oled

class Display:

    def __init__(self):
        self.oled_display = qwiic_micro_oled.QwiicMicroOled()
        self.oled_display.begin()
        self.oled_display.set_font_type(2)
        self.oled_display.clear(self.oled_display.PAGE)
        
    def display_temperature(self, temperature):
        temperature = 9.0 * temperature / 5.0 + 32.0
        self.oled_display.clear(self.oled_display.PAGE)
        self.oled_display.set_cursor(10,0)
        self.oled_display.print(f'{temperature:.1f}')
        self.oled_display.display()
