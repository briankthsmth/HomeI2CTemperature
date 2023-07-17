import qwiic_micro_oled

class Display:

    def __init__(self):
        oled_display = qwiic_micro_oled.QwiicMicroOled()
        oled_display.begin()
        oled_display.clear(oled_display.PAGE)
        
    def display_temperature(self, temperature):
        oled_display.print(temperature)
        oled_display.display()