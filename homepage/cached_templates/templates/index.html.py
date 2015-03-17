# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425758615.395313
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\homepage\\templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'content', 'footer']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      \r\n\r\n        <!-- Modal SignUp-->\r\n        <div class="modal fade" id="signup_dialog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n          <div class="modal-dialog">\r\n            <div class="modal-content">\r\n              <div class="modal-header">\r\n                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n                <h4 class="modal-title" id="myModalLabel">Sign Up</h4>\r\n              </div>\r\n              <div class="modal-body">\r\n                ...\r\n              </div>\r\n                <!--\r\n                  <div class="modal-footer">\r\n                    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\r\n                    <button type="button" class="btn btn-primary">Save changes</button>\r\n                  </div>\r\n                -->\r\n            </div>\r\n          </div>\r\n        </div>\r\n      <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/colonial.png" width="75%%" style="margin-left:-25px;">\r\n    </div>\r\n')
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
{"uri": "index.html", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\homepage\\templates/index.html", "line_map": {"66": 3, "99": 93, "81": 33, "39": 1, "72": 9, "44": 7, "79": 9, "80": 33, "49": 35, "54": 40, "87": 37, "27": 0, "60": 3, "93": 37}, "source_encoding": "ascii"}
__M_END_METADATA
"""
