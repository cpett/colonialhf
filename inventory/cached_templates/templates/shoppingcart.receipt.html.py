# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425755124.147553
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
        shopping_cart = context.get('shopping_cart', UNDEFINED)
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
        shopping_cart = context.get('shopping_cart', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n    <table class="table table-striped table-bordered"\r\n    <tr>\r\n    \r\n    </tr>\r\n      ')
        total_price = 0 
        
        __M_writer('\r\n')
        for item in shopping_cart:
            __M_writer('        ')
            qty = shopping_cart.get(item) 
            
            __M_writer('\r\n        ')
            product = hmod.Product.objects.get(id=item) 
            
            __M_writer('\r\n\r\n          ')
            total_price += product.current_price * qty 
            
            __M_writer('\r\n')
        __M_writer('      </table>\r\n      <div class="row">\r\n        <div class="col-md-9" align="center">\r\n          <h3>Thank you for making a purchase.  Your payment of ')
        __M_writer(str( total_price ))
        __M_writer(' will be processed shortly.<h3>\r\n          <a href="/homepage/index/" align="center" class="btn btn-primary">Back</a>\r\n        </div>\r\n      </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/shoppingcart.receipt.html", "line_map": {"64": 12, "65": 13, "67": 13, "68": 15, "37": 1, "38": 2, "71": 17, "72": 20, "73": 20, "79": 73, "43": 25, "70": 15, "61": 12, "16": 2, "49": 4, "56": 4, "57": 10, "59": 10, "60": 11, "29": 0, "62": 12}, "uri": "shoppingcart.receipt.html"}
__M_END_METADATA
"""
