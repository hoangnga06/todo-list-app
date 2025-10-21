#Danh một công việc mới vào danh sách"
tasks = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách"""
    task.append(task.name)
    print(f"Đã thêm công việc:'{task_name}'")
def list_tasks():
    """Liệt kê tất cả công việc hiện có."""
    if not tasks:
        print("Chưa có công việc nào.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
# --- Điểm bắt đầu của chương trình ---
if__name__=="__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và Github")
    add_task("Làm bài tập thực hành ở nhà")
    list_tasks()