from flask import Flask, request, make_response, jsonify
from words import contents

app = Flask(__name__)


# Function to do the operation of pref and suff combination
def getprefsuff(str1, str2, li, lj):
    pre = str1[0:li]
    lstr2 = len(str2)
    suff = str2[lstr2 - lj: lstr2]
    return pre + suff;


# routing url as mentioned in the question
@app.route('/api/<str1>/<str2>', methods=['GET'])
def working_model(str1, str2):
    new_dict = {}
    new_dict["words"] = []
    for i in range(1, min(len(str2), len(str1)) + 1):
        for j in range(1, min(len(str2), len(str1)) + 1):
            string_val = getprefsuff(str1, str2, i, j)
            if contents.get(string_val, False):
                if string_val not in new_dict["words"]:
                    new_dict["words"].append(string_val)
    if not any(new_dict.values()):
        return "{ Error : 404 } "
    else:
        return new_dict


if __name__ == '__main__':
    app.run(debug=True)
