import tkinter as tk
from tkinter import ttk, messagebox
import requests
import threading
import socket
import subprocess
import platform
import pyperclip
from datetime import datetime

class AdvancedIPFinder:
    def __init__(self):
        self.window = tk.Tk()
        self.setup_window()
        self.setup_styles()
        self.create_widgets()
        self.current_public_ip = None
        
    def setup_window(self):
        self.window.title("IP Address Finder")
        self.window.geometry("450x600")
        self.window.configure(bg="#1a1a1a")
        self.window.resizable(False, False)
        
        self.center_window()
        
        try:
            self.window.iconbitmap("ico/app_icon.ico")
        except:
            pass
    
    def center_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
    
    def setup_styles(self):
        self.colors = {
            'bg_primary': '#1a1a1a',
            'bg_secondary': '#2d2d2d',
            'bg_tertiary': '#404040',
            'accent': '#4a9eff',
            'accent_hover': '#66b3ff',
            'text_primary': '#ffffff',
            'text_secondary': '#b0b0b0',
            'success': '#4caf50',
            'error': '#f44336',
            'warning': '#ff9800'
        }
    
    def create_widgets(self):
        main_frame = tk.Frame(self.window, bg=self.colors['bg_primary'])
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        self.create_header(main_frame)
        
        self.create_public_ip_section(main_frame)
        
        self.create_local_ip_section(main_frame)
        
        self.create_info_section(main_frame)
        
        self.create_footer(main_frame)
    
    def create_header(self, parent):
        header_frame = tk.Frame(parent, bg=self.colors['bg_primary'])
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(
            header_frame, 
            text="🌐 IP Address Finder",
            font=('Helvetica', 18, 'bold'),
            bg=self.colors['bg_primary'],
            fg=self.colors['text_primary']
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            header_frame,
            text="Find your public and local IP address",
            font=('Helvetica', 10),
            bg=self.colors['bg_primary'],
            fg=self.colors['text_secondary']
        )
        subtitle_label.pack(pady=(5, 0))
    
    def create_public_ip_section(self, parent):
        section_frame = tk.Frame(parent, bg=self.colors['bg_secondary'])
        section_frame.pack(fill='x', pady=(0, 15))
        
        content_frame = tk.Frame(section_frame, bg=self.colors['bg_secondary'])
        content_frame.pack(fill='x', padx=15, pady=15)
        
        section_title = tk.Label(
            content_frame,
            text="🌍 Public IP",
            font=('Helvetica', 12, 'bold'),
            bg=self.colors['bg_secondary'],
            fg=self.colors['text_primary']
        )
        section_title.pack(anchor='w')
        
        button_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'])
        button_frame.pack(fill='x', pady=(10, 0))
        
        self.get_ip_button = tk.Button(
            button_frame,
            text="🔍 Get Public IP",
            command=self.get_public_ip_threaded,
            bg=self.colors['accent'],
            fg='white',
            font=('Helvetica', 11, 'bold'),
            relief='flat',
            cursor='hand2',
            padx=30,
            pady=12
        )
        self.get_ip_button.pack(anchor='w')
        
        self.get_ip_button.bind('<Enter>', self.on_button_hover)
        self.get_ip_button.bind('<Leave>', self.on_button_leave)
        
        self.public_ip_result = tk.Label(
            content_frame,
            text="Click the button to get your public IP",
            font=('Helvetica', 11),
            bg=self.colors['bg_secondary'],
            fg=self.colors['text_secondary'],
            wraplength=400
        )
        self.public_ip_result.pack(anchor='w', pady=(10, 0))
        
        self.public_actions_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'])
    
    def create_local_ip_section(self, parent):
        section_frame = tk.Frame(parent, bg=self.colors['bg_secondary'])
        section_frame.pack(fill='x', pady=(0, 15))
        
        content_frame = tk.Frame(section_frame, bg=self.colors['bg_secondary'])
        content_frame.pack(fill='x', padx=15, pady=15)
        
        section_title = tk.Label(
            content_frame,
            text="🏠 Local IP",
            font=('Helvetica', 12, 'bold'),
            bg=self.colors['bg_secondary'],
            fg=self.colors['text_primary']
        )
        section_title.pack(anchor='w')
        
        local_ip = self.get_local_ip()
        self.local_ip_result = tk.Label(
            content_frame,
            text=f"Your local IP is: {local_ip}",
            font=('Helvetica', 11),
            bg=self.colors['bg_secondary'],
            fg=self.colors['success']
        )
        self.local_ip_result.pack(anchor='w', pady=(10, 0))
        
        copy_local_button = tk.Button(
            content_frame,
            text="📋 Copy",
            command=lambda: self.copy_to_clipboard(local_ip),
            bg=self.colors['bg_tertiary'],
            fg=self.colors['text_primary'],
            font=('Helvetica', 9),
            relief='flat',
            cursor='hand2',
            padx=15,
            pady=5
        )
        copy_local_button.pack(anchor='w', pady=(5, 0))
    
    def create_info_section(self, parent):
        section_frame = tk.Frame(parent, bg=self.colors['bg_secondary'])
        section_frame.pack(fill='x', pady=(0, 15))
        
        content_frame = tk.Frame(section_frame, bg=self.colors['bg_secondary'])
        content_frame.pack(fill='x', padx=15, pady=15)
        
        section_title = tk.Label(
            content_frame,
            text="ℹ️ System Information",
            font=('Helvetica', 12, 'bold'),
            bg=self.colors['bg_secondary'],
            fg=self.colors['text_primary']
        )
        section_title.pack(anchor='w')
        
        system_info = f"System: {platform.system()} {platform.release()}"
        hostname = socket.gethostname()
        
        info_text = f"Hostname: {hostname}\n{system_info}"
        
        self.info_label = tk.Label(
            content_frame,
            text=info_text,
            font=('Helvetica', 10),
            bg=self.colors['bg_secondary'],
            fg=self.colors['text_secondary'],
            justify='left'
        )
        self.info_label.pack(anchor='w', pady=(10, 0))
    
    def create_footer(self, parent):
        footer_frame = tk.Frame(parent, bg=self.colors['bg_primary'])
        footer_frame.pack(fill='x', side='bottom')
        
        footer_label = tk.Label(
            footer_frame,
            text=f"© 2024 EventExecutor | Last Update: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
            font=('Helvetica', 8),
            bg=self.colors['bg_primary'],
            fg=self.colors['text_secondary']
        )
        footer_label.pack()
    
    def on_button_hover(self, event):
        event.widget.config(bg=self.colors['accent_hover'])
    
    def on_button_leave(self, event):
        event.widget.config(bg=self.colors['accent'])
    
    def get_local_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            return local_ip
        except Exception:
            try:
                return socket.gethostbyname(socket.gethostname())
            except:
                return "Not available"
    
    def get_public_ip_threaded(self):
        self.get_ip_button.config(text="🔄 Loading...", state='disabled')
        thread = threading.Thread(target=self.get_public_ip)
        thread.daemon = True
        thread.start()
    
    def get_public_ip(self):
        try:
            services = [
                "https://api.ipify.org?format=json",
                "https://httpbin.org/ip",
                "https://api.myip.com"
            ]
            
            for service in services:
                try:
                    response = requests.get(service, timeout=5)
                    response.raise_for_status()
                    
                    if "ipify" in service:
                        data = response.json()
                        ip_address = data['ip']
                    elif "httpbin" in service:
                        data = response.json()
                        ip_address = data['origin']
                    elif "myip" in service:
                        data = response.json()
                        ip_address = data['ip']
                    
                    self.current_public_ip = ip_address
                    self.window.after(0, lambda: self.update_public_ip_result(ip_address, True))
                    return
                    
                except requests.RequestException:
                    continue
            
            self.window.after(0, lambda: self.update_public_ip_result("", False))
            
        except Exception as e:
            self.window.after(0, lambda: self.update_public_ip_result("", False))
    
    def update_public_ip_result(self, ip_address, success):
        self.get_ip_button.config(text="🔍 Get Public IP", state='normal')
        
        if success:
            self.public_ip_result.config(
                text=f"Your public IP is: {ip_address}",
                fg=self.colors['success']
            )
            self.show_public_ip_actions()
        else:
            self.public_ip_result.config(
                text="❌ Error retrieving public IP. Check the Internet connection.",
                fg=self.colors['error']
            )
            self.hide_public_ip_actions()
    
    def show_public_ip_actions(self):
        self.public_actions_frame.pack(anchor='w', pady=(10, 0))
        
        copy_button = tk.Button(
            self.public_actions_frame,
            text="📋 Copy IP",
            command=lambda: self.copy_to_clipboard(self.current_public_ip),
            bg=self.colors['bg_tertiary'],
            fg=self.colors['text_primary'],
            font=('Helvetica', 9),
            relief='flat',
            cursor='hand2',
            padx=15,
            pady=5
        )
        copy_button.pack(side='left', padx=(0, 10))
        
        geo_button = tk.Button(
            self.public_actions_frame,
            text="🌍 Info Geo",
            command=self.show_geo_info,
            bg=self.colors['bg_tertiary'],
            fg=self.colors['text_primary'],
            font=('Helvetica', 9),
            relief='flat',
            cursor='hand2',
            padx=15,
            pady=5
        )
        geo_button.pack(side='left')
    
    def hide_public_ip_actions(self):
        self.public_actions_frame.pack_forget()

        for widget in self.public_actions_frame.winfo_children():
            widget.destroy()
    
    def copy_to_clipboard(self, text):
        try:
            pyperclip.copy(text)
            messagebox.showinfo("Success", f"IP copied to clipboard!\n{text}")
        except:
            self.window.clipboard_clear()
            self.window.clipboard_append(text)
            messagebox.showinfo("Success", f"IP copied to clipboard!\n{text}")
    
    def show_geo_info(self):
        if not self.current_public_ip:
            return
            
        try:
            response = requests.get(f"http://ip-api.com/json/{self.current_public_ip}", timeout=5)
            data = response.json()
            
            if data['status'] == 'success':
                info = f"""
Geolocation Information:
━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌍 Country: {data.get('country', 'N/A')}
🏙️ City: {data.get('city', 'N/A')}
📍 Region: {data.get('regionName', 'N/A')}
🌐 ISP: {data.get('isp', 'N/A')}
🏢 Organization: {data.get('org', 'N/A')}
🕐 Timezone: {data.get('timezone', 'N/A')}
📊 Coordinates: {data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}
                """
                messagebox.showinfo("Geolocation Info", info)
            else:
                messagebox.showerror("Error", "Unable to obtain geolocation information")
        except Exception as e:
            messagebox.showerror("Error", "Error in retrieving geographic information")
    
    def run(self):
        self.window.mainloop()

def main():
    try:
        app = AdvancedIPFinder()
        app.run()
    except KeyboardInterrupt:
        print("\nApplication closed by the user")
    except Exception as e:
        print(f"Application startup error: {e}")

if __name__ == "__main__":
    main()