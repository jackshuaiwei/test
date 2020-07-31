#coding=utf-8
import requests
import pandas as pd
from lxml import etree
import re
import time
import xlwt
import redis


class SB:
    def __init__(self, cookies,filename,redis):
        self.redis = redis
        self.filename = filename
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
        }
        self.cookies = cookies
        self.url = "https://www.amazon.com/s?i=aps&k={}"

    def mycookies(self, cookies):
        cookies = {}
        for i in cookie.split("; "):
            cookies[i.split("=")[0]] = i.split("=")[1]
        return cookies

    def myexcel(self, filename):
        df = pd.read_excel(filename)
        excel_header = df.columns.tolist()
        all_data = []
        rows,columns = df.shape
        for i in range (0,columns,2):
            data = df.iloc[:, i]
            all_data.append(data)
        self.redis.set('total',"总共需要抓取{}列数据".format(columns))
        return all_data,excel_header,columns

    def myrequest(self, keyword, cookies):
        url = self.url.format(keyword)
        response = requests.get(url, headers=self.headers, cookies=cookies, verify=False)
        html = etree.HTML(response.content.decode())
        content = html.xpath("//div[@class='sg-col-inner']/div/span[1]/text()")[0]
        content_t = content.split(" ")[-3]
        res = "".join(re.findall(r'\d+', content_t))
        return res

    def get_result(self, all_data):
        cookies = self.mycookies(self.cookies)
        rt_data = []
        num = 0
        for i in all_data:
            r_data = []
            for j in i:
                result_num = self.myrequest(j,cookies)
                r_data.append(result_num)
            rt_data.append(r_data)
            print("已经爬取完第{}列（从零开始计算）".format(num))
            self.redis.set("done_num","已经爬取完第{}列（从零开始计算）".format(num))
            num = num + 1
            time.sleep(0.5)
        return rt_data

    def save_excel(self, num, data, sheet):
        lennum = len(data)
        for i in range(0, lennum):
            sheet.write(i + 1, num, data[i])

    def run(self):
        all_data,excel_header,columns = self.myexcel(self.filename)
        res = self.get_result(all_data)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet("sb1", cell_overwrite_ok=True)
        for i in range(0,columns):
            sheet.write(0, i, excel_header[i])
            if i % 2 == 0:
                k = int(i/2)
                for j in range(0,len(all_data[k])):
                    sheet.write(j+1, i, all_data[k][j])
            else:
                k = int(i/2)
                for j in range(0,len(all_data[k])):
                    sheet.write(j+1, i, int(res[k][j]))

        # sheet.write(0, 0, "sleepwear")
        # sheet.write(0, 1, "搜索量")
        # sheet.write(0, 2, "pajamas")
        # sheet.write(0, 3, "搜索量")
        # sheet.write(0, 4, "PJs")
        # sheet.write(0, 5, "搜索量")
        # len_all_data = len(all_data)
        # len_res = len(res)
        # num = 0
        # for i in range(0, len_all_data):
        #     self.save_excel(num, all_data[i], sheet)
        #     num += 2
        # num = 1
        # for i in range(0, len_res):
        #     self.save_excel(num, res[i], sheet)
        #     num += 2
        workbook.save("sb.xls")
        self.redis.set("save_name","sb.xls")


if __name__ == "__main__":
    print("开始执行爬取程序")
    red = redis.Redis(host="localhost",port="6379",decode_responses=True)
    while(True):
        cookie = red.get('ama_cookie')
        filename = red.get('filename')
        if cookie and filename:
            print("成功获取cookie和filename")
            break
            
        else:
            print("正在获取cookie,filename...")
            time.sleep(2)
    cookie = "aws-priv=eyJ2IjoxLCJldSI6MCwic3QiOjB9; aws-target-static-id=1568633319305-29341; aws-target-data=%7B%22support%22%3A%221%22%7D; s_fid=5D5D1DE2D1E5528B-252434A2BA596A84; s_vn=1600169319827%26vn%3D1; regStatus=pre-register; aws-target-visitor-id=1568633319310-674099.22_12; session-id=138-5356623-1716963; sp-cdn='L5Z9:HK'; ubid-main=135-2218941-3321818; skin=noskin; x-wl-uid=1X32WI6UEswFhtB2T6WmUR5s7n0l0u8kEyvnf9ulj/yN0gV160KKwMJRCH5eoIoRsTS+rYYXlEbYHQ2nUZtp8mIo7DYQaM82ouuGeXLN/JuYN+4bm/AmUlDxxcUbWBJZ97Euo5sy0PtE=; session-token=bHQtqe5u/yHLSuQ5fTGnE14EbQBQX8FcZ5dS0/XZ576U/l5zquWRiiolNpUOvdKpYAdnyPhQqwe1xZhLSwEYFgzsVNMNnVf5AhBWJfkHiweanw42RIG7+MweT7IjK9kuGAAn4olga8TRocMv/TapCYtnP8zmNLt8dBdcjN3ZUhsseItQKLZkawVAbQPvd59PwaU1gakzmHyWmoe0hmaeU7k1u59ct561f05fI0NJSVV7UqRWL/Jx4ncRK5VsuG0O3zDiccxw5L5ndtMmvkZLDeM9xIprALSB; x-main='CWde7C2vo3DWlJgS1ubgeB3NmQrJ6fPhQdgZnalm90A0d16NZN46pOqukIt632E?'; at-main=Atza|IwEBIFKHiBdQ8bVX2dSviTMU0YmjvckMgHGs3K5kDzYJ9URIwigJ5FEtU-PdCYl00mRqB_QRwbMvxRSxLC21GUS3gMdqF6I3YUAPdgeJMmffzH9Q91mS6aTH_ao4pXXIN-Udmgrk-a6lVMYTUeAfpzhuk7rK3wsJJa8F1NyQDz1_QriV04whEY---FsjXO1il41_yOYFCEnCsGwugHCUw3IiY7H2; sess-at-main='BermSdhULR3/pPeHEqTTCZBB/vMVrMt2aF+deEV9xvA='; sst-main=Sst1|PQGhvtZbQbYwX4uD0fgNCpHxCxsiksjfnu92xiX4a17jVtQ7HcZpwCfVkXaHABm3lkEq4Z9HuNO_jy-Q9OUo4ekXn8b8Eb4JBXyK7Z4R-osJ2MjpqCPJOb5t7g2Ri8HO-XYC7oa8H-t520BKEe462isHZWxPOCUlrL1NcoSMjr0-F4pN65D0vWjeXPwaIgKs0vw-JjE_UKQayFi1Cq3BWPkFLtnVx06xin_VJw6sLmwk_wl68p2kI8fr9fdB4y0rup34iuIZ2EFSw6iYYcZq-It902aMzWGCRnC1ee650lyhV8G_bKs5yhH87zLZ2Q1Y3-6p92ZY8S8pR6pvyOuTGoKeCw; lc-main=en_US; session-id-time=2082787201l; i18n-prefs=USD; csm-hit=tb:BN1QS6AN11G0SA6KTV8V+s-A0T84Y7T9CHQ0G6M2V3E|1596116454663&t:1596116454663&adb:adblk_no"
    sb = SB(cookie,filename,red)
    sb.run()


