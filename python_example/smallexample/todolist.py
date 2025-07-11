# todo_list.py
def main():
    tasks = []
    
    while True:
        print("\n待办事项列表:")
        print("1. 添加任务")
        print("2. 查看任务")
        print("3. 标记任务完成")
        print("4. 删除任务")
        print("5. 退出")
        
        choice = input("请选择操作 (1-5): ")
        
        if choice == "1":
            task = input("请输入任务内容: ")
            tasks.append({"task": task, "done": False})
            print(f"已添加任务: {task}")
            
        elif choice == "2":
            if not tasks:
                print("当前没有任务")
            else:
                for i, task in enumerate(tasks, 1):
                    status = "✓" if task["done"] else " "
                    print(f"{i}. [{status}] {task['task']}")
                    
        elif choice == "3":
            if not tasks:
                print("当前没有任务")
                continue
                
            try:
                task_num = int(input("请输入要标记的任务编号: ")) - 1
                if 0 <= task_num < len(tasks):
                    tasks[task_num]["done"] = True
                    print(f"已标记任务 '{tasks[task_num]['task']}' 为完成")
                else:
                    print("无效的任务编号")
            except ValueError:
                print("请输入有效的数字")
                
        elif choice == "4":
            if not tasks:
                print("当前没有任务")
                continue
                
            try:
                task_num = int(input("请输入要删除的任务编号: ")) - 1
                if 0 <= task_num < len(tasks):
                    removed = tasks.pop(task_num)
                    print(f"已删除任务: '{removed['task']}'")
                else:
                    print("无效的任务编号")
            except ValueError:
                print("请输入有效的数字")
                
        elif choice == "5":
            print("再见!")
            break
            
        else:
            print("无效的选择，请重新输入")

if __name__ == "__main__":
    main()