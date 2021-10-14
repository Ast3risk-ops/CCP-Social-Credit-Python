from guizero import App, Text, ButtonGroup
from sys import exit
app = App(title="社會信用測試", bg="red", layout="auto")
app.set_full_screen("}")
app.info("社會信用測試開始", "Welcome to the Social Credit Test!")
app.warn("警告！", "You will not be able to use your pc until you fnish the test!")
q1 = Text(app, text="Question 1", color="yellow")
q1_text= Text(app, text="How many children do you have?")
q1_choice = ButtonGroup(app, options=[["1", "1"],  ["2", "2"], ["More than 2", "3"]])
app.display()
