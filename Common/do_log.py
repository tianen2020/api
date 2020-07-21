#!/usr/bin/env python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 21:22
# @Author  : 蒲天恩
# @File    : do_log.py
"""
logging配置
"""
import os
import logging.config
import time
log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red',
}
# 定义三种日志输出格式 开始

standard_format ='[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'
# 定义日志输出格式 结束
logfile_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # log文件的目录
time_data = time.strftime("%Y-%m-%d")
logfile_name = f"{time_data}.log"
# log文件的全路径
logfile_path = os.path.join(logfile_dir,"Log")

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(logfile_path):
    os.mkdir(logfile_path)
real_path = os.path.join(logfile_path,logfile_name)

# log配置字典
LOGGING_DIC = {
    'version': 1,  # 版本号
    'disable_existing_loggers': False,  #固定写法
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': id_simple_format
        },
    },
    # 过滤
    'filters': {},
    # 文件句柄（屏幕和文件）
    'handlers': {
        #打印到终端的日志
        # 创建屏幕句柄
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #创建文件句柄
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件配置轮转文件
            'formatter': 'standard',
            'filename': real_path,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M1024*1024*5
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        '': {
            # 2个文件句柄，屏幕句柄加入到logger中
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'INFO',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}
def load_my_logging_cfg(mode):
    logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
    logger = logging.getLogger(mode)  # 生成一个log实例  创建一个日志收集器名字为__name__
    return logger
# if __name__ == '__main__':
#     load_my_logging_cfg("登录")
