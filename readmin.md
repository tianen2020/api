python+requests+unnitest+HTMLHttprunner+jenkins
# unnitest 框架分层设计目录<br>
1.TestCase 测试用例测层，编写测试用例
2.data 数据层，提供测试用例需要的数据
3.Common 逻辑处理层包含了 requests封装，日志的封装，ini文件，操作excel,读取数据库，发送邮件，os模块路径处理
4.Log 日志
5.report 测试报告
6.config 配置文件，线上配置，测试环境，全局配置（可以来进行切换线上和测试）

# requests 模块的封装
1.采用了全局的session来进行发送的请求
2.导入 import requests
# excel 读写封装
1.pip install openpyxl
2.创建excel 用workbook模块
3.打开excel使用load_workbook
4. workbook sheet cell
# 配置文件
1.采用configparser模块
2.section option value
3.配置文件：global 来控制读取不同环境的配置文件；
或者随机数据的值写入配置文件，excel用例从配置文件拿取数据；从来采用ddt数据驱动测试
或者db拿取数据
# path动态路径获取
1.采用os模块
2.获得目录的顶层目录
# 数据库的查询
import pymysql
1.连接数据库
2.建立一个查询页面游标mysql.cursor(pymysql.cursors.DictCursor)
3.编写sql
4.执行sql，（self.mysql.commit()强制执行最新的）
5.查看执行的结果
6.关闭查询，关闭数据库连接
7.数据库查询后记得进行更新数据库self.mysql.commit()强制执行最新的
# 用例中也可以写sql
if case.sql is not None:
    读取用例中的sql进行数据库的连接
# unnitest 框架工作原理
unittest中最核心的四个概念是：test case, test suite, test runner, test fixture
1.一个TestCase的实例就是一个测试用例。什么是测试用例呢？就是一个完整的测试流程，包括测试前准备环境的搭建(setUp)，执行测试代码(run)，以及测试后环境的还原(tearDown)。元测试(unit test)的本质也就在这里，一个测试用例是一个完整的测试单元，通过运行这个测试单元，可以对某一个问题进行验证。
而多个测试用例集合在一起，就是TestSuite，而且TestSuite也可以嵌套TestSuite。
2.TestLoader是用来加载TestCase到TestSuite中的，其中有几个loadTestsFrom__()方法，就是从各个地方寻找TestCase，创建它们的实例，然后add到TestSuite中，再返回一个TestSuite实例。
3.TextTestRunner是来执行测试用例的，其中的run(test)会执行TestSuite/TestCase中的run(result)方法。
4.测试的结果会保存到TextTestResult实例中，包括运行了多少测试用例，成功了多少，失败了多少等信息。
5.而对一个测试用例环境的搭建和销毁，是一个fixture。






