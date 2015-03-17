# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425777343.026956
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['top', 'left', 'content', 'login']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def login():
            return render_login(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def top():
            return render_top(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n    \r\n    <title>Colonial Heritage Foundation</title>\r\n    \r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\r\n    <link rel="stylesheet" href="//code.jquery.com/ui/1.11.2/themes/smoothness/jquery-ui.css">\r\n    <script src="//code.jquery.com/ui/1.11.2/jquery-ui.js"></script>\r\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('users/scripts/script.js/"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\r\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('users/scripts/signup.js/"></script>\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n  \r\n  </head>\r\n  <body>\r\n  \r\n    <header>\r\n      <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/header.jpg" width="100%">\r\n\r\n      <div class="pull-right row container-fluid">\r\n')
        if request.user.is_authenticated():
            __M_writer('          Welcome, ')
            __M_writer(str( request.user.get_full_name() ))
            __M_writer('\r\n          <a href="/users/account/" class="btn btn-success">My Account</a>\r\n          <a href="/homepage/logout/" class="btn btn-danger">Log Out</a>\r\n')
        else:
            __M_writer('          <button id="show_login_dialog" class="btn btn-success">Login</button>\r\n          <a href="/users/signup.create" class="btn btn-primary">Sign Up</a>\r\n')
        __M_writer('      </div>\r\n\r\n    </header> \r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'login'):
            context['self'].login(**pageargs)
        

        __M_writer('\r\n      \r\n      <nav class="navbar navbar-default">\r\n          <div class="container-fluid">\r\n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n              <ul class="nav navbar-nav">\r\n                <li><a href="/homepage/index/" class="top-nav">Home</a></li>\r\n                <li><a href="/inventory/store/" class="top-nav">Store</a></li>\r\n                <li><a href="#">Gallery</a></li>\r\n                <li><a href="#">Products</a></li>\r\n                <li><a href="#">Products</a></li>\r\n              </ul>\r\n              <ul class="nav navbar-nav navbar-right">\r\n                </li>\r\n                <form class="navbar-form navbar-right" role="search">\r\n                  <div class="form-group">\r\n                    <input type="text" class="form-control" placeholder="Search">\r\n                  </div>\r\n                  <button type="submit" class="btn btn-default">Submit</button>\r\n                </form>\r\n              </ul>\r\n            </div>\r\n          </div>\r\n        </nav>\r\n  \r\n    <div class="wrapper">\r\n\r\n      <div class="row">\r\n\r\n      <div class="col-sm-2">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n      </div>\r\n\r\n      <div class="col-sm-10">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \r\n      </div>\r\n\r\n    </div>\r\n\r\n      <div class="push"></div>\r\n\r\n    </div>\r\n\r\n\r\n    <footer>\r\n    <div class="footer">\r\n        <div class="row">\r\n          <div class="col-md-1"></div>\r\n          <div class="col-md-3">\r\n            <ul>\r\n              <li style="margin-top:5px; margin-left:-50px;"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/chflogo.png"></li>\r\n              <li>&copy;2015 Colonial Heritage, Inc. All rights reserved.</li>\r\n            </ul>\r\n          </div>\r\n          <div class="col-md-2">\r\n            <ul>\r\n              <li class="footer-title">About</li>\r\n              <li><a href="#">About</li>\r\n              <li><a href="#">Premium</a></li>\r\n              <li><a href="#">Privacy Policy</a></li>\r\n              <li><a href="#">Terms and Conditions</a></li>\r\n            </ul>\r\n          </div>\r\n          <div class="col-md-2">\r\n            <ul>\r\n              <li class="footer-title">Follow</li>\r\n              <li><a href="#">Facebook</a></li>\r\n              <li><a href="#">Twitter</a></li>\r\n              <li><a href="#">Youtube</a></li>\r\n              <li><a href="#">Blog</a></li>\r\n            </ul>\r\n          </div>\r\n          <div class="col-md-2">\r\n            <ul>\r\n              <li class="footer-title">Help</li>\r\n              <li><a href="#">Support</a></li>\r\n            </ul>\r\n          </div>        \r\n          <div class="col-md-2">\r\n            <ul>\r\n              <li class="footer-title">More</li>\r\n              <li><a href="signup.php">Sign Up</a></li>\r\n              <li><a href="login.php">Log In</a></li>\r\n              <li><a href="#">Careers</a></li>\r\n              <li><a href="#">Developers</a></li>\r\n            </ul>\r\n          </div>\r\n        </div>\r\n    </div>\r\n    <p class="workaround">a</p>\r\n    </footer>\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n  \r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        __M_writer = context.writer()
        __M_writer('\r\n      <div class="row top-header">\r\n        <!--\r\n          <div class="col-md-10 top-header"></div>\r\n          <div class="col-md-1 top-header"><a href="/inventory/store/" class="top-nav">Store</a></div>\r\n          <div class="col-md-1 top-header"><a href="/homepage/index/" class="top-nav">Home</a></div>\r\n        -->\r\n      </div>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n          <div class="left-menu">\r\n')
        if request.user.is_authenticated():
            __M_writer('                <h2 class="managenav">Manage</h2>\r\n                <ul>\r\n                  <li class="menu-nav"><a href="/events/event/">Events</a></li>\r\n                  <li class="menu-nav"><a href="/inventory/item/">Inventory</a></li>\r\n                  <li class="menu-nav"><a href="/inventory/product/">Products</a></li>\r\n                  <li class="menu-nav"><a href="/inventory/order/">Orders</a></li>\r\n                  <li class="menu-nav"><a href="/events/venue/">Venues</a></li>\r\n                  <li class="menu-nav"><a href="/users/users/">Users</a></li>\r\n                  <li class="menu-nav"><a href="/inventory/store/">Store</a></li>\r\n                </ul>\r\n')
        else:
            pass
        __M_writer('          </div>\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n          Site content goes here in sub-templates.\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_login(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def login():
            return render_login(context)
        __M_writer = context.writer()
        __M_writer('\r\n      <div>\r\n        <!-- Modal Login-->\r\n          <div class="modal fade" id="login_dialog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n            <div class="modal-dialog">\r\n              <div class="modal-content">\r\n                <div class="modal-header">\r\n                  <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n                  <h4 class="modal-title" id="myModalLabel">Please Login</h4>\r\n                </div>\r\n                <div class="modal-body">\r\n                  ...\r\n                </div>\r\n                  <!--\r\n                    <div class="modal-footer">\r\n                      <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\r\n                      <button type="button" class="btn btn-warning">Save changes</button>\r\n                    </div>\r\n                  -->\r\n              </div>\r\n            </div>\r\n          </div>\r\n        </div>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 130, "134": 57, "140": 57, "16": 4, "18": 0, "34": 2, "35": 4, "36": 5, "40": 5, "41": 15, "42": 20, "43": 20, "44": 21, "45": 21, "46": 22, "47": 22, "48": 23, "49": 23, "50": 26, "51": 26, "52": 26, "53": 32, "54": 32, "55": 35, "56": 36, "57": 36, "58": 36, "59": 39, "60": 40, "61": 43, "66": 55, "71": 80, "76": 126, "81": 132, "82": 148, "83": 148, "84": 190, "85": 190, "86": 190, "92": 47, "98": 47, "104": 110, "146": 140, "111": 110, "112": 112, "113": 113, "114": 123, "116": 125, "122": 130}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF/homepage/templates/base.htm", "source_encoding": "ascii", "uri": "/homepage/templates/base.htm"}
__M_END_METADATA
"""
