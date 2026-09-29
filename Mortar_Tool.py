"""Mortar Tool - Wardogs mortar calculator, desktop launcher."""
import ctypes
import os
import sys

TITLE = "Mortar Calculator - Wardogs"

def resource_path(name):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)

def alert(msg):
    # Last-resort dialog: works even if the web layer never came up.
    ctypes.windll.user32.MessageBoxW(None, msg, "Mortar Tool", 0x10)

def main():
    # Persist localStorage (last coordinates, Y-flip) across runs
    data_dir = os.path.join(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")), "MortarTool")
    os.makedirs(data_dir, exist_ok=True)
    os.environ["WEBVIEW2_USER_DATA_FOLDER"] = data_dir

    html = resource_path("Mortar_Tool.html")
    if not os.path.exists(html):
        alert("Mortar_Tool.html is missing from the application files.\nReinstall Mortar Tool.")
        sys.exit(1)

    try:
        import webview
        webview.create_window(TITLE, html, width=860, height=1060, min_size=(420, 700))
        webview.start(private_mode=False)
    except Exception as e:
        alert(
            "Mortar Tool could not start its window.\n\n"
            "The Microsoft WebView2 runtime is required and normally ships with Windows 11.\n"
            "Install it from: https://developer.microsoft.com/microsoft-edge/webview2/\n\n"
            f"Details: {e}"
        )
        sys.exit(1)

if __name__ == "__main__":
    main()
