from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp # Display Pixels



class MainApp(MDApp):
    def build(self):
        # Define Screen
        screen = Screen()
        # Define Table
        table = MDDataTable(
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
            size_hint = (0.95, 0.6),
            column_data = [
                ("Part Name", dp(22)),
                ("Parent Equipment", dp(20)),
                ("Quantity", dp(15)),
                ("Location", dp(20)),
                ("Model/Serial Number", dp(25)),
                ("Manufacturer", dp(22)),
                ("Notes", dp(30)),
            ],
            row_data = [
                ("Boiler","Boiler #1", "30", "Locker 1", "SN 234234", "Cleaver Brooks", "N/A"),
                ("Boiler","Boiler #2", "34", "Locker 2", "SN 223244", "Cleaver Brooks", "N/A"),
            ]
        )
        
        
        
        
        
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        # return Builder.load_file("table2.kv")
        screen.add_widget(table)
        return screen
    








MainApp().run()
        