import webbrowser
import re

def is_valid_url(url):
    # 匹配包含至少一个点的字符串，允许各种协议或无协议
    pattern = r'^(https?:\/\/)?[\w\-]+(\.[\w\-]+)+[/#?]?.*$'
    return re.match(pattern, url) is not None

def read_last_valid_url(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in reversed(lines):
                url = line.strip()
                if url and is_valid_url(url):
                    return url
                elif url:
                    print(f"忽略无效 URL: {url}")
            print("文件中没有找到有效的 URL")
            return None
    except FileNotFoundError:
        print(f"找不到文件：{file_path}")
        return None
    except Exception as e:
        print(f"读取文件时出错：{str(e)}")
        return None

def visit_url(url):
    try:
        # 如果 URL 没有协议，添加 http://
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        webbrowser.open(url)
        print(f"已在默认浏览器中打开 {url}")
    except Exception as e:
        print(f"打开 {url} 失败：{str(e)}")

def visit_last_valid_url_from_file(file_path):
    url = read_last_valid_url(file_path)
    if url:
        visit_url(url)
    else:
        print("没有找到有效的 URL 可以访问")

# 使用示例
file_path = 'url.txt'  # 替换为您的文本文件路径
visit_last_valid_url_from_file(file_path)
