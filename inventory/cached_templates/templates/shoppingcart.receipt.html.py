# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428015916.824017
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/shoppingcart.receipt.html'
_template_uri = 'shoppingcart.receipt.html'
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
        shopping_cart0 = context.get('shopping_cart0', UNDEFINED)
        shopping_cart1 = context.get('shopping_cart1', UNDEFINED)
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
        def content():
            return render_content(context)
        shopping_cart0 = context.get('shopping_cart0', UNDEFINED)
        shopping_cart1 = context.get('shopping_cart1', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n    <table class="table table-striped table-bordered"\r\n    <tr>\r\n    \r\n    </tr>\r\n       ')
        total_price = 0 
        
        __M_writer('\r\n')
        if shopping_cart0:
            for item in shopping_cart0:
                __M_writer('          ')
                qty = shopping_cart0.get(item) 
                
                __M_writer('\r\n          ')
                product = hmod.Product.objects.get(id=item) 
                
                __M_writer('\r\n          ')
                total_price += product.current_price * qty 
                
                __M_writer('\r\n')
        if shopping_cart1:
            for item in shopping_cart1:
                __M_writer('          ')
                qty = shopping_cart1.get(item) 
                
                __M_writer('\r\n          ')
                product = hmod.Item.objects.get(id=item) 
                
                __M_writer('\r\n          ')
                total_price += product.standard_rental_price * qty 
                
                __M_writer('\r\n')
        __M_writer('      </table>\r\n      <div class="row">\r\n        <div class="col-md-9" align="center">\r\n          <h3>Thank you for making a purchase.  Your payment of ')
        __M_writer(str( total_price ))
        __M_writer(' will be processed shortly.<h3>\r\n          <a href="/homepage/index/" align="center" class="btn btn-primary">Back</a>\r\n        </div>\r\n      </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 13, "65": 13, "67": 13, "68": 14, "70": 14, "71": 15, "73": 15, "74": 18, "75": 19, "76": 20, "77": 20, "79": 20, "16": 2, "82": 21, "83": 22, "85": 22, "86": 25, "87": 28, "88": 28, "29": 0, "94": 88, "80": 21, "38": 1, "39": 2, "44": 33, "50": 4, "58": 4, "59": 10, "61": 10, "62": 11, "63": 12}, "source_encoding": "ascii", "uri": "shoppingcart.receipt.html", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/shoppingcart.receipt.html"}
__M_END_METADATA
"""
