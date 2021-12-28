import sys
import os
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/main.ui', self)
        # пароль из файла берём
        self.password = open('password_for_admin').readlines()[0].rstrip()
        # заполняем команды из файла
        for el in open('commands').readlines():
            self.comboBox_3.addItem(el.rstrip())
            self.comboBox_2.addItem(el.rstrip())
        # заполняем ip компов
        for el in open("IP'S").readlines():
            self.comboBox.addItem(el.rstrip())
        # реагирование на кнопки для отдельного пк
        self.pushButton_3.clicked.connect(self.open_terminal)  # открытие терминала
        self.pushButton_4.clicked.connect(self.off_pc)  # выключение пк
        self.pushButton_5.clicked.connect(self.reboot_pc)  # перезагрузка пк
        self.pushButton_6.clicked.connect(self.info_pc)  # информация о пк
        # реагирование на кнопки для всех пк
        self.pushButton.clicked.connect(self.open_terminal_for_all)  # открыть терминал для всех
        self.pushButton_15.clicked.connect(self.of_for_all)  # выключить все пк
        self.pushButton_16.clicked.connect(self.reboot_for_all)  # перезагрузить все пк
        self.comboBox_3.activated[str].connect(self.special_command)  # спец команды для всех пк

    def special_command(self, txtVal):
        try:
            f = open("IP'S").readlines()
            for el in f:
                ip = el.split(' - ')[1].rstrip()
                s = f"sshpass -p '{self.password}' ssh {ip} {txtVal}"
                os.system(f'gnome-terminal -- sh -c "{s}"')
            self.lineEdit.setText('')
            QMessageBox.information(self, 'Успех', f"Успешно применил команду на все пк",
                                    QMessageBox.Cancel,
                                    QMessageBox.Cancel)
        except BaseException as e:
            QMessageBox.warning(self, 'Ошибка', f"Ошибка {e}",
                                QMessageBox.Cancel,
                                QMessageBox.Cancel)

    def reboot_for_all(self):
        try:
            f = open("IP'S").readlines()
            for el in f:
                ip = el.split(' - ')[1].rstrip()
                s = f"sshpass -p '{self.password}' ssh {ip} sudo reboot"
                os.system(f'gnome-terminal -- sh -c "{s}"')
            self.lineEdit.setText('')
            QMessageBox.information(self, 'Успех', f"Успешно перезагрузил все пк",
                                       QMessageBox.Cancel,
                                       QMessageBox.Cancel)
        except BaseException as e:
            QMessageBox.warning(self, 'Ошибка', f"Ошибка {e}",
                                    QMessageBox.Cancel,
                                    QMessageBox.Cancel)

    def of_for_all(self):
        try:
            f = open("IP'S").readlines()
            for el in f:
                ip = el.split(' - ')[1].rstrip()
                s = f"sshpass -p '{self.password}' ssh {ip} sudo shutdown -h now"
                os.system(f'gnome-terminal -- sh -c "{s}"')
            self.lineEdit.setText('')
            QMessageBox.information(self, 'Успех', f"Успешно выключили все пк",
                                       QMessageBox.Cancel,
                                       QMessageBox.Cancel)
        except BaseException as e:
            QMessageBox.warning(self, 'Ошибка', f"Ошибка {e}",
                                    QMessageBox.Cancel,
                                    QMessageBox.Cancel)

    def open_terminal_for_all(self):
        ex.close()
        os.system('python3 terminal.py')
        ex.show()

    def open_terminal(self):
        ip = str(self.comboBox.currentText()).split(' - ')[1]
        s = f"sshpass -p '{self.password}' ssh {ip}"
        os.system(f'gnome-terminal -- sh -c "{s}"')

    def off_pc(self):
        ip = str(self.comboBox.currentText()).split(' - ')[1]
        s = f"sshpass -p '{self.password}' ssh {ip} sudo shutdown -h now"
        os.system(f'gnome-terminal -- sh -c "{s}"')

    def reboot_pc(self):
        ip = str(self.comboBox.currentText()).split(' - ')[1]
        s = f"sshpass -p '{self.password}' ssh {ip} sudo reboot"
        os.system(f'gnome-terminal -- sh -c "{s}"')

    def info_pc(self):
        ip = str(self.comboBox.currentText()).split(' - ')[1]
        s = f"sshpass -p '{self.password}' ssh {ip} cat /proc/cpuinfo"
        os.system(f'gnome-terminal -- sh -c "{s}"')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    app.exec_()
