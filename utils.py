import csv
import requests


def download_csv(url: str, fp: str) -> int:
    """
    下載網路上的指定csv檔案
    """
    req = requests.get(url)
    if req.ok:
        content = req.content
        with open(fp, mode="wb") as csvf:
            csvf.write(content)
    return req.status_code


def load_csv(fp: str, attributes: list) -> list:
    """
    以指定欄位載入csv檔案變成一個tuple，每一個row是一個dictionary。
    """
    csv_data = []
    with open(fp, mode="r",  encoding="utf-8-sig", newline="") as csvf:
        dict_reader = csv.DictReader(csvf)
        for row in dict_reader:
            row_data = {attr: row.get(attr, "") for attr in attributes}
            # substitute empty values with NULL
            for k in row_data:
                if not row_data[k]:
                    row_data[k] = "NULL"
            csv_data.append(row_data)
    return list(csv_data)


def store_csv(fp: str, csv_data: list):
    if not csv_data or not isinstance(csv_data[0], dict):
        print("[*] csv_data error.")
        return []
    fieldnames = list(csv_data[0].keys())
    with open(fp, mode="w", encoding="utf-8-sig", newline="") as csvf:
        dict_writer = csv.DictWriter(csvf, fieldnames=fieldnames)
        dict_writer.writeheader()
        for row in csv_data:
            dict_writer.writerow(row)
