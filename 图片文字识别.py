from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '19517004'  
API_KEY = 'kvgz4GeHHiQikfEUHy0pVGf6'
SECRET_KEY = 'YtKuSBZAjChRvQWGkLjB8sLp857jZYo4'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filepath):
    with open(filepath,'rb') as f:
        return f.read()

def get_img_content(img):
    image_content=''
    content = client.basicAccurate(image=img)
    # print(content)
    for words in content['words_result']:
        # print(words)  # 字典
        image_content += words['words']
    print(image_content)

if __name__ == '__main__':
    img = get_file_content('G:\\Ph.D._Thesis\\Dissertation\\Collection\\安徽\\2014\\5\\5_02.png')
    get_img_content(img)