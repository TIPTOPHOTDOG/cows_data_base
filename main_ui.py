import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox


class CowDatabaseUI(QWidget):

    def __init__(self):
        super().__init__()

        # Идентификатор коровы
        self.id_label = QLabel("Идентификатор:")
        self.id_edit = QLineEdit()

        # Имя коровы
        self.name_label = QLabel("Имя:")
        self.name_edit = QLineEdit()

        # Возраст коровы
        self.age_label = QLabel("Возраст:")
        self.age_edit = QLineEdit()

        # Цвет коровы
        self.color_label = QLabel("Цвет:")
        self.color_edit = QLineEdit()

        # Рост коровы
        self.height_label = QLabel("Рост:")
        self.height_edit = QLineEdit()

        # Вес коровы
        self.weight_label = QLabel("Вес:")
        self.weight_edit = QLineEdit()

        # Витамины коровы
        self.vitamins_label = QLabel("Витамины:")
        self.vitamins_edit = QLineEdit()

        # Микроэлементы коровы
        self.minerals_label = QLabel("Микроэлементы:")
        self.minerals_edit = QLineEdit()

        # Кнопка добавления коровы
        self.add_button = QPushButton("Добавить")
        self.add_button.clicked.connect(self.add_cow)

        # Расположение элементов на экране
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
        # Получаем данные из полей ввода
        id = self.id_edit.text()
        name = self.name_edit.text()
        age = self.age_edit.text()
        color = self.color_edit.text()
        height = self.height_edit.text()
        weight = self.weight_edit.text()
        vitamins = self.vitamins_edit.text()
        minerals = self.minerals_edit.text()

        # Создаем объект коровы
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


        QMessageBox.information(self, "Уведомление", "Корова добавлена в базу данных")


if __name__ == '__main__':
    app = QApplication(sys.argv)