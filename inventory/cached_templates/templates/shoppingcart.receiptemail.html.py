# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428035681.403615
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/shoppingcart.receiptemail.html'
_template_uri = 'shoppingcart.receiptemail.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


import homepage.models as hmod 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        shopping_cart0 = context.get('shopping_cart0', UNDEFINED)
        request = context.get('request', UNDEFINED)
        shopping_cart1 = context.get('shopping_cart1', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n')
        __M_writer('\r\n<html>\r\n<head>\r\n\t<title>Email</title>\r\n</head>\r\n<body>\r\n\r\n<p>Dear ')
        __M_writer(str( request.user.get_full_name() ))
        __M_writer(',</p>\r\n\r\n<p>Thank you for your purchase.</p>\r\n\r\n<table>\r\n<tr>\r\n<td>Date: 3/21/2015</td>\r\n</tr>\r\n<tr>\r\n<td>Name: ')
        __M_writer(str( request.user.get_full_name() ))
        __M_writer('</td>\r\n</tr>\r\n')
        total_price = 0 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['total_price'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n')
        if shopping_cart0:
            __M_writer('<h2>Products</h2>\r\n<table>\r\n\t<tr>\r\n\t\t<th>Item</th>\r\n\t\t<th>Quantity</th>\r\n\t\t<th>Price</th>\r\n\t</tr>\r\n')
            for item in shopping_cart0:
                __M_writer('\t  ')
                qty = shopping_cart0.get(item) 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['qty'] if __M_key in __M_locals_builtin_stored]))
                __M_writer('\r\n\t  ')
                product = hmod.Product.objects.get(id=item) 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['product'] if __M_key in __M_locals_builtin_stored]))
                __M_writer('\r\n\t  <tr>\r\n\t      <td>')
                __M_writer(str( product.name ))
                __M_writer('</td>\r\n\t      <td>')
                __M_writer(str( qty ))
                __M_writer('</td>\r\n\t      <td>')
                __M_writer(str( product.current_price * qty ))
                __M_writer('</td>\r\n\t  </tr>\r\n\t  ')
                total_price += product.current_price * qty 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['total_price'] if __M_key in __M_locals_builtin_stored]))
                __M_writer('\r\n')
            __M_writer('\r\n</table>\r\n')
        __M_writer('\r\n\r\n')
        if shopping_cart1:
            __M_writer('<h2>Rentals</h2>\r\n<table>\r\n\t<tr>\r\n\t\t<th>Item</th>\r\n\t\t<th>Quantity</th>\r\n\t\t<th>Price</th>\r\n\t</tr>\r\n\t<tr>\r\n')
            for item in shopping_cart1:
                __M_writer('        ')
                qty = shopping_cart1.get(item) 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['qty'] if __M_key in __M_locals_builtin_stored]))
                __M_writer('\r\n        ')
                product = hmod.Item.objects.get(id=item) 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['product'] if __M_key in __M_locals_builtin_stored]))
                __M_writer('\r\n        <tr>\r\n            <td>')
                __M_writer(str( product.name ))
                __M_writer('</td>\r\n            <td>')
                __M_writer(str( qty ))
                __M_writer('</td>\r\n            <td>')
                __M_writer(str( product.standard_rental_price * qty ))
                __M_writer('</td>\r\n        </tr>\r\n          ')
                total_price += product.standard_rental_price * qty 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['total_price'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(' \r\n')
            __M_writer('\t</tr>\t\r\n</table>\r\n')
        __M_writer('<h3>Total Price: ')
        __M_writer(str( total_price ))
        __M_writer('</h3>\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 2, "18": 0, "26": 1, "27": 2, "28": 9, "29": 9, "30": 18, "31": 18, "32": 20, "36": 20, "37": 21, "38": 22, "39": 29, "40": 30, "41": 30, "45": 30, "46": 31, "50": 31, "51": 33, "52": 33, "53": 34, "54": 34, "55": 35, "56": 35, "57": 37, "61": 37, "62": 39, "63": 42, "64": 44, "65": 45, "66": 53, "67": 54, "68": 54, "72": 54, "73": 55, "77": 55, "78": 57, "79": 57, "80": 58, "81": 58, "82": 59, "83": 59, "84": 61, "88": 61, "89": 63, "90": 66, "91": 66, "92": 66, "98": 92}, "source_encoding": "ascii", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/shoppingcart.receiptemail.html", "uri": "shoppingcart.receiptemail.html"}
__M_END_METADATA
"""
