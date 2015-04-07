# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427991794.278161
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/rentals.html'
_template_uri = 'rentals.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'footer', 'content']


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
        items = context.get('items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

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
        items = context.get('items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Colonial Heritage Online Store</h2>\r\n      <input type="text" id="search_input">\r\n      <button id="search_button" class="btn btn-primary">Search</button>\r\n      <a href="/inventory/store/" class="btn btn-warning">Products</a>\r\n      <div class="text-right">\r\n      </div>\r\n      <br>\r\n      <div class="col-md-8">\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n            <tr>\r\n            <th>Product</th>\r\n            <th>Name</th>\r\n            <th/>\r\n          </tr>\r\n')
        for item in items:
            __M_writer('              <tr>\r\n                <td><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('inventory/media/rentals/')
            __M_writer(str( item.id ))
            __M_writer('.jpg"/></td>\r\n                <td class="product_name">')
            __M_writer(str( item.name ))
            __M_writer('</td>\r\n                <td>\r\n                  <a href="/inventory/rentals.details/')
            __M_writer(str( item.id ))
            __M_writer('/" class="btn btn-primary">Details</a>\r\n                </td>\r\n                <td>\r\n                  \r\n                </td>\r\n              </tr>\r\n')
        __M_writer('        </table>\r\n      </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"67": 3, "73": 42, "79": 42, "85": 9, "27": 0, "93": 9, "94": 25, "95": 26, "96": 27, "97": 27, "98": 27, "99": 27, "100": 28, "101": 28, "102": 30, "103": 30, "40": 1, "45": 7, "110": 104, "104": 37, "50": 40, "55": 45, "61": 3}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/rentals.html", "uri": "rentals.html"}
__M_END_METADATA
"""
