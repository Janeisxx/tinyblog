1.开发环境:Django(1.11.9)+python(3.6),数据库使用Django自带的sqlite
2.项目是一个简单的个人博客,访问首页的地址,运行后--> 本机ip:8000/index
3.页面主要包括博文首页和详情页
4.项目主要包括blogs,comments,users三部分
5.实现了分类,高亮搜索(whoosh引擎,结巴分词),分页(Paginator),RSS订阅等功能
6.实现了评论功能(comments--app)
7.实现了用户登录,注销,改密等功能(users---app)
8.具体的功能很多都在代码注释
9.应用了haystacks搜索,markdown编辑,自定义模板标签(templatetags),通用视图类,modelForm等进阶功能
10.目前还存在一些问题,如只能用markdown语法编辑,归档没有分页等等,找密码邮件只是发到Django后台.需进一步解决.