#coding=utf-8

import unittest
import HtmlTestRunner
import time
from config import globalparam
from public.common import sendmail

def run():
    test_dir = './testcase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')

    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    reportname = globalparam.report_path + '\\' + 'TestResult' + now + '.html'
    with open(reportname,'w') as f:
        runner = HtmlTestRunner.HTMLTestRunner(
            stream=f,
            report_title='Case Test Report',
            descriptions='Test the import testcase'
        )
        runner.run(suite)
    time.sleep(3)

    #sendMail() #邮件暂时不发送，后续根据配置决定
# 发送邮件
def sendMail():
    mail = sendmail.SendMail()
    mail.send()

if __name__=='__main__':
    run()