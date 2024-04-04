# to run the script, we should go to the terminal and type: streamlit run (path of the app)
# to start deploying into web:
# 1. create a requirements file with: pip freeze > requirements.txt
import streamlit as sl
import modules.functions as functions

to_dos = functions.get_todos()


def add_to_do():
    to_do_local = sl.session_state["input_box"] + "\n"
    to_dos.append(to_do_local)
    functions.write_todos(to_dos)


sl.title("My To-do App")
sl.subheader("This is my to-do app")
sl.write("This app is made to increase your productivity")


for index, to_do in enumerate(to_dos):
    checkbox = sl.checkbox(to_do, key=to_do)
    if checkbox:
        to_dos.pop(index)
        functions.write_todos(to_dos)
        del sl.session_state[to_do]
        sl.rerun()

sl.text_input(label="Enter a new to-do item: ",
              placeholder="Type here",
              on_change=add_to_do,
              key="input_box")

