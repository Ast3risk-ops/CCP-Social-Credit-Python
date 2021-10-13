from guizero import App, Text, ButtonGroup
from sys import exit
app = App(title="社會信用測試", bg="red", layout="grid")
q1 = Text(app, text="Question 1", color="yellow", grid=[100,5])

app.display()
