from bottle import route, run, template ,Bottle,static_file,error,request,response

from output_trace import Trace





@route('/')
def index():
    return template("main")

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='assets')



@route('/run',method="POST")
def run_py():
     response.content_type = 'application/json'
     code=request.forms.get("code")
     #obj=pg_logger.exec_script_str(code, False,False, json_finalizer)
     trace=Trace(code)
     obj=trace.output_dict()
     print obj
     return obj





@error(404)
def error404(error):
    return 'Nothing here, sorry'


run(host='localhost', port=90, debug=True, reloader=True)