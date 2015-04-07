# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428176920.08193
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/overdue.html'
_template_uri = 'overdue.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['footer', 'content', 'header']


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
        def footer():
            return render_footer(context._locals(__M_locals))
        Batch90 = context.get('Batch90', UNDEFINED)
        Batch60 = context.get('Batch60', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        Batch30 = context.get('Batch30', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
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
        Batch90 = context.get('Batch90', UNDEFINED)
        Batch60 = context.get('Batch60', UNDEFINED)
        Batch30 = context.get('Batch30', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Overdue Items</h2>\r\n      <br>\r\n      <div class="text-right">\r\n      <a href="/inventory/return/" class="btn btn-primary">Back to Rentals</a>\r\n      <a href="/inventory/overdue.email/" class="btn btn-primary">Send Email</a>\r\n      </div>\r\n      <br/>\r\n      Batch30\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n          <th>Username</th>\r\n          <th>Item</th>\r\n          <th>Rental Time</th>\r\n          <th>Due Date</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n\r\n')
        for item in Batch30: 
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( item.userid.username ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( item.itemid.name ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( item.rental_time ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( item.due_date ))
            __M_writer(' </td>\r\n              <td>\r\n                <a href="/inventory/return.details/')
            __M_writer(str( item.id ))
            __M_writer('" class="btn btn-success">Process</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('      </table>\r\n      <br/>\r\n      Batch60\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n          <th>Username</th>\r\n          <th>Item</th>\r\n          <th>Rental Time</th>\r\n          <th>Due Date</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n\r\n')
        for item in Batch60: 
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( item.userid.username ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( item.itemid.name ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( item.rental_time ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( item.due_date ))
            __M_writer(' </td>\r\n              <td>\r\n                <a href="/inventory/return.details/')
            __M_writer(str( item.id ))
            __M_writer('" class="btn btn-success">Process</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('      </table>\r\n      <br/>\r\n      Batch90\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n          <th>Username</th>\r\n          <th>Item</th>\r\n          <th>Rental Time</th>\r\n          <th>Due Date</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n\r\n')
        for item in Batch90: 
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( item.userid.username ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( item.itemid.name ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( item.rental_time ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( item.due_date ))
            __M_writer(' </td>\r\n              <td>\r\n                <a href="/inventory/return.details/')
            __M_writer(str( item.id ))
            __M_writer('" class="btn btn-success">Process</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('      </table>\r\n')
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
{"source_encoding": "ascii", "line_map": {"128": 3, "134": 3, "140": 134, "27": 0, "41": 1, "46": 7, "51": 86, "56": 91, "62": 88, "68": 88, "74": 9, "83": 9, "84": 28, "85": 29, "86": 30, "87": 30, "88": 31, "89": 31, "90": 32, "91": 32, "92": 33, "93": 33, "94": 35, "95": 35, "96": 39, "97": 51, "98": 52, "99": 53, "100": 53, "101": 54, "102": 54, "103": 55, "104": 55, "105": 56, "106": 56, "107": 58, "108": 58, "109": 62, "110": 74, "111": 75, "112": 76, "113": 76, "114": 77, "115": 77, "116": 78, "117": 78, "118": 79, "119": 79, "120": 81, "121": 81, "122": 85}, "uri": "overdue.html", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/overdue.html"}
__M_END_METADATA
"""
