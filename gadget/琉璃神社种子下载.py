from requests import get
from re import findall
from time import sleep


def get_pages():  # 获取动漫资源的页数
    from_url = 'http://www.llss.at/wp/category/all/anime/'
    res_get = get(from_url)
    res = findall(r'>第 1 页，共 ([1-9]\d+) 页</span>', res_get.text)
    return int(res[0])


def download(each_url):  # 获取每一个资源的磁力链
    url_text = get(each_url).text
    res_magnet = findall(r'([0-9a-fA-F]{40})', url_text)  # 可能有多个
    magnet_set = set(res_magnet)  # 使用set去重
    res_title = findall(r'<h1 class="entry-title">(.*?)</h1>', url_text)  # 唯一的

    with open('23,24,22.txt', 'a+', encoding='utf-8') as f:
        if res_title is not None:
            f.write(res_title[0] + ':\n')
            print(res_title[0])
            for each in magnet_set:
                f.write('        magnet:?xt=urn:btih:' + each + '\n')
                print(each)
        else:
            print('[!]Cannot find magnet links! Skip it!')
            return


def visit_each_page(pages):  # 进入每一个页面找资源
    try:
        root_url = 'http://www.llss.at/wp/category/all/anime/page/'
        for i in range(23, 25):
            print('[*]Now in page %d' % i)
            now_url = root_url + str(i) + '/'
            now_page_text = get(now_url).text
            # now_res = findall('href="(http://www.llss.at/wp/all/anime/.*?more.*?)"', now_page_text)
            now_res = findall(r'<h1 class="entry-title"><a href="(.*?)".*?</a>', now_page_text)
            if now_res != None:
                for each in now_res:
                    print("startDownload")
                    download(each)
                    print("endDownload")
                    #print('[*]sleep for 2s')
                    #sleep(2)
    except:
        exit('[!]Oh no!!! Something wrong has happened!\n[!]May be the website has been changed ?')


if __name__ == "__main__":
    print("main")
    pages = get_pages()
    print("getPages")
    visit_each_page(pages)
    print("end")
