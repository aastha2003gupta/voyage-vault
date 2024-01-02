import streamlit as st

def add_task(new_task):
    if new_task:
        st.session_state.task_list.append(new_task)

def remove_completed_tasks(completed_tasks):
    for task in completed_tasks:
        st.session_state.task_list.remove(task)

def display_tasks():
    for i, task in enumerate(st.session_state.task_list):
        st.write(f"{i + 1}. {task}")

if "task_list" not in st.session_state:
    st.session_state.task_list = []

st.title('Vacation To-Do List')

new_task = st.text_input("Enter your task", "")

if st.button("Add Task"):
    add_task(new_task)

st.write("### Current Tasks:")
display_tasks()

completed_tasks = []
for i, task in enumerate(st.session_state.task_list):
    if st.checkbox(f"Complete: {task}"):
        completed_tasks.append(task)

if st.button("Remove Completed Tasks"):
    remove_completed_tasks(completed_tasks)

st.session_state.task_list = list(set(st.session_state.task_list))
