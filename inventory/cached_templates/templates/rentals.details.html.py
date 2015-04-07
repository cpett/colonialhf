# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428176330.922156
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/rentals.details.html'
_template_uri = 'rentals.details.html'
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
        def header():
            return render_header(context._locals(__M_locals))
        product = context.get('product', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        product = context.get('product', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content col-md-12">\r\n      <h2 class="manage">')
        __M_writer(str( product.name ))
        __M_writer(' Details</h2>\r\n      <div class="text-right">\r\n      </div>\r\n      <br>\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n          <th></th>\r\n          <th>Description</th>\r\n          <th>Value</th>\r\n          <th>Rental Price</th>\r\n          <th>Quantity</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n')
        __M_writer('            <tr>\r\n              <td><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('inventory/media/rentals/')
        __M_writer(str( product.id ))
        __M_writer('.jpg"/></td>\r\n              <td>')
        __M_writer(str( product.description ))
        __M_writer(' </td>\r\n              <td>')
        __M_writer(str( product.value ))
        __M_writer(' </td>\r\n              <td>')
        __M_writer(str( product.standard_rental_price ))
        __M_writer(' </td>\r\n              <td><input type="number" value="1" min="1" id="item_qty"/></td>\r\n              <td>\r\n                  <div class="row">\r\n                  <button id="show_shoppingcart_dialog" data-id="')
        __M_writer(str( product.id ))
        __M_writer('" data-qty="1" data-type="1" class="btn btn-warning">Add to Cart</button>\r\n                  </div>\r\n                  <p>\r\n                  <div class="row">\r\n                  <a href="/inventory/rentals/" class="btn btn-primary">Back to Store</a>\r\n                  </div>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('          </table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"67": 3, "73": 47, "109": 43, "79": 47, "85": 10, "27": 0, "93": 10, "94": 12, "95": 12, "96": 26, "97": 27, "98": 27, "99": 27, "100": 27, "101": 28, "102": 28, "103": 29, "40": 1, "105": 30, "106": 30, "107": 34, "108": 34, "45": 7, "104": 29, "50": 45, "115": 109, "55": 50, "61": 3}, "source_encoding": "ascii", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/rentals.details.html", "uri": "rentals.details.html"}
__M_END_METADATA
"""
