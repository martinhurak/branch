from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

extension = ".csv"
filename = "extract_" + timestamp + extension

DATA_DIR = "./data"

REALSOFT_RAW_FOLDER = DATA_DIR + "/raw/realsoft/"
REALSOFT_RAW_FILENAME = DATA_DIR + "/raw/realsoft/" + filename
