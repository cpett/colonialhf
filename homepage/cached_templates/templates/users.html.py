# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423200972.552547
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\homepage\\templates/users.html'
_template_uri = 'users.html'
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
        users = context.get('users', UNDEFINED)
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
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">User Management</h2>\r\n      <div class="clearfix"></div>\r\n      <div class="text-right">\r\n        <a href="/homepage/users.create/" class="btn btn-primary">Create New User</a>\r\n      </div>\r\n      <br>\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n        <tr>\r\n          <th>ID</th>\r\n          <th>Username</th>\r\n          <th>First Name</th>\r\n          <th>Last Name</th>\r\n          <th>Email</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n')
        for user in users:
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
            __M_writer(' </td>\r\n              <td>\r\n                <a href="/homepage/users.edit/')
            __M_writer(str( user.id ))
            __M_writer('/" class="btn btn-success">Edit</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('      </table>\r\n\r\n    </div>\r\n')
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
{"uri": "users.html", "line_map": {"66": 9, "67": 26, "68": 27, "69": 28, "70": 28, "71": 29, "72": 29, "73": 30, "74": 30, "75": 31, "76": 31, "77": 32, "78": 32, "79": 34, "80": 34, "81": 38, "87": 43, "27": 0, "93": 43, "99": 3, "39": 1, "105": 3, "44": 7, "111": 105, "49": 41, "59": 9}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\homepage\\templates/users.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
