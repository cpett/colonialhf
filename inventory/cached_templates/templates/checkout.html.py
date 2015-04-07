# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428026044.646287
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/checkout.html'
_template_uri = 'checkout.html'
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
        shopping_cart0 = context.get('shopping_cart0', UNDEFINED)
        form = context.get('form', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        shopping_cart1 = context.get('shopping_cart1', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content col-md-6">\r\n    <h2>Billing Information</h2>\r\n    <form method = "POST">\r\n    <table class="table table-striped table-bordered"\r\n    <tr>\r\n    ')
        __M_writer(str( form ))
        __M_writer('\r\n    </tr>\r\n      ')
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
        __M_writer('      </table>\r\n      <div class="row">\r\n        <div class="col-md-9">\r\n          <h3>Total Price: ')
        __M_writer(str( total_price ))
        __M_writer('</h3>\r\n        </div>\r\n        </form>\r\n        <div class="col-md-3">\r\n          <button type="submit" id="check_out" class="btn btn-warning pull-right">Check Out</button>\r\n        </div>\r\n      </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 12, "66": 13, "67": 14, "68": 15, "69": 15, "71": 15, "72": 16, "74": 16, "75": 17, "77": 17, "78": 20, "79": 21, "16": 2, "81": 22, "83": 22, "84": 23, "86": 23, "87": 24, "89": 24, "90": 27, "91": 30, "92": 30, "29": 0, "80": 22, "98": 92, "39": 1, "40": 2, "45": 38, "51": 4, "60": 4, "61": 10, "62": 10, "63": 12}, "source_encoding": "ascii", "uri": "checkout.html", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\inventory\\templates/checkout.html"}
__M_END_METADATA
"""
