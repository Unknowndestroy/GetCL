
# pip install pynput keyboard win10toast pyautogui pillow

import keyboard
from pynput.mouse import Listener as MouseListener
from win10toast import ToastNotifier
from PIL import ImageDraw
import pyautogui
import sys

clicks = []
toaster = ToastNotifier()

MAX_CLICKS = 4  

def on_click(x, y, button, pressed):
    if not pressed:
        return
    clicks.append((x, y))
    msg = f"Tıklandı: ({x}, {y})"
    print(f"🖱️ {msg}")
    toaster.show_toast("Click Kayıt", msg, duration=3, threaded=True)
    if len(clicks) >= MAX_CLICKS:
        toaster.show_toast("Click Kayıt", "Kayıt bitti!", duration=3, threaded=True)
        return False  

if __name__ == "__main__":
    print(f"F9’a bas, {MAX_CLICKS} tıklamayı kaydetmeye başlarsın.")
    keyboard.wait('f9')  
    print(f"📌 Kayıt başlıyor! Ekrana {MAX_CLICKS} kere tıkla...")
    toaster.show_toast("Click Kayıt", "Kayıt başlıyor!", duration=3, threaded=True)

    with MouseListener(on_click=on_click) as listener:
        listener.join()

    print("\n✅ Kaydedilen koordinatlar:")
    for i, (x, y) in enumerate(clicks, 1):
        print(f"  {i}. ({x}, {y})")

    screenshot = pyautogui.screenshot()
    draw = ImageDraw.Draw(screenshot)
    draw.line(clicks, fill="red", width=3)
    for (x, y) in clicks:
        r = 5
        draw.ellipse((x-r, y-r, x+r, y+r), outline="blue", width=2)
    screenshot.show()

    input("\nEnter’a bas çıkmak için...")
    print("Çıkılıyor, güle güle 🖕")
