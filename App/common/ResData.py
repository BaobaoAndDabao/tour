from flask import jsonify

class ResData():
    def paramEmpty(paramName):
        res={"code":"-1","msg":paramName+"参数为空"}
        return jsonify(res)

    def fail(self):
        res={"code":"-1","msg":"失败"}
        return jsonify(res)

    def success(data):
        res = {"code": "0", "data": data}
        return jsonify(res)


