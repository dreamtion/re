#!/usr/local/bin/python3
import re
import os
import time
from urllib.request import Request, urlopen
import urllib
import cgi, cgitb
from multiprocessing.pool import ThreadPool

start_time=time.time()




def get_title(url):
    content=get_content(url)
    pattern= re.compile(r'<title>.*?</title>')
    match=pattern.search(content)
    title=match.group()[7:-29]
    return (title)

def get_filename(image_link):
    try:
        filename=image_link.split("/")[-1]
        return filename;
    except:
        match = None



def get_content(site):
    hdr = {'User-Agent': 'Mozilla/5.0','Cookie':'nw=session'}
    req = Request(site, headers=hdr)
    content = urlopen(req).read().decode('utf-8')
    return content;

def get_image_page(img_num,num,site):
    match='init'
    image_page_link='init'
    while (match):
        try:
            pattern = re.compile(r'https://e-hentai.org/'+'\S'+'/\S\S\S\S\S\S\S\S\S\S/'+str(num)+'-'+str(img_num))
            content= get_content(site)
            match=pattern.search(content)
            image_page_link=match.group()
            return image_page_link;
        except:
            match = None


def get_num(url):
    pattern = re.compile(r'\d.*?/')
    num = pattern.search(url)
    num = num.group()[:-1]
    return num;

def get_image_link(image_page):
    content=get_content(image_page)
    pattern = re.compile(r'http://\d.*?'+'\.jpg')
    match=pattern.search(content)
    image_link=match.group()
    return image_link;




def start(url):
    page_num=0
    img_num=1
    num=get_num(url)
    match='init'
    image_page='init'

    site= url+"?p="+str(page_num)
    while (image_page):
        site= url+"?p="+str(page_num)
        try:
            image_page=get_image_page(img_num,num,site)
            while (image_page==None):
                page_num=page_num+1
                site= url+"?p="+str(page_num)
                image_page=get_image_page(img_num,num,site)
                if (image_page):
                    image_page=image_page
                else: break
           # print ("%s" % image_page)
            #print ("<br \>")
            image_link=get_image_link(image_page)
            print ("%s" % image_link)
            print ("<br \>")
            #with open ('image_link.txt','a') as the_file:
                #the_file.write(image_link+'\n')


            img_num=img_num+1


        except:
            image_page= None

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
url = form.getvalue('url')
print ("Content-type: text/html\r\n\r\n")

#url=input('Please enter the site address:')
start(url)
#ThreadPool(8).imap_unordered(start(url))
end_time = time.time()

print(end_time-start_time)
# https://e-hentai.org/g/1319544/afd4c6e739/
# https://e-hentai.org/g/1413847/c2143cadf2/