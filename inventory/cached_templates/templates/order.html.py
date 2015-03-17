# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425598708.204279
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/order.html'
_template_uri = 'order.html'
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
        def footer():
            return render_footer(context._locals(__M_locals))
        orders = context.get('orders', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n')
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
        orders = context.get('orders', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Order Management</h2>\r\n      <div class="text-right">\r\n        <a href="/inventory/order.create/" class="btn btn-primary">Create New order</a>\r\n      </div>\r\n      <br>\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n          <th>ID</th>\r\n          <th>Order Date</th>\r\n          <th>Phone</th>\r\n          <th>Date Picked</th>\r\n          <th>Date Paid</th>\r\n          <th>Date Shipped</th>\r\n          <th>Tracking Number</th>\r\n        </tr>\r\n')
        for order in orders:
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( order.id ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( order.order_date ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( order.phone ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( order.date_picked ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( order.date_shipped ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( order.tracking_number ))
            __M_writer(' </td>\r\n              <td>\r\n                <a href="/inventory/order.edit/')
            __M_writer(str( order.id ))
            __M_writer('/" class="btn btn-success">Edit</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('      </table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/order.html", "source_encoding": "ascii", "uri": "order.html", "line_map": {"66": 3, "107": 37, "72": 45, "108": 41, "78": 45, "84": 11, "27": 0, "92": 28, "93": 29, "94": 30, "95": 30, "96": 31, "97": 31, "98": 32, "99": 32, "100": 33, "101": 33, "102": 34, "39": 1, "104": 35, "105": 35, "106": 37, "103": 34, "44": 7, "114": 108, "49": 43, "91": 11, "54": 48, "60": 3}}
__M_END_METADATA
"""
