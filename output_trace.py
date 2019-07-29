
# simplified version of generate_json_trace.py
import pg_logger, json


class Trace():
    def __init__(self,code):
        self.__code=code
        self.__output={}

    def json_finalizer(self,input_code, output_trace):
        ret = dict(code=input_code, trace=output_trace)
        json_output = json.dumps(ret, indent=2)
        self.__output=json_output

    def output_dict(self):
        pg_logger.exec_script_str(self.__code, False,False, self.json_finalizer)
        return self.__output
