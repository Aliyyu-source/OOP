# file_handler.py

class FileHandler:
    filepath: str

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        return None

    def __str__(self) -> str:
        return self.filepath

    def read(self) -> list:
        rows = []
        try:
            filehandle = open(self.filepath, 'r', encoding="UTF-8")
            row = filehandle.readline()
            while row != '':
                rows.append(row.rstrip('\n'))
                row = filehandle.readline()
            filehandle.close()
        except Exception:
            print(f"Failed to read file '{self.filepath}'")
        return rows

    def write(self, rows: list) -> None:
        try:
            filehandle = open(self.filepath, 'w', encoding="UTF-8")
            for row in rows:
                filehandle.write(f"{row}\n")
            filehandle.close()
        except Exception:
            print(f"Failed to write file '{self.filepath}'")
        return None
