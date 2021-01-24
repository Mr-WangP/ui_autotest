# coding=utf-8
from poium import Page, NewPageElement


class BlogPage(Page):
    login_element = NewPageElement(xpath="//*[@id='navbar_login_status']/a[4]", describe='登录按钮', index=0, timeout=3)
    regist_element = NewPageElement(xpath="//*[@id='navbar_login_status']/a[3]", describe='登录按钮')
    home_element = NewPageElement(xpath="//*[@id='nav_left']/li[2]/a", describe='首页')
    news_element = NewPageElement(xpath="//*[@id='nav_left']/li[3]/a", describe='新闻')
    # ...
    find_element = NewPageElement(xpath="//*[@id='nav_left']/li[9]/div[1]/a", describe='发现')
    yuanzi_element = NewPageElement(xpath="//*[@id='nav_left']/li[9]/div[2]/a[1]", describe='园子')
    shoucang_element = NewPageElement(xpath="//*[@id='nav_left']/li[9]/div[2]/a[3]", describe='收藏')
    # ...
    jinghua_element = NewPageElement(xpath="//*[@id='sidenav_pick']/a/span", describe='精华')
    dingyue_element = NewPageElement(xpath="//*[@id='sidenav_subscription']/a/span", describe='订阅')
    more_element = NewPageElement(xpath="//*[@id='sidenav_more']/div[1]/a/span", describe='更多')
    all_blogs_element = NewPageElement(xpath="//*[@id='sidenav_more']/div[2]/a[1]", describe='所有随笔')
    # ...
    login_title_element = NewPageElement(xpath="//div[text()='博客园用户登录']", describe='博客园客户登录')
