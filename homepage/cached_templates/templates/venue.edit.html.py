# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423196270.217914
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\homepage\\templates/venue.edit.html'
_template_uri = 'venue.edit.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'content', 'left', 'footer']


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
        def header():
            return render_header(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        venues = context.get('venues', UNDEFINED)
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
        

        __M_writer('\r\n')
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        venues = context.get('venues', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <form method="POST">\r\n        <table>\r\n          ')
        __M_writer(str( form ))
        __M_writer('\r\n        </table>\r\n        <br>\r\n        <button type="submit" class="btn btn-primary">Submit</button>\r\n        <a href="/homepage/venue.delete/')
        __M_writer(str( venues.id ))
        __M_writer('" class="btn btn-danger">Delete Venue</a>\r\n      </form>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="left-menu">\r\n    \t<h2 class="managenav">Manage</h2>\r\n    \t<ul>\r\n    \t\t<li class="menu-nav"><a href="/homepage/venues">venues</a></li>\r\n        <li class="menu-nav"><a href="/homepage/inventory">Inventory</a></li>\r\n        <li class="menu-nav"><a href="/homepage/area">Areas</a></li>\r\n        <li class="menu-nav"><a href="/homepage/users">Users</a></li>\r\n        <li class="menu-nav"><a href="/homepage/MyAccount">My Account</a></li>\r\n    \t</ul>\r\n    </div>\r\n')
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
{"source_encoding": "ascii", "uri": "venue.edit.html", "line_map": {"116": 35, "98": 9, "91": 30, "68": 3, "104": 9, "42": 1, "110": 35, "47": 7, "80": 22, "52": 20, "122": 116, "57": 33, "88": 22, "89": 26, "90": 26, "27": 0, "92": 30, "74": 3, "62": 38}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\homepage\\templates/venue.edit.html"}
__M_END_METADATA
"""
