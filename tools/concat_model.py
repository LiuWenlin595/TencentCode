import tensorflow as tf
import joblib
import os
from google.protobuf import text_format

frozen_graph_path = "./saved_model.pbtxt"
model_strategy_path = "./model_10000"
model_low_level_path = "./model_178550"

def convert_pbtxt_to_pb(frozen_graph_path):
    with tf.gfile.FastGFile(frozen_graph_path, 'r') as f:
        graph_def = tf.GraphDef()
        file_content = f.read()
        text_format.Merge(file_content, graph_def)
        tf.train.write_graph(graph_def, 'res1', 'saved_model.pb', as_text=False)

convert_pbtxt_to_pb(frozen_graph_path)

# f = open(frozen_graph_path, "r")
# graph_protobuf = text_format.Parse(f.read(), tf.GraphDef())

# # Import the graph protobuf into our new graph.
# graph_clone = tf.Graph()
# with graph_clone.as_default():
#     tf.import_graph_def(graph_def=graph_protobuf, name="")

# # Display the graph inline.
# graph_clone.as_graph_def()

# # load_graph(frozen_graph)
# print("haha")

with tf.Graph().as_default() as graph:
    with open(frozen_graph, 'rb') as f:
        print(type(f))
        tf.import_graph_def(f)
    def get_load_variables_op(model_strategy_path, model_low_level_path, variables=None):
        variables = variables or tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES)
        print(variables)
        params_strategy = joblib.load(model_strategy_path)
        params_low_level = joblib.load(model_low_level_path)
        restores = []
        if isinstance(params_strategy, list):
            print("hunky in list", len(params_strategy), len(params_strategy), len(variables))
            assert len(params_strategy) == len(variables), 'number of variables loaded mismatches len(variables)'
            for d1, d2, v in zip(params_strategy, params_low_level, variables):
                if "strategy" in v:
                    print("in strategy, ", v)
                    restores.append(v.assign(d2))
                else:
                    print("in other, ", v)
                    restores.append(v.assign(d1))
        else:
            print("hunky in no list", len(params_strategy), len(params_strategy), len(variables))
            for v in variables:
                if v.name not in params_strategy and v.name not in params_low_level:
                    print("skip missing  param:{}".format(v.name))
                elif "strategy" in v.name:
                    print("in strategy, ", v.name)
                    restores.append(v.assign(params_low_level[v.name]))
                else:
                    print("in other, ", v.name)
                    restores.append(v.assign(params_strategy[v.name]))
        return restores

    def save_variables(save_path, variables=None, sess=None):
        variables = variables or tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES)

        ps = sess.run(variables)
        save_dict = {v.name: value for v, value in zip(variables, ps)}
        dirname = os.path.dirname(save_path)
        if any(dirname):
            os.makedirs(dirname, exist_ok=True)
        joblib.dump(save_dict, save_path)
    concat_op = get_load_variables_op(model_strategy_path, model_low_level_path)
    with tf.Session() as sess:
        sess.run(concat_op)
        save_variables("./model_concat", sess)
