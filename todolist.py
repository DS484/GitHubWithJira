import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        self.root.geometry("400x400")
        
        # List hiển thị các công việc
        self.todo_listbox = tk.Listbox(root, width=50, height=15)
        self.todo_listbox.pack(pady=10)
        
        # Nhập công việc mới
        self.entry_task = tk.Entry(root, width=50)
        self.entry_task.pack(pady=5)
        
        # Frame chứa các nút thao tác
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)
        
        # Nút thêm công việc
        btn_add = tk.Button(btn_frame, text="Thêm", width=10, command=self.add_task)
        btn_add.grid(row=0, column=0, padx=5)
        
        # Nút sửa công việc
        btn_edit = tk.Button(btn_frame, text="Sửa", width=10, command=self.edit_task)
        btn_edit.grid(row=0, column=1, padx=5)
        
        # Nút xoá công việc
        btn_delete = tk.Button(btn_frame, text="Xoá", width=10, command=self.delete_task)
        btn_delete.grid(row=0, column=2, padx=5)
    
    def add_task(self):
        task = self.entry_task.get().strip()
        if task:
            self.todo_listbox.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập công việc cần thêm!")
    
    def edit_task(self):
        try:
            index = self.todo_listbox.curselection()[0]
            current_task = self.todo_listbox.get(index)
            new_task = simpledialog.askstring("Sửa công việc", "Chỉnh sửa công việc:", initialvalue=current_task)
            if new_task and new_task.strip():
                self.todo_listbox.delete(index)
                self.todo_listbox.insert(index, new_task.strip())
            else:
                messagebox.showwarning("Cảnh báo", "Công việc không được để trống!")
        except IndexError:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn công việc cần sửa!")
    
    def delete_task(self):
        try:
            index = self.todo_listbox.curselection()[0]
            self.todo_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn công việc cần xoá!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
