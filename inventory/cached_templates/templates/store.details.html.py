# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425772773.299109
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/store.details.html'
_template_uri = 'store.details.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'header', 'footer']


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
        def header():
            return render_header(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        product = context.get('product', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
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
        product = context.get('product', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content col-md-12">\r\n      <h2 class="manage">')
        __M_writer(str( product.name ))
        __M_writer(' Details</h2>\r\n      <div class="text-right">\r\n      </div>\r\n      <br>\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n          <th></th>\r\n          <th>Description</th>\r\n          <th>Category</th>\r\n          <th>Current Price</th>\r\n          <th>Quantity</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n')
        __M_writer('            <tr>\r\n              <td><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('inventory/media/products/')
        __M_writer(str( product.id ))
        __M_writer('.jpg"/></td>\r\n              <td>')
        __M_writer(str( product.description ))
        __M_writer(' </td>\r\n              <td>')
        __M_writer(str( product.category ))
        __M_writer(' </td>\r\n              <td>')
        __M_writer(str( product.current_price ))
        __M_writer(' </td>\r\n              <td><input type="number" value="1" min="1" id="item_qty"/></td>\r\n              <td>\r\n                  <div class="row">\r\n                  <button id="show_shoppingcart_dialog" data-pid="')
        __M_writer(str( product.id ))
        __M_writer('" data-qty="1" class="btn btn-warning">Add to Cart</button>\r\n                  </div>\r\n                  <p>\r\n                  <div class="row">\r\n                  <a href="/inventory/store/" class="btn btn-primary">Back to Store</a>\r\n                  </div>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('          </table>\r\n\r\n')
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
{"line_map": {"69": 10, "70": 12, "71": 12, "72": 26, "73": 27, "74": 27, "75": 27, "76": 27, "77": 28, "78": 28, "79": 29, "80": 29, "81": 30, "82": 30, "83": 34, "84": 34, "85": 43, "27": 0, "97": 3, "91": 3, "103": 47, "40": 1, "45": 7, "50": 45, "115": 109, "55": 50, "109": 47, "61": 10}, "uri": "store.details.html", "source_encoding": "ascii", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/store.details.html"}
__M_END_METADATA
"""
