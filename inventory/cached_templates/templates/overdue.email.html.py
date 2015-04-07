# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428132115.813963
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/overdue.email.html'
_template_uri = 'overdue.email.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


import homepage.models as hmod 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n')
        __M_writer('\r\n<html>\r\n<head>\r\n\t<title>Email</title>\r\n</head>\r\n<body>\r\n\r\n<p>Dear Valued Customer,</p>\r\n\r\n<p>You have an overdue item. It has been more than 30 days since you rented it.\r\nPlease return it soon, or else.\r\n</p>\r\n\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 2, "24": 2, "18": 0, "30": 24, "23": 1}, "uri": "overdue.email.html", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/overdue.email.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
