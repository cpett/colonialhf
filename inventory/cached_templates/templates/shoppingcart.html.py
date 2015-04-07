# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428010065.247441
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/shoppingcart.html'
_template_uri = 'shoppingcart.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        shopping_cart0 = context.get('shopping_cart0', UNDEFINED)
        shopping_cart1 = context.get('shopping_cart1', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        shopping_cart0 = context.get('shopping_cart0', UNDEFINED)
        shopping_cart1 = context.get('shopping_cart1', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="target">        \r\n    ')
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
        __M_writer('</h3>\r\n        </div>\r\n        <div class="col-md-3">\r\n          <a href="/inventory/shoppingcart.review/" id="check_out" class="btn btn-warning pull-right">Check Out</a>\r\n        </div>\r\n      </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/shoppingcart.html", "uri": "shoppingcart.html", "line_map": {"16": 2, "29": 0, "38": 1, "39": 2, "44": 65, "50": 4, "58": 4, "59": 6, "61": 6, "62": 7, "63": 8, "64": 18, "65": 19, "66": 19, "68": 19, "69": 20, "71": 20, "72": 22, "73": 22, "74": 23, "75": 23, "76": 24, "77": 24, "78": 25, "79": 25, "80": 26, "81": 26, "82": 28, "84": 28, "85": 30, "86": 32, "87": 33, "88": 42, "89": 43, "90": 43, "92": 43, "93": 44, "95": 44, "96": 46, "97": 46, "98": 47, "99": 47, "100": 48, "101": 48, "102": 49, "103": 49, "104": 50, "105": 50, "106": 52, "108": 52, "109": 54, "110": 56, "111": 58, "112": 58, "118": 112}}
__M_END_METADATA
"""
