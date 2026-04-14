class FileHandler:
    filepath: str 
    def __init__(self, filepath: str):
        self.filepath = filepath
        return None
    

    def read(self) -> list[str]:
        rows: list[str] = []
        try:
            filehandle = open(self.filepath, "r", encoding="utf-8")
            rows = filehandle.readlines()
            while row != "":
                rows.append(row.strip())
                row = filehandle.readline()
            filehandle.close()
        except Exception:
            print(f'file not found')
           
            return rows