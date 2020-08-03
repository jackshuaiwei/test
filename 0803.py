import requests
from lxml import etree

def get_page_num(keywords=""):
    url = "https://www.amazon.de/s?k={}+&page=1".format(keywords)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }
    cookie = "session-id=258-6720872-4175233; i18n-prefs=EUR; ubid-acbde=259-9310800-1550847; session-token='8k5T3RJzWzLy74n6eVALpZMkxfQAc2wQKyKIjekU24adphDriYoWHJT/YAt/QTrjzYmmm0t4/zsm5XSQ/o/EEbu58SeiP5LNLAFTVHcBiJY8J52iEBW0JdrWIVeu3HcLBHT3XplO/AP7rzmuRVoBSAe5+qF7KgCh2wx06zf2srQiphdmf+VkiTiUAw5kQrDI9kbqcUn6TGWINM5+n7/0B6eeErsO4UEh3wH9BF+V+qs='; x-acbde='m?Gj?s71CFvsopyj2F64FYdAn793rsB0R8uEza8oYxd2cyNvRY4lQW4blEOVYD7Z'; at-acbde=Atza|IwEBIL7x-bQQJBVy22L7cA4aQaKzaJfJRZNtq-6s5VXaldzYcQ01cVM6CEP2rseAubrCqtQVIipe-o-kOpi50UEiLb6DYqo6hm6yvgFLFdGegV_jJ1F7S25Kdu2wnrMYXe4Kn6O6sQkPOBfJSn04MlLT98EVKjroIbo91a5inTm5ceeOfQyDIN6CnZ0BTqMn1H-At5MeNplBa5oycybwXU3h8ZiO; sess-at-acbde='AKEE+awDQjDEL/JxQafHVPE4Z2eyvT7z8X8AJ5lnAdM='; sst-acbde=Sst1|PQErzYGOxZWPAkWIL6qkM27qC_MQ8w2PpTwC6f5oyR2NBEhaonqQu5_7K6jicZ5yOWOT_p3LJ54obedHevRqHq_MKmSVL6X5VoFXOiDMOgb_XCICwruwZkU0Vk9CXeZV31uzV1xWu9qoMx_wZ7fFqYs7IqlIIxw-faAdQG369Z7B4qY0FXM4lgyKoTkR65WEceb4_zV9h2JuOfMxxB8f80PJBEPlcixpw-fkVcenrka1Bm2By6ESAO5Q5a1dpBzZxeK9Yy-Dezynf_JlKEU_J9lSK5TbqeXCHp7Gq_5XeUKPwnXHzRfLBQYjihZ3GwkAjA3udM0iTbnKEVnUB5o1MtXsYA; x-wl-uid=1mgHnbPDbuh7H2ObkZ3sT62aHVqLLWdtmn738cJKQtPtRJ9XTCiEToB6uHx34d2xQPHTx9W0ucdskw5qyv1wzm+TmQywUoUBZq4rjObcHX6axhQFQY9jsMVVLzoWn7SqC2Oj+jo41AmI=; session-id-time=2082754801l; csm-hit=tb:s-ZYE7T0TDPJN331AY22BB|1596462854926&t:1596462856628&adb:adblk_no"
    cookies = {}
    for i in cookie.split("; "):
        cookies[i.split("=")[0]] = i.split("=")[1]

    response = requests.get(url, headers=headers, verify=False, cookies=cookies)
    html = etree.HTML(response.content.decode())
    total_num = html.xpath("//li[@class='a-disabled']/text()")[-1]
    return int(total_num)


