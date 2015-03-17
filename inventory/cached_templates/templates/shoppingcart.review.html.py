# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425773603.132907
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/shoppingcart.review.html'
_template_uri = 'shoppingcart.review.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


import homepage.models as hmod 

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
        shopping_cart = context.get('shopping_cart', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        shopping_cart = context.get('shopping_cart', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="target col-md-10">\r\n    <h2>Review Cart</h2>\r\n    <table class="table table-striped table-bordered"\r\n    <tr>\r\n      <th>Name</th>\r\n      <th>Quantity</th>\r\n      <th>Total Price</th>\r\n      <th>Remove</th>\r\n    </tr>\r\n      ')
        total_price = 0 
        
        __M_writer('\r\n')
        for item in shopping_cart:
            __M_writer('        ')
            qty = shopping_cart.get(item) 
            
            __M_writer('\r\n        ')
            product = hmod.Product.objects.get(id=item) 
            
            __M_writer('\r\n        <tr>\r\n            <td>')
            __M_writer(str( product.name ))
            __M_writer('</td>\r\n            <td>')
            __M_writer(str( qty ))
            __M_writer('</td>\r\n            <td>')
            __M_writer(str( product.current_price * qty ))
            __M_writer('</td>\r\n            <td><button id="btn_remove" data-id="')
            __M_writer(str( item ))
            __M_writer('" class="remove btn btn-danger">X</button></td>\r\n        </tr>\r\n          ')
            total_price += product.current_price * qty 
            
            __M_writer('\r\n')
        __M_writer('      </table>\r\n      <div class="row">\r\n        <div class="col-md-9">\r\n          <p><strong>Total Price: ')
        __M_writer(str( total_price ))
        __M_writer('</strong></p>\r\n        </div>\r\n        <div class="col-md-3">\r\n          <button id="cart_login_dialog" class="btn btn-warning pull-right">Check Out</button>\r\n        </div>\r\n      </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 16, "65": 17, "67": 17, "68": 19, "69": 19, "70": 20, "71": 20, "72": 21, "73": 21, "74": 22, "75": 22, "76": 24, "78": 24, "79": 26, "16": 2, "81": 29, "87": 81, "29": 0, "80": 29, "37": 1, "38": 2, "43": 36, "49": 4, "56": 4, "57": 14, "59": 14, "60": 15, "61": 16, "62": 16}, "uri": "shoppingcart.review.html", "source_encoding": "ascii", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/shoppingcart.review.html"}
__M_END_METADATA
"""
