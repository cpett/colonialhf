# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425678757.360302
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\users\\templates/users.edit.html'
_template_uri = 'users.edit.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['top', 'content', 'footer', 'header']


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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def top():
            return render_top(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

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
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <form method="POST">\r\n        <table>\r\n          ')
        __M_writer(str( form ))
        __M_writer('\r\n        </table>\r\n        <br>\r\n        <button type="submit" class="btn btn-primary">Submit</button>\r\n        <a href="/users/users.delete/')
        __M_writer(str( user.id ))
        __M_writer('" class="btn btn-danger">Delete Account</a>\r\n      </form>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="footer">\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="header">\r\n\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"97": 28, "67": 9, "121": 115, "103": 28, "73": 9, "42": 1, "109": 3, "47": 7, "79": 15, "91": 23, "115": 3, "52": 13, "57": 26, "87": 15, "88": 19, "89": 19, "90": 23, "27": 0}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\users\\templates/users.edit.html", "source_encoding": "ascii", "uri": "users.edit.html"}
__M_END_METADATA
"""
