# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428007506.856032
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
        shopping_cart1 = context.get('shopping_cart1', UNDEFINED)
        shopping_cart0 = context.get('shopping_cart0', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        shopping_cart1 = context.get('shopping_cart1', UNDEFINED)
        shopping_cart0 = context.get('shopping_cart0', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="target col-md-10">\r\n    <h2>Review Cart</h2>\r\n    ')
        total_price = 0 
        
        __M_writer('\r\n')
        if shopping_cart0:
            __M_writer('      Products\r\n      <table class="table table-striped table-bordered"\r\n      <tr>\r\n        <th>Name</th>\r\n        <th>Quantity</th>\r\n        <th>Unit Price</th>\r\n        <th>Total Price</th>\r\n        <th>Remove</th>\r\n      </tr>\r\n\r\n')
            for item in shopping_cart0:
                __M_writer('              ')
                qty = shopping_cart0.get(item) 
                
                __M_writer('\r\n              ')
                product = hmod.Product.objects.get(id=item) 
                
                __M_writer('\r\n              <tr>\r\n                  <td>')
                __M_writer(str( product.name ))
                __M_writer('</td>\r\n                  <td>')
                __M_writer(str( qty ))
                __M_writer('</td>\r\n                  <td>')
                __M_writer(str( product.current_price ))
                __M_writer('</td>\r\n                  <td>')
                __M_writer(str( product.current_price * qty ))
                __M_writer('</td>\r\n                  <td><button id="btn_remove" data-id="')
                __M_writer(str( item ))
                __M_writer('" data-type="0" class="remove btn btn-danger">X</button></td>\r\n              </tr>\r\n                ')
                total_price += product.current_price * qty 
                
                __M_writer(' \r\n')
            __M_writer('          </table>\r\n')
        if shopping_cart1:
            __M_writer('          Rentals\r\n          <table class="table table-striped table-bordered"\r\n          <tr>\r\n            <th>Name</th>\r\n            <th>Quantity</th>\r\n            <th>Unit Price</th>\r\n            <th>Total Price</th>\r\n            <th>Remove</th>\r\n          </tr>\r\n')
            for item in shopping_cart1:
                __M_writer('                ')
                qty = shopping_cart1.get(item) 
                
                __M_writer('\r\n                ')
                product = hmod.Item.objects.get(id=item) 
                
                __M_writer('\r\n                <tr>\r\n                    <td>')
                __M_writer(str( product.name ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( qty ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( product.standard_rental_price ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( product.standard_rental_price * qty ))
                __M_writer('</td>\r\n                    <td><button id="btn_remove" data-id="')
                __M_writer(str( item ))
                __M_writer('" data-type="1" class="remove btn btn-danger">X</button></td>\r\n                </tr>\r\n                  ')
                total_price += product.standard_rental_price * qty 
                
                __M_writer(' \r\n')
            __M_writer('            </table>\r\n')
        __M_writer('      <div class="row">\r\n        <div class="col-md-9">\r\n          <h3>Total Price: ')
        __M_writer(str( total_price ))
        __M_writer('</h3>\r\n        </div>\r\n        <div class="col-md-3">\r\n          <button id="cart_login_dialog" class="btn btn-warning pull-right">Check Out</button>\r\n        </div>\r\n      </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "shoppingcart.review.html", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/shoppingcart.review.html", "line_map": {"16": 2, "29": 0, "38": 1, "39": 2, "44": 66, "50": 4, "58": 4, "59": 7, "61": 7, "62": 8, "63": 9, "64": 19, "65": 20, "66": 20, "68": 20, "69": 21, "71": 21, "72": 23, "73": 23, "74": 24, "75": 24, "76": 25, "77": 25, "78": 26, "79": 26, "80": 27, "81": 27, "82": 29, "84": 29, "85": 31, "86": 33, "87": 34, "88": 43, "89": 44, "90": 44, "92": 44, "93": 45, "95": 45, "96": 47, "97": 47, "98": 48, "99": 48, "100": 49, "101": 49, "102": 50, "103": 50, "104": 51, "105": 51, "106": 53, "108": 53, "109": 55, "110": 57, "111": 59, "112": 59, "118": 112}}
__M_END_METADATA
"""
