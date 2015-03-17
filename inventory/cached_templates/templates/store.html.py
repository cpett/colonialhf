# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425778518.002349
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/store.html'
_template_uri = 'store.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'content', 'footer']


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
        def header():
            return render_header(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Colonial Heritage Online Store</h2>\r\n      <input type="text" id="search_input">\r\n      <button id="search_button" class="btn btn-primary">Search</button>\r\n      <div class="text-right">\r\n      </div>\r\n      <br>\r\n      <div class="col-md-8">\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n            <tr>\r\n            <th>Product</th>\r\n            <th>Name</th>\r\n            <th/>\r\n          </tr>\r\n')
        for product in products:
            __M_writer('              <tr>\r\n                <td><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('inventory/media/products/')
            __M_writer(str( product.id ))
            __M_writer('.jpg"/></td>\r\n                <td class="product_name">')
            __M_writer(str( product.name ))
            __M_writer('</td>\r\n                <td>\r\n                  <a href="/inventory/store.details/')
            __M_writer(str( product.id ))
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


"""
__M_BEGIN_METADATA
{"uri": "store.html", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/store.html", "line_map": {"67": 3, "73": 9, "81": 9, "82": 24, "83": 25, "84": 26, "85": 26, "86": 26, "87": 26, "88": 27, "89": 27, "90": 29, "91": 29, "92": 36, "98": 41, "27": 0, "40": 1, "45": 7, "110": 104, "104": 41, "50": 39, "55": 44, "61": 3}, "source_encoding": "ascii"}
__M_END_METADATA
"""
