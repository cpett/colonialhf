# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423181237.904245
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\homepage\\templates/inventory.html'
_template_uri = 'inventory.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['footer', 'header', 'content', 'left']


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
        def footer():
            return render_footer(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
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
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Inventory Management</h2>\r\n      <button type="button" class="btn btn-primary right">Create New Item</button>\r\n      <h3>Item Management</h3>\r\n      <table class="table table-hover bottom-buffer">\r\n          <tr>\r\n            <th>Name</th>\r\n            <th>Description</th> \r\n            <th>Type</th>\r\n            <th>Value</th>\r\n            <th> &nbsp;&nbsp;Maintenace</th>\r\n          </tr>\r\n          <tr>\r\n            <td>Nickers</td>\r\n            <td>Colonial Pants</td> \r\n            <td>Rentable</td>\r\n            <td>10.00</td>\r\n            <td><a href="" class="details">Show Details</a>&nbsp; <a href="" class="edit">Edit</a>&nbsp; <a href="" class="delete">Delete</a></td>\r\n         </tr>\r\n         <tr>\r\n            <td>Waist Coat</td>\r\n            <td>Colonial Jacket</td> \r\n            <td>Rentable</td>\r\n            <td>10.00</td>\r\n            <td><a href="" class="details">Show Details</a>&nbsp; <a href="" class="edit">Edit</a>&nbsp; <a href="" class="delete">Delete</a></td>\r\n         </tr>\r\n         <tr>\r\n            <td>Embalming Tool</td>\r\n            <td>N/A</td> \r\n            <td>Display</td>\r\n            <td>7.99</td>\r\n            <td><a href="" class="details">Show Details</a>&nbsp; <a href="" class="edit">Edit</a>&nbsp; <a href="" class="delete">Delete</a></td>\r\n         </tr>\r\n         <tr>\r\n            <td>Mayflower</td>\r\n            <td>Lifesize replica of colonial ship</td> \r\n            <td>Non-rentable</td>\r\n            <td>80,000.00</td>\r\n            <td><a href="" class="details">Show Details</a>&nbsp; <a href="" class="edit">Edit</a>&nbsp; <a href="" class="delete">Delete</a></td>\r\n         </tr>\r\n      </table>\r\n      <button type="button" class="btn btn-primary right">Create New Product</button>\r\n      <h3>Product Management</h3>\r\n      <table class="table table-hover bottom-buffer">\r\n          <tr>\r\n            <th>Name</th>\r\n            <th>Description</th>\r\n            <th>Category</th> \r\n            <th>Current Price</th>\r\n            <th> &nbsp;&nbsp;Maintenace</th>\r\n          </tr>\r\n          <tr>\r\n            <td>Colonial Necklace</td>\r\n            <td>Customized neckalces, just like the colonians used to wear</td>\r\n            <td>Individual</td> \r\n            <td>5.99</td>\r\n            <td><a href="" class="details">Show Details</a>&nbsp; <a href="" class="edit">Edit</a>&nbsp; <a href="" class="delete">Delete</a></td>\r\n         </tr>\r\n         <tr>\r\n            <td>Powderd Wig</td>\r\n            <td>Wig wore during the colonial era</td>\r\n            <td>Bulk</td> \r\n            <td>8.35</td>\r\n            <td><a href="" class="details">Show Details</a>&nbsp; <a href="" class="edit">Edit</a>&nbsp; <a href="" class="delete">Delete</a></td>\r\n         </tr>\r\n      </table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="left-menu">\r\n    \t<h2 class="managenav">Manage</h2>\r\n    \t<ul>\r\n    \t\t<li class="menu-nav"><a href="event">Events</a></li>\r\n        <li class="menu-nav"><a href="inventory">Inventory</a></li>\r\n        <li class="menu-nav"><a href="area">Areas</a></li>\r\n        <li class="menu-nav"><a href="users">Users</a></li>\r\n        <li class="menu-nav"><a href="MyAccount">My Account</a></li>\r\n    \t</ul>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "inventory.html", "line_map": {"65": 92, "101": 9, "71": 92, "40": 1, "107": 9, "45": 7, "77": 3, "113": 107, "50": 20, "83": 3, "55": 90, "89": 22, "27": 0, "95": 22}, "source_encoding": "ascii", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\homepage\\templates/inventory.html"}
__M_END_METADATA
"""
