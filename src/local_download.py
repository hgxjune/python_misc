# -*- coding: UTF-8 -*-
###-----------------------------------------------------------------------------
## @doc main 
## @author hgx <hgx@live.cn>
## @copyright 2024 hgx, All rights reserved.
## @since 2024-09-20 18:07:03 
###-----------------------------------------------------------------------------

import io
import os
import wx
import qrcode
import threading
import socket
import socketserver
import http.server

################################################################################
### 网络
class FileDownloadHandler(http.server.BaseHTTPRequestHandler):
    def __init__(self, request, client_addr, server):
        self.base_path = server.base_path
        super().__init__(request, client_addr, server)

    def do_GET(self):
        # 获取请求的文件路径
        file_path = self.base_path

        # 检查文件是否存在
        if not os.path.isfile(file_path):
            self.send_error(404, "文件不存在")
            return

        # 设置响应头
        self.send_response(200)
        self.send_header("Content-type", "application/octet-stream")
        self.send_header("Content-Disposition", f"attachment; filename={os.path.basename(file_path)}")
        self.end_headers()

        # 发送文件内容
        with open(file_path, "rb") as file:
            self.wfile.write(file.read())

def run_server(port=8080, base_path=''):
    class CustomTCPServer(socketserver.TCPServer):
        def __init__(self, server_address, RequestHandlerClass, base_path=''):
            self.base_path = base_path
            super().__init__(server_address, RequestHandlerClass)

    global server
    server = CustomTCPServer(("", port), FileDownloadHandler, base_path=base_path)
    server.serve_forever()

def start_server_in_thread(base_path=''):
    global thread
    ip = getIp()
    port = getPort()
    thread = threading.Thread(target=run_server, args=(port, base_path,))
    thread.start()
    return 'http://' + ip + ':' + str(port) + '/download/' + os.path.basename(base_path) 

def stop_server_in_thread():
    global thread
    global server
    if 'thread' in globals() and thread is not None :
        server.shutdown()
        server.server_close()
        thread.join()
        thread = None

def getIp():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip

def getPort():
    for port in range(8000, 65535):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('0.0.0.0', port))
                s.close()
                return port
            except OSError:
                continue


################################################################################
### UI
class DownForm(wx.Frame):
    def __init__(self, parent=None, title=None, size=(300, 300)):
        wx.Frame.__init__(self, parent=parent, title=title, size=size)
        # self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        # 标签居中
        self.panel = wx.Panel(self)
        self.label = wx.StaticText(self.panel, label='拖拽文件到此处', style = wx.ALIGN_CENTER)
        self.label.SetFont(wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.label, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL)
        self.panel.SetSizer(self.sizer)
        self.panel.SetDropTarget(FileDropTarget(self))
        # wx.CallAfter(self.Bind, wx.EVT_KEY_DOWN, self.OnKeyDown)

    def createQr(self, path):
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2)
        qr.add_data(path)
        qr.make(fit=True)
        image = qr.make_image(fill_color="black", back_color="white")
        image = image.resize((300, 300))
        image_stream = io.BytesIO()
        image.save(image_stream, format='PNG')
        image_stream.seek(0)
        return image_stream

    def OnChoseFile(self, path):
        print(path)
        url = start_server_in_thread(path)
        print(url)
        stream = self.createQr(url)
        bitmap = wx.Image(stream)
        image = wx.StaticBitmap(self.panel, wx.ID_ANY, bitmap)
        self.label.Show(False)
        self.SetTitle('请扫码下载')
        self.sizer.Clear()
        self.sizer.Add(image, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL)

    def OnKeyDown(self, event):
        keycode = event.GetKeyCode()
        print(keycode)
        if keycode == wx.WXK_ESCAPE:
            self.Close()
        else:
            event.Skip()


class FileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window
    
    def OnDropFiles(self, x, y, filenames):
        self.window.OnChoseFile(filenames[0])
        return True



class App(wx.App):
    def OnInit(self):
        self.frame = DownForm(None, title='选择文件', size=(320, 340))
        self.frame.Center()
        self.frame.Show()
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeykDown)

        return True
    
    def OnExit(self):
        stop_server_in_thread()
        return 0

    def OnKeykDown(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_ESCAPE:
            self.ExitMainLoop()
        else:
            event.Skip()


################################################################################
def main():
    app = App()
    app.MainLoop()



if __name__ == '__main__':
    print('--', __file__)
    main()

