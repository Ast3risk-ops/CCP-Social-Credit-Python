from guizero import App, Text, ButtonGroup, PushButton
from sys import exit


def e(message):
    app.destroy()
    exit([message])


def q2_start():
    app.info("", "SENDING ANSWER...")
    app.info("", "ANSWER SUBMITTED")
    if q1_choice == 1:
        app.info("正确！", "Correct!")
    else:
        app.warn("错！", "Wrong!")
        app.error("", "ERR_WRONG_ANSWER")
        e("ERR_WRONG_ANSWER")


app = App(title="社會信用測試", bg="red", layout="auto")

app.set_full_screen("}")
app.info("社會信用測試開始", "Welcome to the Social Credit Test!")
app.warn("警告！", "You will not be able to use your pc until you finish the test!")
q1 = Text(app, text="Question 1", color="yellow")
q1_text = Text(app, text="How many children do you have?")
q1_choice = ButtonGroup(app, options=[["1", "1"], ["2", "2"], ["More than 2", "3"], ["", "ee"]], selected="ee")
q1_button = PushButton(app, command=q2_start, text="Submit")
app.display()
