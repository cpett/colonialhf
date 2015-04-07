# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428107367.362194
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/return.details.html'
_template_uri = 'return.details.html'
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
        returns = context.get('returns', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        returns = context.get('returns', UNDEFINED)
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Rental Details</h2>\r\n      <br>\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n          <th>Username</th>\r\n          <th>Item</th>\r\n          <th>Rental Time</th>\r\n          <th>Due Date</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n')
        for item in returns:
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( item.userid.username ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( item.itemid.name ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( item.rental_time ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( item.due_date ))
            __M_writer(' </td>\r\n              <td>\r\n                <a href="/inventory/return/" class="btn btn-success">Back</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('        </table>\r\n    <table>\r\n    <form method = "POST">\r\n      <table class="table table-striped table-bordered"\r\n        <tr>\r\n          ')
        __M_writer(str( form ))
        __M_writer('\r\n          <td></td>\r\n          <td>\r\n            <button type="submit" id="check_out" class="btn btn-success">Return</button>\r\n          </td>\r\n        </tr>\r\n        \r\n    </form>\r\n      </table>\r\n\r\n\r\n\r\n\r\n')
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
{"line_map": {"69": 11, "70": 23, "71": 24, "72": 25, "73": 25, "74": 26, "75": 26, "76": 27, "77": 27, "78": 28, "79": 28, "80": 34, "81": 39, "82": 39, "88": 3, "27": 0, "94": 3, "100": 54, "40": 1, "106": 54, "45": 7, "112": 106, "50": 52, "55": 57, "61": 11}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/return.details.html", "source_encoding": "ascii", "uri": "return.details.html"}
__M_END_METADATA
"""
