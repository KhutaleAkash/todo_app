#!/usr/bin/env python3
"""
Simple To-Do Application (CLI)
Features: add, view, edit, delete, save & load (tasks.json)
"""

import json
import os

DATA_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(tasks, text):
    text = text.strip()
    if not text:
        print("Cannot add an empty task.")
        return
    tasks.append({"task": text})
    save_tasks(tasks)
    print(f"Task '{text}' added successfully.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour To Do List:")
    for i, item in enumerate(tasks, start=1):
        print(f"{i}. {item['task']}")
    print()  # blank line


def edit_task(tasks, index, new_text):
    if index < 1 or index > len(tasks):
        print("Invalid task number.")
        return
    new_text = new_text.strip()
    if not new_text:
        print("Task text cannot be empty.")
        return
    old = tasks[index - 1]["task"]
    tasks[index - 1]["task"] = new_text
    save_tasks(tasks)
    print(f"Task '{old}' updated to '{new_text}'.")


def delete_task(tasks, index):
    if index < 1 or index > len(tasks):
        print("Invalid task number.")
        return
    removed = tasks.pop(index - 1)
    save_tasks(tasks)
    print(f"Task '{removed['task']}' deleted.")


def prompt_menu():
    print("Choose an option:")
    print("  1. Add task")
    print("  2. View tasks")
    print("  3. Edit task")
    print("  4. Delete task")
    print("  5. Exit")


def main():
    tasks = load_tasks()
    print("Simple To-Do App (tasks saved to tasks.json)\n")

    while True:
        prompt_menu()
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            text = input("Enter task description: ")
            add_task(tasks, text)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            if not tasks:
                print("No tasks to edit.")
                continue
            view_tasks(tasks)
            try:
                idx = int(input("Enter task number to edit: ").strip())
            except ValueError:
                print("Please enter a valid number.")
                continue
            new_text = input("Enter new task description: ")
            edit_task(tasks, idx, new_text)

        elif choice == "4":
            if not tasks:
                print("No tasks to delete.")
                continue
            view_tasks(tasks)
            try:
                idx = int(input("Enter task number to delete: ").strip())
            except ValueError:
                print("Please enter a valid number.")
                continue
            confirm = input(f"Are you sure you want to delete task {idx}? (y/N): ").strip().lower()
            if confirm == "y":
                delete_task(tasks, idx)
            else:
                print("Delete cancelled.")

        elif choice == "5":
            print("Bye!")
            break

        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()
