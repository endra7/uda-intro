
page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="www.google.com">'''
#ver 1
'''
start_link=page.find('<a href=')
start_quote=page.find('"',start_link)
end_quote=page.find('"',start_quote+1)
url=page[start_quote+1:end_quote]
print(url)
'''

#ver 2

def get_next_target(page):
    start_link=page.find('<a href=')
    if(start_link != -1):
        start_quote=page.find('"',start_link)
        end_quote=page.find('"',start_quote+1)
        url=page[start_quote+1:end_quote]
        return url,end_quote
    else:
        return None,0
'''
def print_all_links(page):
    while True:
        url,endpos=get_next_target(page)
        if url:
            print url
            page=page[endpos:]
        else:
            break
'''

def get_all_links(page):
    links=[]
    while True:
        url,endpos=get_next_target(page)
        if url:
            links.append(url)
            page=page[endpos:]
        else:
            break
    return links

def union(primary,secondary):
    for each in secondary:
        if each not in primary:
            primary.append(each)


def crawl_web(seed_page):
    #links to be crawled
    tocrawl=[seed_page]
    #links already crawled
    crawled=[]
    while tocrawl:
        page=tocrawl.pop()
        if page not in crawled:
            union(tocrawl,get_all_links(page))
            crawled.append(page)
    return crawled
        
