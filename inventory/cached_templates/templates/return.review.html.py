# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428177968.521295
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/return.review.html'
_template_uri = 'return.review.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['footer', 'header', 'content']


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
        def header():
            return render_header(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        rental = context.get('rental', UNDEFINED)
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
        rental = context.get('rental', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Returned Items</h2>\r\n      <br>\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n          <th>ID</th>\r\n          <th>User</th>\r\n          <th>Item</th>\r\n          <th>Rented</th>\r\n          <th>Due</th>\r\n          <th>Returned</th>\r\n          <th>Condition</th>\r\n          <th>Damage Fee</th>\r\n          <th>Late Fee</th>\r\n          <th>Total Fees</th>\r\n        </tr>\r\n')
        for item in rental:
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( item.id ))
            __M_writer('</td>\r\n              <td>')
            __M_writer(str( item.userid ))
            __M_writer('</td>\r\n              <td>')
            __M_writer(str( item.itemid.name ))
            __M_writer('</td>\r\n              <td>')
            __M_writer(str( item.rental_time ))
            __M_writer('</td>\r\n              <td>')
            __M_writer(str( item.due_date ))
            __M_writer('</td>\r\n              <td>')
            __M_writer(str( item.return_time ))
            __M_writer('</td>\r\n              <td>')
            __M_writer(str( item.condition ))
            __M_writer('</td>\r\n              <td>')
            __M_writer(str( item.damage_fee ))
            __M_writer('</td>\r\n              <td>')
            __M_writer(str( item.late_fee ))
            __M_writer('</td>\r\n              <td>')
            __M_writer(str( item.fees_paid ))
            __M_writer('</td>\r\n            </tr>\r\n')
        __M_writer('      </table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/return.review.html", "line_map": {"66": 44, "107": 34, "113": 37, "72": 3, "108": 35, "78": 3, "84": 9, "27": 0, "92": 26, "93": 27, "94": 28, "95": 28, "96": 29, "97": 29, "98": 30, "99": 30, "100": 31, "101": 31, "102": 32, "39": 1, "104": 33, "105": 33, "106": 34, "103": 32, "44": 7, "109": 35, "110": 36, "111": 36, "112": 37, "49": 42, "91": 9, "54": 47, "120": 114, "114": 40, "60": 44}, "source_encoding": "ascii", "uri": "return.review.html"}
__M_END_METADATA
"""
