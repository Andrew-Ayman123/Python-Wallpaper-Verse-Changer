import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import change_wallpaper_daily as mainExec
import json
import win32com.client


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.jsonSettings = mainExec.loadSettings()
        self.verse_text = mainExec.get_bible_verse(
            self.jsonSettings["backUpText"])

        self.temp_image_path = "./.edited_wallpaper.png"
        self.setWindowTitle("Choose Background Verse")

        self.setMinimumSize(QtCore.QSize(661, 575))
        self.setMaximumSize(QtCore.QSize(661, 575))
        self.center_widget = QtWidgets.QWidget(self)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.center_widget)

        self.column = QtWidgets.QVBoxLayout()
        self.column.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.column.setContentsMargins(8, 8, 8, 8)
        self.column.setSpacing(8)
        # ROW 1 #############
        self.row1 = QtWidgets.QHBoxLayout()

        self.path_line_edit = QtWidgets.QLineEdit(self.center_widget)
        self.path_line_edit.setReadOnly(True)
        self.path_line_edit.setPlaceholderText(
            os.path.abspath(self.jsonSettings["imagePath"]))
        self.row1.addWidget(self.path_line_edit)

        self.bowse_button = QtWidgets.QPushButton(self.center_widget)
        self.bowse_button.setText("Browse")
        self.bowse_button.clicked.connect(self.browse_trig)
        self.row1.addWidget(self.bowse_button)

        self.save_button = QtWidgets.QPushButton(self.center_widget)
        self.save_button.setText("Save")
        self.save_button.clicked.connect(self.save_trig)
        self.row1.addWidget(self.save_button)

        self.column.addLayout(self.row1)

        # ROW 2 #############
        self.row2 = QtWidgets.QFormLayout()
        self.row2.setContentsMargins(0, 8, -1, -1)
        # ROW 2. Font Size
        self.font_size_label = QtWidgets.QLabel(self.center_widget)
        self.font_size_label.setText("Font Size:")
        self.row2.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.font_size_label)

        self.font_size_selector = QtWidgets.QSpinBox(self.center_widget)
        self.font_size_selector.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.font_size_selector.setMinimum(8)
        self.font_size_selector.setMaximum(96)
        self.font_size_selector.setSingleStep(4)
        self.font_size_selector.setProperty(
            "value", self.jsonSettings["fontSize"])
        self.font_size_selector.valueChanged.connect(self.font_size_trig)
        self.row2.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.font_size_selector)

        # ROW 2. Font Width
        self.font_width_label = QtWidgets.QLabel(self.center_widget)
        self.font_width_label.setText("Font Width:")
        self.row2.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.font_width_label)

        self.font_width_selector = QtWidgets.QSpinBox(self.center_widget)
        self.font_width_selector.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.font_width_selector.setMinimum(20)
        self.font_width_selector.setSingleStep(20)
        self.font_width_selector.setMaximum(1000)
        self.font_width_selector.setProperty(
            "value", self.jsonSettings["verseWidth"])
        self.font_width_selector.valueChanged.connect(self.font_width_trig)
        self.row2.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.font_width_selector)

        # ROW 2. Font Color
        self.font_color_label = QtWidgets.QLabel(self.center_widget)
        self.font_color_label.setText("Font Color:")
        self.row2.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.font_color_label)

        self.color_picker_button = QtWidgets.QPushButton(self.center_widget)
        self.color_picker_button.setText("Choose Color")
        self.color_picker_button.clicked.connect(self.font_color_trig)
        self.row2.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.color_picker_button)

        # ROW 2. Verse X Position
        self.verse_x_label = QtWidgets.QLabel(self.center_widget)
        self.verse_x_label.setText("Verse X Position:")
        self.row2.setWidget(
            3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.verse_x_label)

        self.verse_x_slider = QtWidgets.QSlider(self.center_widget)
        self.verse_x_slider.setMaximum(20)
        self.verse_x_slider.setSingleStep(2)
        self.verse_x_slider.setPageStep(5)
        self.verse_x_slider.setProperty(
            "value", self.jsonSettings["xRatio"]*20)
        self.verse_x_slider.setOrientation(QtCore.Qt.Horizontal)
        self.verse_x_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verse_x_slider.setTickInterval(1)
        self.verse_x_slider.valueChanged.connect(self.x_pos_trig)
        self.row2.setWidget(
            3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.verse_x_slider)

        # ROW 2. Verse Y Position
        self.verse_y_label = QtWidgets.QLabel(self.center_widget)
        self.verse_y_label.setText("Verse Y Position:")
        self.row2.setWidget(
            4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.verse_y_label)

        self.verse_y_slider = QtWidgets.QSlider(self.center_widget)
        self.verse_y_slider.setMaximum(20)
        self.verse_y_slider.setSingleStep(2)
        self.verse_y_slider.setPageStep(5)
        self.verse_y_slider.setProperty(
            "value", self.jsonSettings["yRatio"]*20)
        self.verse_y_slider.setOrientation(QtCore.Qt.Horizontal)
        self.verse_y_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verse_y_slider.setTickInterval(1)
        self.verse_y_slider.valueChanged.connect(self.y_pos_trig)
        self.row2.setWidget(
            4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.verse_y_slider)

        self.column.addLayout(self.row2)

        # ROW 3 #############
        self.row3 = QtWidgets.QHBoxLayout()

        self.background_image = QtWidgets.QWidget(self.center_widget)

        self.drawImage()

        self.row3.addWidget(self.background_image)

        self.column.addLayout(self.row3)

        # the column itself #############
        self.column.setStretch(2, 1)
        self.horizontalLayout_4.addLayout(self.column)
        self.setCentralWidget(self.center_widget)

    def drawImage(self):
        mainExec.write_image(
            self.jsonSettings, self.verse_text, self.temp_image_path)
        self.background_image.setStyleSheet(
            f"image: url(\"{self.temp_image_path}\")")

    def save_trig(self):
        result = QtWidgets.QMessageBox.question(self, "Saving Wallpaper Verse", "Are you sure you want to Save?",
                                                QtWidgets.QMessageBox.StandardButton.Save |
                                                QtWidgets.QMessageBox.StandardButton.Cancel)
        if result == QtWidgets.QMessageBox.StandardButton.Save:
            self.schedule_task()
            self.save_settings_execute()

    def schedule_task(self):
        # To-Do:check if a schedule is there before and if not create one
        scheduler: win32com.client.CDispatch = win32com.client.Dispatch(
            "Schedule.Service")
        scheduler.Connect()
        root_folder = scheduler.GetFolder('\\')

        # Get the task definition for the specified task name
        try:
            task = root_folder.GetTask(self.jsonSettings["taskName"])
        except Exception as e:
            # Constants used in the task scheduler API
            TASK_TRIGGER_DAILY = 2
            TASK_ACTION_EXEC = 0
            TASK_CREATE_OR_UPDATE = 6
            TASK_LOGON_INTERACTIVE_TOKEN = 3
            FILE_EXECUTED='./change_wallpaper_daily.py'

            task = scheduler.NewTask(0)
            # Set the task settings
            task.RegistrationInfo.Description = self.jsonSettings["taskName"]
            task.Settings.Enabled = True
            task.Settings.Hidden = True

            # Set the task trigger to run daily at the specified time
            trigger = task.Triggers.Create(TASK_TRIGGER_DAILY)
            trigger.StartBoundary = datetime.datetime.now().strftime('%Y-%m-%dT23:59:59')
            trigger.DaysInterval = 1
            trigger.ExecutionTimeLimit = 'PT1M'  # 1 hour time limit
            trigger.Enabled = True

            # Set the task action to run a Python script
            action = task.Actions.Create(
                TASK_ACTION_EXEC)
            
            action.Path = os.path.abspath(FILE_EXECUTED)
            action.WorkingDirectory = os.path.abspath(os.path.dirname(FILE_EXECUTED))

            # Set the task settings
            task.Settings.ExecutionTimeLimit = 'PT1M'  # 1 hour
            task.Settings.StartWhenAvailable  = True  # Run task as soon as possible after a scheduled start is missed
            task.Settings.RestartInterval = 'PT1M'  # Restart every 1 minute
            task.Settings.RestartCount = 2  # Attempt to restart up to 2 times

            # Add the task to the root folder
            root_folder.RegisterTaskDefinition(
                self.jsonSettings["taskName"],
                task,  # Task definition object
                TASK_CREATE_OR_UPDATE,  # Create or update the task
                '',  # No user account information
                '',  # No password
                # Log on with an interactive token
                TASK_LOGON_INTERACTIVE_TOKEN,
            )

        # Close the task scheduler object
        scheduler = None

    def save_settings_execute(self):
        with open("./settings.json", "w", encoding="utf-8") as json_file:
            # Write the dictionary to the JSON file
            json.dump(self.jsonSettings, json_file, ensure_ascii=False)
        mainExec.main()

    def browse_trig(self):
        file_filter = "Image files (*.png *.jpg *.jpeg *.bmp);;All files (*.*)"
        try:
            file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
                self, "Open image file", "", file_filter)
            if file_name:
                self.jsonSettings["imagePath"] = file_name
                self.path_line_edit.setPlaceholderText(
                    os.path.abspath(self.jsonSettings["imagePath"]))
                self.drawImage()
        except:
            print("This is not a valid image")

    def font_size_trig(self, val):
        self.jsonSettings["fontSize"] = val
        self.drawImage()

    def font_width_trig(self, val):
        self.jsonSettings["verseWidth"] = val
        self.drawImage()

    def font_color_trig(self):
        color = QtWidgets.QColorDialog.getColor(
            QtGui.QColor(self.jsonSettings["fontColor"]))
        if color.isValid():
            self.jsonSettings["fontColor"] = color.name()
            self.drawImage()

    def x_pos_trig(self, val):
        self.jsonSettings["xRatio"] = val/20
        self.drawImage()

    def y_pos_trig(self, val):
        self.jsonSettings["yRatio"] = val/20
        self.drawImage()

    def closeEvent(self, event):
        if (self.jsonSettings == mainExec.loadSettings()):
            return

        result = QtWidgets.QMessageBox.warning(self, "Not Saved", "Are you sure you want to exit without saving?",
                                               QtWidgets.QMessageBox.StandardButton.Save |
                                               QtWidgets.QMessageBox.StandardButton.Discard | QtWidgets.QMessageBox.StandardButton.Cancel)
        if result == QtWidgets.QMessageBox.StandardButton.Save:
            self.save_settings_execute()
            event.accept()
        elif result == QtWidgets.QMessageBox.StandardButton.Discard:
            event.accept()
        elif result == QtWidgets.QMessageBox.StandardButton.Cancel:
            event.ignore()
        else:  # Redundant
            event.accept()

    def final_close(self):
        os.remove(self.temp_image_path)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    icon = QtGui.QIcon("./logo.png")
    app.setWindowIcon(icon)

    mainWindow = MainWindow()

    app.aboutToQuit.connect(mainWindow.final_close)
    mainWindow.show()
    sys.exit(app.exec_())
