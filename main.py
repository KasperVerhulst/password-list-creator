from ui.MainWindow import MainWindow

title = "password list"
size = "600x400"


def main():
    app = MainWindow(title,size)
    app.mainloop()

if __name__ == "__main__":
    main()