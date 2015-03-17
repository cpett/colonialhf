# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423109037.791158
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\homepage\\templates/myaccount.html'
_template_uri = 'myaccount.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'content', 'footer', 'left']


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
        def header():
            return render_header(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

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
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">My Account</h2>\r\n            <div class="row">\r\n              <div class="col-md-4">\r\n                    <div class="form-group">\r\n                    <label for="inputEmail3" class="col-sm-2 control-label editform">First Name</label>\r\n                      <p>Josh</p>\r\n                  </div>\r\n                  <div class="form-group">\r\n                    <label for="inputPassword3" class="col-sm-2 control-label editform">Last Name</label>\r\n                      <p>Haws</p>\r\n                  </div>\r\n                  <div class="form-group">\r\n                    <label for="inputEmail3" class="col-sm-2 control-label editform">Email Address</label>\r\n                      <p>joshhaws@colonialheritage.org</p>\r\n                  </div>\r\n                  <div class="form-group">\r\n                    <label for="inputEmail3" class="col-sm-2 control-label editform">Password</label>\r\n                      <p>****</p>\r\n                  </div>\r\n              </div>\r\n              <div class="col-md-4">\r\n                    <div class="form-group">\r\n                    <label for="inputEmail3" class="col-sm-2 control-label editform">Street Address</label>\r\n                      <p>99 s 600 e</p>\r\n                  </div>\r\n                  <div class="form-group">\r\n                    <label for="inputPassword3" class="col-sm-2 control-label editform">City</label>\r\n                      <p>Provo</p>\r\n                  </div>\r\n                  <div class="form-group">\r\n                    <label for="inputEmail3" class="col-sm-2 control-label editform">Zip</label>\r\n                      <p>84606</p>\r\n                  </div>\r\n                  <div class="form-group">\r\n                    <label for="inputEmail3" class="col-sm-2 control-label editform">Country</label>\r\n                      <p>United States</p>\r\n                  </div>\r\n\r\n              </div>\r\n              <div class="col-md-4">\r\n              <div class="form-group">\r\n                    <label for="inputEmail3" class="col-sm-2 control-label editform">Security Question</label>\r\n                      <p>First Pet Name?</p>\r\n                  </div>\r\n                  <div class="form-group">\r\n                    <label for="inputPassword3" class="col-sm-2 control-label editform">Answer</label>\r\n                      <p>Spikey</p>\r\n                  </div>\r\n              </div>\r\n            </div>\r\n            <form action="AccountChanges"><button type="submit" class="btn btn-primary left">Edit Account</button></form>\r\n')
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


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="left-menu">\r\n    \t<h2 class="managenav">Manage</h2>\r\n    \t<ul>\r\n    \t<li class="menu-nav"><a href="event">Events</a></li>\r\n        <li class="menu-nav"><a href="inventory">Inventory</a></li>\r\n        <li class="menu-nav"><a href="area">Areas</a></li>\r\n        <li class="menu-nav"><a href="users">Users</a></li>\r\n        <li class="menu-nav"><a href="MyAccount">My Account</a></li>\r\n    \t</ul>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 3, "101": 9, "71": 3, "40": 1, "107": 9, "45": 7, "77": 22, "113": 107, "50": 20, "83": 22, "55": 75, "89": 77, "27": 0, "95": 77}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\homepage\\templates/myaccount.html", "uri": "myaccount.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
