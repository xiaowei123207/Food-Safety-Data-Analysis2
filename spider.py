import requests
from bs4 import BeautifulSoup
import csv

# 1. 设定目标网址
url = "http://quotes.toscrape.com/"
# 加上请求头，假装我们是浏览器，避免被网站拦截
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

print("正在请求网页...")
# 2. 发送请求获取网页内容
response = requests.get(url, headers=headers)

# 3. 用 BeautifulSoup 解析网页
soup = BeautifulSoup(response.text, "html.parser")
# 找到所有包含名言的代码块
quotes = soup.find_all("div", class_="quote")

print(f"找到 {len(quotes)} 条名言，开始提取数据...")

# 4. 把提取到的数据保存为 CSV 文件
with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # 写入表头
    writer.writerow(["名言", "作者"])
    
    # 遍历提取每一条名言和作者
    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text
        writer.writerow([text, author])
        print(f"已抓取：{text[:20]}... - {author}")

print("🎉 抓取完成！已保存到 quotes.csv 文件。")