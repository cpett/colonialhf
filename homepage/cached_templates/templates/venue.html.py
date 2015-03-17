# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423200915.442703
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\homepage\\templates/venue.html'
_template_uri = 'venue.html'
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
        def footer():
            return render_footer(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        venues = context.get('venues', UNDEFINED)
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
        venues = context.get('venues', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Venue Management</h2>\r\n      <div class="text-right">\r\n        <a href="/homepage/venue.create/" class="btn btn-primary">Create New venue</a>\r\n      </div>\r\n      <br>\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n          <th>ID</th>\r\n          <th>Name</th>\r\n          <th>Address</th>\r\n          <th>City</th>\r\n          <th>State</th>\r\n          <th>ZIP</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n')
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
            __M_writer(' </td>\r\n              <td>\r\n                <a href="/homepage/venue.edit/')
            __M_writer(str( venue.id ))
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
{"uri": "venue.html", "line_map": {"67": 11, "68": 28, "69": 29, "70": 30, "71": 30, "72": 31, "73": 31, "74": 32, "75": 32, "76": 33, "77": 33, "78": 34, "79": 34, "80": 35, "81": 35, "82": 37, "83": 37, "84": 41, "90": 45, "27": 0, "96": 45, "102": 3, "39": 1, "44": 7, "49": 43, "114": 108, "54": 48, "60": 11, "108": 3}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\homepage\\templates/venue.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
