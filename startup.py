import StringIO

__author__ = 'zhangfuming'

import sys
sys.path.append('configs')

def main(avgs):
    script = avgs[1]
    type = 'stdout'
    env = 'dev'
    try:
        env = avgs[2]
    except:
        pass
    try:
        type = avgs[3]
    except:
        pass
    api_module = __import__(script)
    apis = api_module.apis
    #create curl service
    from service import curl_service
    curlService = curl_service.CurlService()
    result = StringIO.StringIO()
    result.write("\r\n")
    result.write("="*100)
    result.write("\r\n")
    result.write(("%s (%s)\r\n") % (apis['desc'],env))
    result.write("="*100)
    result.write("\r\n")
    for item in apis['list']:
        #print item['url'],'   ',item['method']
        color=32
        if item['method'].upper() == 'GET':
            response = curlService.get(item,env)
            s = StringIO.StringIO()
            if type == 'stdout':
                if response['http_status'] == 200:
                    color=32
                else:
                    color=31
                s.write(("API Name:\033[%dm%s\033[0m\r\n") % (color,item['desc']))
                s.write(("Http Status:\033[%dm%s\033[0m\r\n") % (color,response['http_status']))
                s.write(("Content-type: \033[%dm%s\033[0m\r\n") % (color,response['content_type']))
                s.write(("Effective-Url: \033[%dm%s\033[0m\r\n")%(color,response['effective_url']))
                s.write(("Method: \033[%dm%s\033[0m\r\n")%(color,item['method']))
                s.write(("Response: \033[%dm%s\033[0m\r\n") %(color,response['response']))
                print s.getvalue()
            else:
                s.write(("API Name:%s\r\n") % (item['desc']))
                s.write(("Http Status:%s\r\n") % (response['http_status']))
                s.write(("Content-type:%s\r\n") % (response['content_type']))
                s.write(("Effective-Url:%s\r\n")%(response['effective_url']))
                s.write(("Method:%s\r\n")%(item['method']))
                s.write(("Response:%s\r\n") %(response['response']))
            result.write(s.getvalue())
            result.write("-"*50)
            result.write("\r\n")
            #print ("Http Status:\033[%dm%s\033[0m") % (color,item['desc'])
            #print ("Http Status:\033[%dm%s\033[0m") % (color,response['http_status'])
            #print ("Content-type: \033[%dm%s\033[0m") % (color,response['content_type'])
            #print ("Effective-Url: \033[%dm%s\033[0m")%(color,response['effective_url'])
            #print ("Response: \033[%dm%s\033[0m") %(color,response['response'])
        elif item['method'].upper() == 'POST':
            response = curlService.post(item,env)
            if type == 'stdout':
                if response['http_status'] == 200:
                    color=32
                else:
                    color=31
                s = StringIO.StringIO()
                s.write(("API Name:\033[%dm%s\033[0m\r\n") % (color,item['desc']))
                s.write(("Http Status:\033[%dm%s\033[0m\r\n") % (color,response['http_status']))
                s.write(("Content-type: \033[%dm%s\033[0m\r\n") % (color,response['content_type']))
                s.write(("Effective-Url: \033[%dm%s\033[0m\r\n")%(color,response['effective_url']))
                s.write(("Method: \033[%dm%s\033[0m\r\n")%(color,item['method']))
                s.write(("Header: \033[%dm%s\033[0m\r\n")%(color,item['header']))
                s.write(("Params: \033[%dm%s\033[0m\r\n")%(color,item['params']))
                s.write(("Response: \033[%dm%s\033[0m\r\n") %(color,response['response']))
                print s.getvalue()
            else:
                s = StringIO.StringIO()
                s.write(("API Name:%s\r\n") % (item['desc']))
                s.write(("Http Status:%s\r\n") % (response['http_status']))
                s.write(("Content-type:%s\r\n") % (response['content_type']))
                s.write(("Effective-Url:%s\r\n")%(response['effective_url']))
                s.write(("Method:%s\r\n")%(item['method']))
                s.write(("Header:%s\r\n")%(item['header']))
                s.write(("Params:%s\r\n")%(item['params']))
                s.write(("Response:%s\r\n") %(response['response']))
            result.write(s.getvalue())
            result.write("-"*50)
            result.write("\r\n")
        else:
            print 'method %s not supported!' % item['method']
    print result.getvalue()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'not config provided,run the script like [python startup.py script_name]'
    else:
        main(sys.argv)