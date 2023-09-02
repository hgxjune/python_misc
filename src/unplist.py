#!/usr/bin/python
# -*- coding: UTF-8 -*-
import plistlib
import os
import sys
import shutil
from PIL import Image

# PIL 安装： pip install pillow

def export_image(img, pathname, item):
    # 去透明后的子图矩形
    x, y, w, h = tuple(map(int, item['frame']))
    # 子图原始大小
    size = tuple(map(int, item['sourceSize']))
    # 子图在原始图片中的偏移
    ox, oy, _, _ = tuple(map(int, item['sourceColorRect']))

    # 获取子图左上角，右下角
    if item['rotated']:
        box = (x, y, x + h, y + w)
    else:
        box = (x, y, x + w, y + h)

    # 使用原始大小创建图像，全透明
    image = Image.new('RGBA', size, (0, 0, 0, 0))
    # 从图集中裁剪出子图
    sprite = img.crop(box)

    # rotated纹理旋转90度
    if item['rotated']:
        sprite = sprite.transpose(Image.ROTATE_90)

    # 粘贴子图，设置偏移
    image.paste(sprite, (ox, oy))

    # 保存到文件
    print('保存文件：%s' % pathname)
    image.save(pathname, 'png')

# 获取 frame 参数
def get_frame(frame):
    result = {}
    if frame['frame']:
        result['frame'] = frame['frame'].replace('}', '').replace('{', '').split(',')
        result['sourceSize'] = frame['sourceSize'].replace('}', '').replace('{', '').split(',')
        result['sourceColorRect'] = frame['sourceColorRect'].replace('}', '').replace('{', '').split(',')
        result['rotated'] = frame['rotated']
    return result

# 生成图片
def gen_image(file_name, export_path):
    # 检查文件是否存在
    plist = file_name + '.plist'
    if not os.path.exists(plist):
        print('plist文件【%s】不存在！请检查' % plist)
        return

    png = file_name + '.png'
    if not os.path.exists(png):
        print('png文件【%s】不存在！请检查' % plist)
        return

    # 检查导出目录
    if not os.path.exists(export_path):
        try:
            os.mkdir(export_path)
        except Exception as e:
            print(e)
            return

    # 使用plistlib库加载 plist 文件
    lp = plistlib.load(open(plist, 'rb'))
    # 加载 png 图片文件
    img = Image.open(file_name + '.png')

    # 读取所有小图数据
    frames = lp['frames']
    for key in frames:
        item = get_frame(frames[key])
        export_image(img, os.path.join(export_path, key), item)



# 遍历目录
def transform_folder(source, dest):
    if not os.path.exists(source):
        print('源目录不存在: %s' % source)
        return
    if not os.path.exists(dest):
        print('目的目录不存在: %s' % root)
        pass
    transform(source, dest)


# 递归遍历，解压 plist 到 name.plist 文件夹，且 copy 所有 png 文件
def transform(source, dest):
    clear_file = []
    for name in os.listdir(source):
        path_from = source + "/" + name
        path_dest = dest + "/" + name

        if os.path.isdir(path_from):
            if not os.path.exists(path_dest):
                os.mkdir(path_dest)
            transform(path_from, path_dest)
        elif name.endswith('.plist'):
            gen_image(path_from.split(".")[0], path_dest)
            clear_file.append(path_dest.split(".")[0] + ".png")
        elif name.endswith('.png'):
            shutil.copy(path_from, path_dest)

    for f in clear_file:
        if os.path.exists(f):
            print('删除文件：%s' % f)
            os.remove(f)

    pass


# 只遍历当前目录，直接在当前目录生成子目录
def transform_one(root):
    if not os.path.exists(root):
        print('目录不存在: %s' % root)
        return
    for rt, ds, fs in os.walk(root):
        for f in fs:
            if f.endswith('.plist'):
                path = root+"/"+f.split(".")[0]
                gen_image(path, path)



if __name__ == '__main__':
    source = "F:/from"
    dest   = "F:/to"
    transform_folder(source, dest)
