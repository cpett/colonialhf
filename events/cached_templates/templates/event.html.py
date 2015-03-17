# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425710490.070976
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\events\\templates/event.html'
_template_uri = 'event.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        events = context.get('events', UNDEFINED)
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
        events = context.get('events', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Event Management</h2>\r\n      <div class="text-right">\r\n        <a href="/events/event.create/" class="btn btn-primary">Create New Event</a>\r\n      </div>\r\n      <br>\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n          <th>Name</th>\r\n          <th>Start Date</th>\r\n          <th>Map</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n')
        for event in events:
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( event.name ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( event.start_date ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( event.map_file_name ))
            __M_writer(' </td>\r\n              <td>\r\n                <a href="/events/event.edit/')
            __M_writer(str( event.id ))
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
{"source_encoding": "ascii", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\events\\templates/event.html", "line_map": {"67": 11, "68": 25, "69": 26, "70": 27, "71": 27, "72": 28, "73": 28, "74": 29, "75": 29, "76": 31, "77": 31, "78": 35, "108": 102, "84": 39, "90": 39, "27": 0, "96": 3, "102": 3, "39": 1, "44": 7, "49": 37, "54": 42, "60": 11}, "uri": "event.html"}
__M_END_METADATA
"""
