# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423114636.602342
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\homepage\\templates/users2.edit.html'
_template_uri = 'users2.edit.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['left', 'content', 'header', 'footer']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="left-menu">\r\n      <h2 class="managenav">Manage</h2>\r\n      <ul>\r\n        <li class="menu-nav"><a href="event">Events</a></li>\r\n        <li class="menu-nav"><a href="inventory">Inventory</a></li>\r\n        <li class="menu-nav"><a href="area">Areas</a></li>\r\n        <li class="menu-nav"><a href="users">Users</a></li>\r\n        <li class="menu-nav"><a href="MyAccount">My Account</a></li>\r\n      </ul>\r\n    </div>\r\n')
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
        __M_writer('\r\n    <div class="content">\r\n      <form method="POST">\r\n        <table>\r\n          ')
        __M_writer(str( form ))
        __M_writer('\r\n        </table>\r\n        <br>\r\n        <button type="submit" class="btn btn-primary">Submit</button>\r\n        <a href="/homepage/users2.delete/')
        __M_writer(str( user.id ))
        __M_writer('" class="btn btn-danger">Delete Account</a>\r\n      </form>\r\n    </div>\r\n')
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


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\homepage\\templates/users2.edit.html", "line_map": {"97": 3, "67": 9, "121": 115, "103": 3, "73": 9, "42": 1, "109": 35, "47": 7, "79": 22, "91": 30, "115": 35, "52": 20, "57": 33, "87": 22, "88": 26, "89": 26, "90": 30, "27": 0}, "source_encoding": "ascii", "uri": "users2.edit.html"}
__M_END_METADATA
"""
