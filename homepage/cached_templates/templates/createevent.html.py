# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423174614.174938
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\homepage\\templates/createevent.html'
_template_uri = 'createevent.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'footer', 'content', 'left']


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
        def footer():
            return render_footer(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Create Event</h2>\r\n\r\n      <form action="event">\r\n        <input type="text" class="form-control createevent" placeholder="Name" aria-describedby="basic-addon1">\r\n        <input type="text" class="form-control createevent" placeholder="Start Date" aria-describedby="basic-addon1">\r\n        <input type="text" class="form-control createevent" placeholder="End Date" aria-describedby="basic-addon1">\r\n        <input type="text" class="form-control createevent" placeholder="Venue" aria-describedby="basic-addon1">\r\n        <input type="text" class="form-control createevent" placeholder="Area" aria-describedby="basic-addon1">\r\n        <button type="submit" class="btn btn-default createeventbutton">Create Event</button>\r\n      </form>\r\n    \r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="left-menu">\r\n    \t<h2 class="managenav">Manage</h2>\r\n    \t<ul>\r\n    \t\t<li class="menu-nav"><a href="event">Events</a></li>\r\n        <li class="menu-nav"><a href="inventory">Inventory</a></li>\r\n        <li class="menu-nav"><a href="area">Areas</a></li>\r\n        <li class="menu-nav"><a href="users">Users</a></li>\r\n        <li class="menu-nav"><a href="MyAccount">My Account</a></li>\r\n\r\n    \t</ul>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 3, "101": 9, "71": 3, "40": 1, "107": 9, "45": 7, "77": 39, "113": 107, "50": 21, "83": 39, "55": 37, "89": 23, "27": 0, "95": 23}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\homepage\\templates/createevent.html", "source_encoding": "ascii", "uri": "createevent.html"}
__M_END_METADATA
"""
