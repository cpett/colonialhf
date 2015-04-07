# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428039904.67578
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\events\\templates/event.details.html'
_template_uri = 'event.details.html'
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
        events = context.get('events', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
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
        events = context.get('events', UNDEFINED)
        def content():
            return render_content(context)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Event Details</h2>\r\n      <br>\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n          <th>Name</th>\r\n          <th>Start Date</th>\r\n          <th>Map</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n')
        for event in events:
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( event.name ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( event.start_date ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( event.map_file_name ))
            __M_writer(' </td>\r\n              <td>\r\n                <a href="/events/event.view/" class="btn btn-success">Back</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('      </table>\r\n\r\n      <h2 class="manage">Featured Items</h2>\r\n      <br>\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n          <th>Name</th>\r\n          <th>Description</th>\r\n          <th>Cost</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n')
        for product in products:
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( product.name ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( product.description ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( product.current_price ))
            __M_writer(' </td>\r\n              <td>\r\n                <a href="/inventory/store.details/')
            __M_writer(str( product.id ))
            __M_writer('/" class="btn btn-success">Purchase</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('      </table>\r\n\r\n')
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
{"filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\events\\templates/event.details.html", "source_encoding": "ascii", "uri": "event.details.html", "line_map": {"67": 57, "73": 11, "119": 113, "81": 11, "82": 22, "83": 23, "84": 24, "85": 24, "86": 25, "87": 25, "88": 26, "89": 26, "90": 32, "91": 43, "92": 44, "93": 45, "94": 45, "95": 46, "96": 46, "97": 47, "98": 47, "27": 0, "100": 49, "101": 53, "40": 1, "107": 3, "45": 7, "99": 49, "113": 3, "50": 55, "55": 60, "61": 57}}
__M_END_METADATA
"""
