# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423200826.524003
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\homepage\\templates/item.html'
_template_uri = 'item.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
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
        def content():
            return render_content(context)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Item Management</h2>\r\n      <div class="text-right">\r\n        <a href="/homepage/item.create/" class="btn btn-primary">Create New Item</a>\r\n      </div>\r\n      <br>\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n          <th>ID</th>\r\n          <th>Name</th>\r\n          <th>Description</th>\r\n          <th>Value</th>\r\n          <th>Standard Rental Price</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n')
        for item in items:
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( item.id ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( item.name ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( item.description ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( item.value ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( item.standard_rental_price ))
            __M_writer(' </td>\r\n              <td>\r\n                <a href="/homepage/item.edit/')
            __M_writer(str( item.id ))
            __M_writer('/" class="btn btn-success">Edit</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('      </table>\r\n\r\n')
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
{"uri": "item.html", "line_map": {"67": 11, "68": 27, "69": 28, "70": 29, "71": 29, "72": 30, "73": 30, "74": 31, "75": 31, "76": 32, "77": 32, "78": 33, "79": 33, "80": 35, "81": 35, "82": 39, "88": 43, "27": 0, "94": 43, "100": 3, "39": 1, "106": 3, "44": 7, "112": 106, "49": 41, "54": 46, "60": 11}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\homepage\\templates/item.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
