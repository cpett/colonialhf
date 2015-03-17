# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425421353.915432
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\events\\templates/venue.html'
_template_uri = 'venue.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        venues = context.get('venues', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
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
        venues = context.get('venues', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Venue Management</h2>\r\n      <div class="text-right">\r\n        <a href="/events/venue.create/" class="btn btn-primary">Create New venue</a>\r\n      </div>\r\n      <br>\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n          <th>ID</th>\r\n          <th>Name</th>\r\n          <th>Address</th>\r\n          <th>City</th>\r\n          <th>State</th>\r\n          <th>ZIP</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n')
        for venue in venues:
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( venue.id ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( venue.name ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( venue.address ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( venue.city ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( venue.state ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( venue.zip ))
            __M_writer(' </td>\r\n              <td>\r\n                <a href="/events/venue.edit/')
            __M_writer(str( venue.id ))
            __M_writer('/" class="btn btn-success">Edit</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('      </table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\events\\templates/venue.html", "uri": "venue.html", "line_map": {"66": 45, "107": 37, "72": 3, "108": 41, "78": 3, "84": 11, "27": 0, "92": 28, "93": 29, "94": 30, "95": 30, "96": 31, "97": 31, "98": 32, "99": 32, "100": 33, "101": 33, "102": 34, "39": 1, "104": 35, "105": 35, "106": 37, "103": 34, "44": 7, "114": 108, "49": 43, "91": 11, "54": 48, "60": 45}}
__M_END_METADATA
"""
