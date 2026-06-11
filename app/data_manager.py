import json
import os
from typing import List, Dict, Any, Optional


class DataManager:
    def __init__(self, filename: str = "accounts.json"):

        current_dir = os.path.dirname(os.path.abspath(__file__))

        project_root = os.path.dirname(current_dir)

        self.filepath = os.path.join(project_root, "data", filename)

        data_folder = os.path.dirname(self.filepath)
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)

    def _load_raw_data(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.filepath):
            return []

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"[Warning] Could not read data file: {e}")
            return []

    def save_account(self, account_data: Dict[str, Any]) -> None:
        all_accounts = self._load_raw_data()

        account_updated = False
        for i, acc in enumerate(all_accounts):
            if acc["account_number"] == account_data["account_number"]:
                all_accounts[i] = account_data
                account_updated = True
                break

        if not account_updated:
            all_accounts.append(account_data)

        self._write_to_file(all_accounts)

    def get_account(self, account_number: str) -> Optional[Dict[str, Any]]:
        all_accounts = self._load_raw_data()
        for acc in all_accounts:
            if acc["account_number"] == account_number:
                return acc
        return None

    def _write_to_file(self, data: List[Dict[str, Any]]) -> None:
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"[Critical Error] Could not save data: {e}")
