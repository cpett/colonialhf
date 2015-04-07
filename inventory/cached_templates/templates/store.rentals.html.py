# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427991073.800734
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/store.rentals.html'
_template_uri = 'store.rentals.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'footer', 'header']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Colonial Heritage Online Store</h2>\r\n      <input type="text" id="search_input">\r\n      <button id="search_button" class="btn btn-primary">Search</button>\r\n      <a href="/inventory/store/" class="btn btn-warning">Products</a>\r\n      <div class="text-right">\r\n      </div>\r\n      <br>\r\n      <div class="col-md-8">\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n            <tr>\r\n            <th>Product</th>\r\n            <th>Name</th>\r\n            <th/>\r\n          </tr>\r\n')
        for item in items:
            __M_writer('              <tr>\r\n                <td><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('inventory/media/rentals/')
            __M_writer(str( item.id ))
            __M_writer('.jpg"/></td>\r\n                <td class="product_name">')
            __M_writer(str( item.name ))
            __M_writer('</td>\r\n                <td>\r\n                  <a href="/inventory/store.details/')
            __M_writer(str( item.id ))
            __M_writer('/" class="btn btn-primary">Details</a>\r\n                </td>\r\n                <td>\r\n                  \r\n                </td>\r\n              </tr>\r\n')
        __M_writer('        </table>\r\n      </div>\r\n\r\n')
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
{"uri": "store.rentals.html", "line_map": {"69": 9, "70": 25, "71": 26, "72": 27, "73": 27, "74": 27, "75": 27, "76": 28, "77": 28, "78": 30, "79": 30, "80": 37, "86": 42, "27": 0, "92": 42, "98": 3, "40": 1, "45": 7, "110": 104, "104": 3, "50": 40, "55": 45, "61": 9}, "source_encoding": "ascii", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/store.rentals.html"}
__M_END_METADATA
"""
