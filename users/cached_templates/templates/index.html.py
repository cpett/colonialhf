# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425590296.722658
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\users\\templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'top', 'left', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/users/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def header():
            return render_header(context._locals(__M_locals))
        def top():
            return render_top(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="header">\r\n\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="row top-header">\r\n      <div class="col-md-10 top-header"></div>\r\n      <div class="col-md-1 top-header"><a href="/homepage/login/" class="top-nav">Login</a></div>\r\n      <div class="col-md-1 top-header"><a href="SignUp" class="top-nav">Sign Up</a></div>\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="left">\r\n\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n  <div>\r\n    <button id="show_login_dialog" class="btn btn-success">Login</button>\r\n  </div>\r\n\r\n\r\n<!-- Modal -->\r\n<div class="modal fade" id="login_dialog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n  <div class="modal-dialog">\r\n    <div class="modal-content">\r\n      <div class="modal-header">\r\n        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n        <h4 class="modal-title" id="myModalLabel">Modal title</h4>\r\n      </div>\r\n      <div class="modal-body">\r\n        ...\r\n      </div>\r\n      <div class="modal-footer">\r\n        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\r\n        <button type="button" class="btn btn-primary">Save changes</button>\r\n      </div>\r\n    </div>\r\n  </div>\r\n</div>\r\n\r\n  Lorem Ipsum\r\n  Lorem Ipsum\r\n  \r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\users\\templates/index.html", "source_encoding": "ascii", "uri": "index.html", "line_map": {"96": 17, "66": 3, "114": 108, "102": 23, "72": 3, "108": 23, "45": 7, "78": 9, "40": 1, "50": 15, "84": 9, "55": 21, "90": 17, "27": 0, "60": 53}}
__M_END_METADATA
"""
