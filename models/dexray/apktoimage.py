from androguard.core.bytecodes.apk import APK
from PIL import Image

def get_dex_bytes(apk: APK) -> bytes:
    for f in apk.get_files():
        if f.endswith(".dex"):
            yield apk.get_file(f)

def generate_png(apk: APK, filename: str, folder: str):
    stream = bytes()
    for s in get_dex_bytes(apk):
        stream += s
    current_len = len(stream)
    image = Image.frombytes(mode='L', size=(1, current_len), data=stream)
    filename = filename.split("/")[-1]
    image.save(f"{folder}/{filename}.png")
    return "{folder}/{filename}.png"
    
def apktoimage(filename, destination_folder):
    apk = APK(filename)
    return generate_png(apk, filename, destination_folder)