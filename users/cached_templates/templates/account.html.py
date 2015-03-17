# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425683948.896451
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\users\\templates/account.html'
_template_uri = 'account.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'content', 'top']


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
        def content():
            return render_content(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def top():
            return render_top(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

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
        __M_writer('\r\n  <div class="header">\r\n\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n        <tr>\r\n          <th>ID</th>\r\n          <th>Username</th>\r\n          <th>First Name</th>\r\n          <th>Last Name</th>\r\n          <th>Email</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n')
        __M_writer('            <tr>\r\n              <td>')
        __M_writer(str( user.id ))
        __M_writer(' </td>\r\n              <td>')
        __M_writer(str( user.username ))
        __M_writer(' </td>\r\n              <td>')
        __M_writer(str( user.first_name ))
        __M_writer(' </td>\r\n              <td>')
        __M_writer(str( user.last_name ))
        __M_writer(' </td>\r\n              <td>')
        __M_writer(str( user.email ))
        __M_writer(' </td>\r\n              <td>\r\n                <a href="/users/account.edit/')
        __M_writer(str( user.id ))
        __M_writer('/" class="btn btn-success">Edit</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('      </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="row top-header">\r\n\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "account.html", "source_encoding": "ascii", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\users\\templates/account.html", "line_map": {"66": 3, "72": 17, "79": 17, "80": 29, "81": 30, "82": 30, "83": 31, "84": 31, "85": 32, "86": 32, "87": 33, "88": 33, "89": 34, "90": 34, "91": 36, "92": 36, "93": 40, "27": 0, "39": 1, "105": 9, "44": 7, "111": 105, "99": 9, "49": 13, "54": 42, "60": 3}}
__M_END_METADATA
"""
