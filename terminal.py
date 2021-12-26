import sys
import os
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class Terminal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/terminal.ui', self)
        # пароль из файла берём
        self.password = open('password_for_admin').readlines()[0].rstrip()
        # реагирование на кнопку
        self.pushButton.clicked.connect(self.run_command)

    def run_command(self):
        try:
            f = open("IP'S").readlines()
            command = self.lineEdit.text()
            for el in f:
                ip = el.split(' - ')[1].rstrip()
                s = f"sshpass -p '{self.password}' ssh {ip} {command}"
                os.system(f'gnome-terminal -x sh -c "{s}"')
            self.lineEdit.setText('')
            QMessageBox.information(self, 'Успех', f"Успешно проведена команда {command}",
                                       QMessageBox.Cancel,
                                       QMessageBox.Cancel)
        except BaseException as e:
            QMessageBox.warning(self, 'Ошибка', f"Ошибка {e}",
                                    QMessageBox.Cancel,
                                    QMessageBox.Cancel)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Terminal()
    ex.show()
    app.exec_()