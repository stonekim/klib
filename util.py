# -*- coding:utf-8 -*-  

import logging
import os
import sys
import socket
import subprocess
import urllib,urllib2

class HttpService(object):
    """
    http工具类，支持get post 以及上传文件
    """
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def post(self, url, params):
        """
        post函数
        args:
            url,请求的url
            parame,请求参数，支持dict 以及tuple
        return:
            content,返回的文本内容
            status,请求成功与否
        """
        return self.__service(url, params)

    def get(self, url):
        """
        gey函数
        args:
            url,请求的url
        return:
            content,返回的文本内容
            status,请求成功与否
        """
        return self.__service(url)

    def __service(self, url, params=None, timeout=50):
        old_timeout = socket.getdefaulttimeout()
        socket.setdefaulttimeout(timeout)
        try:
            # POST
            if params:
                self.logger.debug('post %s params[%s]' % (url, params))
                request = urllib2.Request(url, urllib.urlencode(params))
            # GET
            else:
                self.logger.debug('get %s params[%s]' % (url, params))
                request = urllib2.Request(url)
            request.add_header('Accept-Language', 'zh-cn')
            response = urllib2.urlopen(request)
            content = response.read()
            response.close()
            self.logger.debug('content->%s, code->%d'
                              % (content, response.code))
            if response.code == 200:
                return content, True
            return content, False
        except Exception as ex:
            return str(ex), False
        finally:
            socket.setdefaulttimeout(old_timeout)

def run_shell(command,
              useshell=True,
              universal_newlines=True,
              env=os.environ):  # PY016
    """
    执行本地系统命令函数
    args:
        command,执行命令list
        universal_newlines, if True: 各种换行符统一换成: \n
        useshell,  if True: /bin/sh -c command
        env,环境变量
    return:
        returncode,进程退出状态码
        output,标准输出
        errout,错误输出
    """
    try:
        p = subprocess.Popen(command,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          shell=useshell,
                          universal_newlines=universal_newlines,
                          env=env)
        output, errout = p.communicate()
        return p.returncode, output, errout
    except:
        return -1, None, None


if __name__ == "__main__":
    ''' test run_shell '''
    #useshell = sys.platform.startswith("win")
    #status, output, errout = run_shell("ls /proc/ | grep '12'", useshell=useshell) 
    #print status
    #print output

    ''' test HttpService '''
    #h = HttpService() 
    #get_url = "http://music.baidu.com"
    #content,status = h.get(get_url)
    #print status
    #print content

