import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox


class CowDatabaseUI(QWidget):

    def __init__(self):
        super().__init__()

        # ������������� ������
        self.id_label = QLabel("�������������:")
        self.id_edit = QLineEdit()

        # ��� ������
        self.name_label = QLabel("���:")
        self.name_edit = QLineEdit()

        # ������� ������
        self.age_label = QLabel("�������:")
        self.age_edit = QLineEdit()

        # ���� ������
        self.color_label = QLabel("����:")
        self.color_edit = QLineEdit()

        # ���� ������
        self.height_label = QLabel("����:")
        self.height_edit = QLineEdit()

        # ��� ������
        self.weight_label = QLabel("���:")
        self.weight_edit = QLineEdit()

        # �������� ������
        self.vitamins_label = QLabel("��������:")
        self.vitamins_edit = QLineEdit()

        # ������������� ������
        self.minerals_label = QLabel("�������������:")
        self.minerals_edit = QLineEdit()

        # ������ ���������� ������
        self.add_button = QPushButton("��������")
        self.add_button.clicked.connect(self.add_cow)

        # ������������ ��������� �� ������
        self.id_label.move(20, 20)
        self.id_edit.move(80, 20)

        self.name_label.move(20, 50)
        self.name_edit.move(80, 50)

        self.age_label.move(20, 80)
        self.age_edit.move(80, 80)

        self.color_label.move(20, 110)
        self.color_edit.move(80, 110)

        self.height_label.move(20, 140)
        self.height_edit.move(80, 140)

        self.weight_label.move(20, 170)
        self.weight_edit.move(80, 170)

        self.vitamins_label.move(20, 200)
        self.vitamins_edit.move(80, 200)

        self.minerals_label.move(20, 230)
        self.minerals_edit.move(80, 230)

        self.add_button.move(20, 260)

        self.show()

    def add_cow(self):
        # �������� ������ �� ����� �����
        id = self.id_edit.text()
        name = self.name_edit.text()
        age = self.age_edit.text()
        color = self.color_edit.text()
        height = self.height_edit.text()
        weight = self.weight_edit.text()
        vitamins = self.vitamins_edit.text()
        minerals = self.minerals_edit.text()

        # ������� ������ ������
        cow = {
            "_id": id,
            "name": name,
            "age": age,
            "color": color,
            "height": height,
            "weight": weight,
            "vitamins": vitamins,
            "minerals": minerals
        }


        QMessageBox.information(self, "�����������", "������ ��������� � ���� ������")


if __name__ == '__main__':
    app = QApplication(sys.argv)