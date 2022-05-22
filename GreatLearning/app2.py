import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.cols= 2
        
        self.add_widget(Label(text= "Student Name:"))
        self.s_name= TextInput(multiline= False)
        self.add_widget(self.s_name)

        self.add_widget(Label(text= "Student Marks:"))
        self.s_marks= TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text= "Student Gender:"))
        self.s_gender= TextInput(multiline=False)
        self.add_widget(self.s_gender)

        self.b= Button(text= "Submit")
        # self.b.bind(on_press=self.submit())
        self.b.bind(
            on_press=self.submit
        )
        self.add_widget(self.b)
    
    def submit(self, instance):
        print("The name of the student is "+ self.s_name.text)
        print("The gender of the student is "+ self.s_gender.text)
        print("The marks of the student is "+ self.s_marks.text)
        
class MainApp(App):
    def build(self):
        return Grid()

if __name__=='__main__':
    MainApp().run()
