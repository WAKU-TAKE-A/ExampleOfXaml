# -*- coding: utf-8 -*-

"""
Data Binding Example.

* Run this file.
"""

import wpf
from System.Windows import Application, Window

class Example_xaml_main(Window):

    def __init__(self):
        wpf.LoadComponent(self, 'example_xaml_view.xaml')
        print('Init window.')
    
    def button1_Click(self, sender, e):
        ans = float(self.textBox1.Text) + float(self.textBox2.Text)
        self.textBox3.Text = str(ans)

if __name__ == '__main__':
    Application().Run(Example_xaml_main())
