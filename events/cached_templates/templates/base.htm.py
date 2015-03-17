# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425419667.042756
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\events\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['top', 'content', 'left']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def top():
            return render_top(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n    \r\n    <title>Colonial Heritage Foundation</title>\r\n    \r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\r\n    <link rel="stylesheet" href="//code.jquery.com/ui/1.11.2/themes/smoothness/jquery-ui.css">\r\n    <script src="//code.jquery.com/jquery-1.10.2.js"></script>\r\n    <script src="//code.jquery.com/ui/1.11.2/jquery-ui.js"></script>\r\n    <link rel="stylesheet" href="/resources/demos/style.css">\r\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/scripts/script.js/"></script>\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n  \r\n  </head>\r\n  <body>\r\n  \r\n    <header>\r\n      <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/header.jpg" width="100%">\r\n    </header> \r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\r\n      \r\n\r\n\r\n\r\n\r\n  \r\n\r\n<!--\r\n<nav class="navbar navbar-default">\r\n  <div class="container-fluid">\r\n    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n      <ul class="nav navbar-nav">\r\n        <li><a href="index">Home</a></li>\r\n        <li><a href="#">About</a></li>\r\n        <li><a href="#">Gallery</a></li>\r\n        <li><a href="#">Products</a></li>\r\n        <li><a href="#">Products</a></li>\r\n      </ul>\r\n      <ul class="nav navbar-nav navbar-right">\r\n        </li>\r\n        <form class="navbar-form navbar-right" role="search">\r\n          <div class="form-group">\r\n            <input type="text" class="form-control" placeholder="Search">\r\n          </div>\r\n          <button type="submit" class="btn btn-default">Submit</button>\r\n        </form>\r\n      </ul>\r\n    </div>\r\n  </div>\r\n</nav>\r\n-->\r\n  \r\n    <div class="wrapper">\r\n\r\n      <div class="row">\r\n\r\n      <div class="col-sm-2">\r\n        ')
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
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n      <div class="row top-header">\r\n          <div class="col-md-9 top-header"></div>\r\n          <div class="col-md-1 top-header"><strong>Welcome, ')
        __M_writer(str( request.user.first_name ))
        __M_writer('</strong></div>\r\n          <div class="col-md-1 top-header"><a href="/homepage/logout/" class="top-nav">Logout</a></div>\r\n          <div class="col-md-1 top-header"><a href="SignUp" class="top-nav">Sign Up</a></div>\r\n      </div>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n        Site content goes here in sub-templates.\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n          <div class="left-menu">\r\n            <h2 class="managenav">Manage</h2>\r\n            <ul>\r\n              <li class="menu-nav"><a href="/events/event/">Events</a></li>\r\n              <li class="menu-nav"><a href="/inventory/item/">Inventory</a></li>\r\n              <li class="menu-nav"><a href="/inventory/product/">Products</a></li>\r\n              <li class="menu-nav"><a href="/inventory/order/">Orders</a></li>\r\n              <li class="menu-nav"><a href="/events/venue/">Venues</a></li>\r\n              <li class="menu-nav"><a href="/users/users/">Users</a></li>\r\n            </ul>\r\n          </div>\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\colonialHF\\events\\templates/base.htm", "line_map": {"64": 155, "65": 155, "66": 155, "72": 34, "80": 37, "79": 34, "16": 4, "81": 37, "18": 0, "87": 95, "93": 95, "32": 2, "33": 4, "34": 5, "99": 79, "38": 5, "39": 15, "40": 22, "41": 22, "42": 25, "43": 25, "44": 25, "45": 31, "46": 31, "111": 105, "51": 41, "105": 79, "56": 91, "61": 97, "62": 113, "63": 113}, "uri": "base.htm", "source_encoding": "ascii"}
__M_END_METADATA
"""
