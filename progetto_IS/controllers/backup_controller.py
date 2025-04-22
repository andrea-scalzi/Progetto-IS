import os
import shutil
import threading
import time
from datetime import datetime, timedelta


class BackupController:
    def __init__(self, data_path="data", backup_path="backup"):
        self.data_path = data_path
        self.backup_path = backup_path

        self.inizio_backup_automatico()

    def esegui_backup(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = os.path.join(self.backup_path, f"backup_{timestamp}")

        os.makedirs(backup_dir)

        for file in os.listdir(self.data_path):
            if file.endswith(".json"):
                shutil.copy(os.path.join(self.data_path, file), os.path.join(backup_dir, file))

        return True

    def lista_backup(self):
        backup_list = [d for d in os.listdir(self.backup_path) if d.startswith("backup_")]
        return sorted(backup_list, reverse=True)

    def ripristina_backup(self, backup_name):
        backup_dir = os.path.join(self.backup_path, backup_name)

        if not os.path.exists(backup_dir):
            return False

        for file in os.listdir(backup_dir):
            if file.endswith(".json"):
                shutil.copy(os.path.join(backup_dir, file), os.path.join(self.data_path, file))

        return True

    def elimina_backup(self, backup_name):
        backup_dir = os.path.join(self.backup_path, backup_name)

        if os.path.exists(backup_dir):
            shutil.rmtree(backup_dir)
            return True

        return False

    def backup_automatico(self):
        while True:
            now = datetime.now()
            next_backup = now + timedelta(days=(7 - now.weekday()) % 7)
            next_backup = next_backup.replace(hour=18, minute=0, second=0, microsecond=0)

            seconds_to_wait = (next_backup - now).total_seconds()
            time.sleep(seconds_to_wait)

            self.esegui_backup()

    def inizio_backup_automatico(self):
        thread = threading.Thread(target=self.backup_automatico, daemon=True)
        thread.start()
