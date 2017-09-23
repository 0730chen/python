import requests
form bs4 import BeautifulSoup
form urllib import request
def get_html(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    html = requests.get(url,headers=headers)
    return html
def get_links(html):
    soup = BeautifulSoup(html.content,'lxml')
    result=soup.find_all('img')
    attritube='src'
    
    links=[]
    for x in result:
        links.append('http:'+x.get(attritube))
        
    return links
    
def downlaod(start,end):
    if not os.path.exists('jiandan'):
        os.makedirs('jiandan')
    for x in range(start,end):
        if not os.path.exists('jiandan\\meizitu'+str(x)):
            os.makedirs('jiandan\\meizitu'+str(x))
        url = 'http://jandan.net/ooxx/page-'+ str(x)+ '#comments'
        html = get_html(url)
        links = get_links(html)
        i = 0
        for link in links:
            filename = 'jiandan\\meizitu'+str(x)+'\\'+str(i)+'.jpg'
            with open(filename,'w'):
                try:
                    request.urlretrieve(link,filename)
                except:
                    print('获取图片%s失败'%filename)
if __name__=='__main__':
    start = int(input('请输入一个开始数: '))
    end = int(input('请输入一个结束数: '))
    assert<1<start<end<2000
    download(start,end)
    

                    
                    
                
            
            
            
        
        
        
        
            
        
    
    
        
    
    
    
    

    
