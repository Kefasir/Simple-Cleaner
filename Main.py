import sys
import shutil
import ctypes
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import QSettings
from PySide6.QtGui import QIcon

from UI import Ui_MainWindow
from fast_menu import Ui_FAST_MENU
from deep_menu import Ui_DEEP_MENU
from custom_menu import Ui_CUSTOM_MENU


class FAST(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FAST_MENU()
        self.ui.setupUi(self)
        self.setWindowTitle("Fast settings")

        self.clean_options = {
            self.ui.checkBoxFAST1: [r"C:\Temp"],
            self.ui.checkBoxFAST1_2: [r"C:\Windows\Temp"],
            self.ui.checkBoxFAST1_4: ["RECYCLE_BIN"]
        }

        self.settings = QSettings("MyCleaner", "FAST")

        for checkbox in self.clean_options:
            checkbox.setChecked(self.settings.value(checkbox.objectName(), False, type=bool))
            checkbox.toggled.connect(self.save_checkbox)

    def save_checkbox(self, checked):
        checkbox = self.sender()
        self.settings.setValue(checkbox.objectName(), checked)

    def get_patch(self):
        paths = []
        for checkbox, checkbox_paths in self.clean_options.items():
            if checkbox.isChecked():
                paths.extend(checkbox_paths)
        return paths


class DEEP(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DEEP_MENU()
        self.ui.setupUi(self)
        self.setWindowTitle("Deep settings")

        user_profile = os.environ.get("USERPROFILE")
        local_appdata = os.environ.get("LOCALAPPDATA")

        self.clean_options = {
            self.ui.checkBoxDEEP1: [r"C:\ProgramData\Microsoft\Windows\WER\Temp"],
            self.ui.checkBoxDEEP2: [fr"{local_appdata}\Microsoft\Windows\Explorer"],
            self.ui.checkBoxDEEP4: [fr"{local_appdata}\NVIDIA\DXCache"],
            self.ui.checkBoxDEEP5: [fr"{local_appdata}\Google\Chrome\User Data\Default\Cache\Cache_Data"],
            self.ui.checkBoxDEEP6: [fr"{user_profile}\AppData\Roaming\discord\Cache\Cache_Data"],
            self.ui.checkBoxDEEP7: [fr"{user_profile}\Downloads"]
        }

        self.settings = QSettings("MyCleaner", "DEEP")

        for checkbox in self.clean_options:
            checkbox.setChecked(self.settings.value(checkbox.objectName(), False, type=bool))
            checkbox.toggled.connect(self.save_checkbox)

    def save_checkbox(self, checked):
        checkbox = self.sender()
        self.settings.setValue(checkbox.objectName(), checked)

    def get_patch(self):
        paths = []
        for checkbox, checkbox_paths in self.clean_options.items():
            if checkbox.isChecked():
                paths.extend(checkbox_paths)
        return paths


class CUSTOM(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CUSTOM_MENU()
        self.ui.setupUi(self)
        self.setWindowTitle("Custom settings")

        user_profile = os.environ.get("USERPROFILE")
        local_appdata = os.environ.get("LOCALAPPDATA")

        self.clean_options = {
            self.ui.checkBoxFAST1_1: [r"C:\Temp"],
            self.ui.checkBoxFAST1_2_1: [r"C:\Windows\Temp"],
            self.ui.checkBoxFAST1_4_1: ["RECYCLE_BIN"],
            self.ui.checkBoxDEEP1: [r"C:\ProgramData\Microsoft\Windows\WER\Temp"],
            self.ui.checkBoxDEEP2: [fr"{local_appdata}\Microsoft\Windows\Explorer"],
            self.ui.checkBoxDEEP4: [fr"{local_appdata}\NVIDIA\DXCache"],
            self.ui.checkBoxDEEP5: [fr"{local_appdata}\Google\Chrome\User Data\Default\Cache\Cache_Data"],
            self.ui.checkBoxDEEP6: [fr"{user_profile}\AppData\Roaming\discord\Cache\Cache_Data"],
            self.ui.checkBoxDEEP7: [fr"{user_profile}\Downloads"]
        }

        self.settings = QSettings("MyCleaner", "Custom")

        for checkbox in self.clean_options:
            checkbox.setChecked(self.settings.value(checkbox.objectName(), False, type=bool))
            checkbox.toggled.connect(self.save_checkbox)

    def save_checkbox(self, checked):
        checkbox = self.sender()
        self.settings.setValue(checkbox.objectName(), checked)

    def get_patch(self):
        paths = []
        for checkbox, checkbox_paths in self.clean_options.items():
            if checkbox.isChecked():
                paths.extend(checkbox_paths)
        return paths


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Cleaner")
        self.setWindowIcon(QIcon("cleaner.ico"))

        self.settings_fast = None
        self.settings_deep = None
        self.settings_custom = None
        self.scanned = False
        self.ui.BAR.setValue(0)
        self.ui.CLEAR.setEnabled(False)

        self.FREE_MEMORY()
        self.ui.FAST.clicked.connect(self.open_fast)
        self.ui.DEEP.clicked.connect(self.open_deep)
        self.ui.CUSTOM.clicked.connect(self.open_custom)
        self.ui.SCAN.clicked.connect(self.scan)
        self.ui.CLEAR.clicked.connect(self.clear)

    def open_fast(self):

        self.settings_fast = FAST(self)
        self.settings_fast.show()
        self.ui.SEL_MODE.setText("Selected Clean mode: FAST")

    def open_deep(self):

        self.settings_deep = DEEP(self)
        self.settings_deep.show()
        self.ui.SEL_MODE.setText("Selected Clean mode: DEEP")

    def open_custom(self):

        self.settings_custom = CUSTOM(self)
        self.settings_custom.show()
        self.ui.SEL_MODE.setText("Selected Clean mode: CUSTOM")

    def FREE_MEMORY(self):

        usage = shutil.disk_usage("C:")
        free_gb = usage.free / (1024 ** 3)
        total_gb = usage.total / (1024 ** 3)
        self.ui.FREE.setText(f"{free_gb:.1f} GB / {total_gb:.1f} GB")

        return usage.free

    def get_all_paths(self):

        paths = []

        if self.settings_fast is not None:
            paths.extend(self.settings_fast.get_patch())
        if self.settings_deep is not None:
            paths.extend(self.settings_deep.get_patch())
        if self.settings_custom is not None:
            paths.extend(self.settings_custom.get_patch())

        return paths

    def get_files(self, folder_path):

        files = []

        if not os.path.exists(folder_path):
            return files
        for root, dirs, filenames in os.walk(folder_path):
            for file in filenames:
                files.append(os.path.join(root, file))

        return files

    def scan(self):

        all_files = []

        for folder_path in self.get_all_paths():
            if folder_path != "RECYCLE_BIN":
                all_files.extend(self.get_files(folder_path))

        total_files = len(all_files)
        total_size = 0

        self.ui.BAR.setValue(0)

        if total_files == 0:

            self.ui.RESULTS.setText("0 B")
            self.scanned = False
            self.ui.CLEAR.setEnabled(False)

            return

        self.ui.SCAN.setEnabled(False)

        for index, file_path in enumerate(all_files, 1):

            try:
                total_size += os.path.getsize(file_path)
            except (PermissionError, FileNotFoundError, OSError):
                pass
            self.ui.BAR.setValue(int(index / total_files * 100))


        self.ui.RESULTS.setText(self.format_byte(total_size))
        self.scanned = True
        self.ui.CLEAR.setEnabled(total_size > 0)
        self.ui.SCAN.setEnabled(True)

    def clear(self):

        if not self.scanned:
            self.ui.RESULTS.setText("Scan it first!")

            return

        all_paths = self.get_all_paths()
        files_to_delete = []
        recycle_bin = False

        for folder_path in all_paths:
            if folder_path == "RECYCLE_BIN":
                recycle_bin = True
            else:
                files_to_delete.extend(self.get_files(folder_path))

        total_items = len(files_to_delete) + (1 if recycle_bin else 0)

        if total_items == 0:

            self.ui.BAR.setValue(100)
            self.ui.RESULTS.setText("0 B")
            self.scanned = False
            self.ui.CLEAR.setEnabled(False)
            self.FREE_MEMORY()

            return

        self.ui.CLEAR.setEnabled(False)
        self.ui.SCAN.setEnabled(False)
        self.ui.BAR.setValue(0)

        cleaned = 0

        for file_path in files_to_delete:
            try:
                os.remove(file_path)
            except (PermissionError, FileNotFoundError, OSError):
                pass

            cleaned += 1
            self.ui.BAR.setValue(int(cleaned / total_items * 100))

        for folder_path in all_paths:

            if folder_path != "RECYCLE_BIN" and os.path.exists(folder_path):
                for root, dirs, files in os.walk(folder_path, topdown=False):
                    for directory in dirs:
                        try:
                            os.rmdir(os.path.join(root, directory))
                        except (PermissionError, OSError):

                            pass

        if recycle_bin:
            try:
                ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 7)
            except Exception:
                pass

            cleaned += 1

            self.ui.BAR.setValue(int(cleaned / total_items * 100))

        self.ui.BAR.setValue(100)
        self.ui.RESULTS.setText("0 B")
        self.scanned = False
        self.ui.SCAN.setEnabled(True)
        self.ui.CLEAR.setEnabled(False)
        self.FREE_MEMORY()

    def format_byte(self, size):
        if size >= 1024 ** 3:
            return f"{size / (1024 ** 3):.2f} GB"
        if size >= 1024 ** 2:
            return f"{size / (1024 ** 2):.2f} MB"
        if size >= 1024:
            return f"{size / 1024:.2f} KB"
        return f"{size} B"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
