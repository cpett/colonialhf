# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425674610.623708
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\users\\templates/signup.html'
_template_uri = 'signup.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'left', 'top', 'content']


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
    return runtime._inherit_from(context, '/homepage/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def header():
            return render_header(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        def top():
            return render_top(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
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


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div>\r\n\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="row top-header">\r\n\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <form id="signup" method="POST">\r\n        <table>\r\n          ')
        __M_writer(str( form ))
        __M_writer(' \r\n        </table>\r\n        <br>\r\n        <button type="submit" class="btn btn-primary">Submit</button>\r\n        <a href="/users/signup.delete/')
        __M_writer(str( user.id ))
        __M_writer('" class="btn btn-danger">Delete Account</a>\r\n      </form>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"112": 21, "98": 9, "68": 3, "116": 29, "104": 21, "42": 1, "47": 7, "80": 15, "113": 25, "114": 25, "115": 29, "52": 13, "86": 15, "57": 19, "122": 116, "27": 0, "92": 9, "74": 3, "62": 32}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\users\\templates/signup.html", "uri": "signup.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