def amazon(keywords,page_num):
    url = "https://www.amazon.de/s?k=Negligee+Nachtwäsche+Sexy+Nachthemd+&page={}".format(page_num)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }
    cookie = "session-id=258-6720872-4175233; i18n-prefs=EUR; ubid-acbde=259-9310800-1550847; session-token='8k5T3RJzWzLy74n6eVALpZMkxfQAc2wQKyKIjekU24adphDriYoWHJT/YAt/QTrjzYmmm0t4/zsm5XSQ/o/EEbu58SeiP5LNLAFTVHcBiJY8J52iEBW0JdrWIVeu3HcLBHT3XplO/AP7rzmuRVoBSAe5+qF7KgCh2wx06zf2srQiphdmf+VkiTiUAw5kQrDI9kbqcUn6TGWINM5+n7/0B6eeErsO4UEh3wH9BF+V+qs='; x-acbde='m?Gj?s71CFvsopyj2F64FYdAn793rsB0R8uEza8oYxd2cyNvRY4lQW4blEOVYD7Z'; at-acbde=Atza|IwEBIL7x-bQQJBVy22L7cA4aQaKzaJfJRZNtq-6s5VXaldzYcQ01cVM6CEP2rseAubrCqtQVIipe-o-kOpi50UEiLb6DYqo6hm6yvgFLFdGegV_jJ1F7S25Kdu2wnrMYXe4Kn6O6sQkPOBfJSn04MlLT98EVKjroIbo91a5inTm5ceeOfQyDIN6CnZ0BTqMn1H-At5MeNplBa5oycybwXU3h8ZiO; sess-at-acbde='AKEE+awDQjDEL/JxQafHVPE4Z2eyvT7z8X8AJ5lnAdM='; sst-acbde=Sst1|PQErzYGOxZWPAkWIL6qkM27qC_MQ8w2PpTwC6f5oyR2NBEhaonqQu5_7K6jicZ5yOWOT_p3LJ54obedHevRqHq_MKmSVL6X5VoFXOiDMOgb_XCICwruwZkU0Vk9CXeZV31uzV1xWu9qoMx_wZ7fFqYs7IqlIIxw-faAdQG369Z7B4qY0FXM4lgyKoTkR65WEceb4_zV9h2JuOfMxxB8f80PJBEPlcixpw-fkVcenrka1Bm2By6ESAO5Q5a1dpBzZxeK9Yy-Dezynf_JlKEU_J9lSK5TbqeXCHp7Gq_5XeUKPwnXHzRfLBQYjihZ3GwkAjA3udM0iTbnKEVnUB5o1MtXsYA; x-wl-uid=1mgHnbPDbuh7H2ObkZ3sT62aHVqLLWdtmn738cJKQtPtRJ9XTCiEToB6uHx34d2xQPHTx9W0ucdskw5qyv1wzm+TmQywUoUBZq4rjObcHX6axhQFQY9jsMVVLzoWn7SqC2Oj+jo41AmI=; session-id-time=2082754801l; csm-hit=tb:s-ZYE7T0TDPJN331AY22BB|1596462854926&t:1596462856628&adb:adblk_no"
    cookies = {}
    for i in cookie.split("; "):
        cookies[i.split("=")[0]] = i.split("=")[1]

    response = requests.get(url, headers=headers, verify=False, cookies=cookies)
    html = etree.HTML(response.content.decode())
    title_list = html.xpath("//h5[@class='s-line-clamp-1']/span/text()")
    detail_list = html.xpath("//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']/a/span/text()")
    count = len(title_list)
    content = []
    for i in range(0, count):
        content.append([title_list[i], detail_list[i]])
    # with open("a.html", "w", encoding="utf-8") as f:
    #     f.write(response.content.decode())
    title = "untlet"
    detail = "Negligee Nachtwäsche Sexy Nachthemd Damen Chemise Dessous Babydoll Tiefer V-Ausschnitt Spitze Lingerie Nachtkleid Sleepwear"

    for i in content:
        if i[0] == title:
            if i[1] == detail:
                return page_num
    return 0


keywords = "Negligee,Nachtwäsche,Sexy,Nachthemd"
keywords = keywords.replace(",","+")

total_num = get_page_num(keywords)
page_list = []
for i in range(1,total_num+1):
    re = amazon(keywords,i)
    if re != 0:
        page_list.append(i)



print(page_list)
