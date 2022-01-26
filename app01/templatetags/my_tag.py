from django import template

# 注册
register = template.Library()


@register.inclusion_tag('my_tag/headers.html')
def banner(menu_name):
    print(menu_name)
    img_list = [
        "/static/my/img/lunbo/1.jpg",
        "/static/my/img/lunbo/2.jpg",
        "/static/my/img/lunbo/3.jpg",
    ]
    return {"img_list": img_list}
