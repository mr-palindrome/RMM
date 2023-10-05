import tkinter as tk
from tkinter import ttk
import threading
import asyncio
import json
import websockets


class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RMM Dashboard")
        self.root.geometry("500x800")

        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.log_listbox = tk.Listbox(self.frame, width=80, height=20)
        self.log_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.log_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_listbox.config(yscrollcommand=self.scrollbar.set)

        self.websocket_thread = threading.Thread(target=self.start_websocket)
        self.websocket_thread.daemon = True
        self.websocket_thread.start()
        self.device_list = []

    async def connect_to_websocket(self):
        async with websockets.connect(
            "ws://localhost:8000/ws/device_status/"
        ) as websocket:
            while True:
                message = await websocket.recv()
                self.on_message(message)

    def start_websocket(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.connect_to_websocket())

    def on_message(self, message):
        device_data = json.loads(message)
        if device_data.get("msg") == "connected":
            device_data = device_data["data"]
            for device in device_data:
                device_name = device["name"]
                status = device["status"]
                last_update = device["updated_at"]
                self.device_list.append(device)
                device_info = f"\t{device_name:<30} {status:<20} {last_update}"
                self.log_listbox.insert(device["id"], device_info)

        else:
            device_name = device_data["name"]
            status = device_data["status"]
            last_update = device_data["updated_at"]
            self.device_list.append(device_name)
            device_info = f"\t{device_name:<30} {status:<20} {last_update}"

            index_device = self.log_listbox.get(
                first=device_data["id"] - 1, last=device_data["id"]-1
            )
            index = device_data["id"]-1
            if len(index_device) > 0:
                self.log_listbox.delete(index)
                # index -= 1
            self.log_listbox.insert(index, device_info)
            self.highlight_device(index)
            self.root.after(5000, lambda: self.remove_highlight(index))

    def highlight_device(self, index):
        self.log_listbox.itemconfig(index, {"bg": "#bfbfbf"})

    def remove_highlight(self, index):
        self.log_listbox.itemconfig(index, {"bg": "black"})


if __name__ == "__main__":
    root_tk = tk.Tk()
    app = DashboardApp(root_tk)
    root_tk.mainloop()
