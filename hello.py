from bottle import route, run, template ,Bottle,static_file,error,request,response



# simplified version of generate_json_trace.py
import pg_logger, json

def json_finalizer(input_code, output_trace):
  ret = dict(code=input_code, trace=output_trace)
  json_output = json.dumps(ret, indent=2)
  print(json_output)



@route('/')
def index():
    return {'name':"dfff"}

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='assets')



@route('/run',method="POST")
def run_py():
     response.set_header('Origin', '*')
     code=request.forms.get("code")
     obj=pg_logger.exec_script_str(code, False,False, json_finalizer)
     
     
     return obj





@error(404)
def error404(error):
    return 'Nothing here, sorry'


run(host='localhost', port=90, debug=True, reloader=True)