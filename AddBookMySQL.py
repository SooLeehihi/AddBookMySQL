import tkinter as tk
from tkinter import ttk
import mysql.connector
import pymysql

def get_contacts():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="Kyo",
            password="1234",
            database="addbook",
            cursor=pymysql.cursor.DictCursor
        )
        cursor = connection.cursor()
        cursor.execute('SELECT name, phone FROM git aaddbook')
        contacts = cursor.fetchall()
        connection.close()
        return contacts
    except mysql.connector.Error as error:
        print("MySQL 오류 발생:", error)
        return []

def add_contact(name, phone):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="Kyo",
            password="1234",
            database="addbook",
            cursor=pymysql.cursor.DictCursor
        )
        cursor = connection.cursor()
        cursor.execute('INSERT INTO addbook (name, phone) VALUES (%s, %s)', (name, phone))
        connection.commit()
        connection.close()
        print("연락처 추가됨")
    except mysql.connector.Error as error:
        print("MySQL 오류 발생:", error)

def delete_contact(name):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="Kyo",
            password="1234",
            database="addbook",
            cursor=pymysql.cursor.DictCursor
        )
        cursor = connection.cursor()
        cursor.execute('DELETE FROM addbook WHERE name = %s', (name,))
        connection.commit()
        connection.close()
        print("연락처 삭제됨")
    except mysql.connector.Error as error:
        print("MySQL 오류 발생:", error)
        
def update_contact(name, phone):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="Kyo",
            password="1234",
            database="addbook",
            cursor=pymysql.cursor.DictCursor
        )
        cursor = connection.cursor()
        cursor.execute('UPDATE addbook SET phone = %s WHERE name = %s', (phone, name))
        connection.commit()
        connection.close()
        print("연락처 수정됨")
    except mysql.connector.Error as error:
        print("MySQL 오류 발생:", error)


def show_contacts():
    contacts = get_contacts()

    root = tk.Tk()
    root.title("전화번호부")

    tree = ttk.Treeview(root, columns=('이름', '전화번호'))
    tree.heading('#0', text='ID')
    tree.heading('#1', text='이름')
    tree.heading('#2', text='전화번호')

    for idx, (name, phone) in enumerate(contacts, start=1):
        tree.insert('', 'end', text=idx, values=(name, phone))

    tree.pack(expand=True, fill='both')

    root.mainloop()

def add_contact_gui():
    def add():
        name = name_entry.get()
        phone = phone_entry.get()
        add_contact(name, phone)
        window.destroy()

    window = tk.Toplevel()
    window.title("연락처 추가")

    name_label = tk.Label(window, text="이름:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(window)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    phone_label = tk.Label(window, text="전화번호:")
    phone_label.grid(row=1, column=0, padx=5, pady=5)
    phone_entry = tk.Entry(window)
    phone_entry.grid(row=1, column=1, padx=5, pady=5)

    add_button = tk.Button(window, text="추가", command=add)
    add_button.grid(row=3, columnspan=2, padx=5, pady=5)

def delete_contact_gui():
    def delete():
        name = name_entry.get()
        delete_contact(name)
        window.destroy()

    window = tk.Toplevel()
    window.title("연락처 삭제")

    name_label = tk.Label(window, text="이름:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(window)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    delete_button = tk.Button(window, text="삭제", command=delete)
    delete_button.grid(row=2, columnspan=2, padx=5, pady=5)
    
def update_contact_gui():
    def update():
        name= name_entry.get()
        phone= phone_entry.get()
        update_contact(name,phone)
        window.destroy()
        
    window = tk.Toplevel()
    window.title("연락처 수정")

    name_label = tk.Label(window, text="이름:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(window)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    phone_label = tk.Label(window, text="전화번호:")
    phone_label.grid(row=1, column=0, padx=5, pady=5)
    phone_entry = tk.Entry(window)
    phone_entry.grid(row=1, column=1, padx=5, pady=5)

    update_button = tk.Button(window, text="수정", command=update)
    update_button.grid(row=3, columnspan=2, padx=5, pady=5)
    
def main():
    root = tk.Tk()
    root.title("전화번호부")

    add_button = tk.Button(root, text="연락처 추가", command=add_contact_gui)
    add_button.pack(pady=5)

    delete_button = tk.Button(root, text="연락처 삭제", command=delete_contact_gui)
    delete_button.pack(pady=5)
    
    update_button = tk.Button(root, text="연락처 수정", command=update_contact_gui)
    update_button.pack(pady=5)
    
    show_button = tk.Button(root, text="연락처 출력", command=show_contacts)
    show_button.pack(pady=5)

    exit_button = tk.Button(root, text="종료", command=root.quit)
    exit_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()