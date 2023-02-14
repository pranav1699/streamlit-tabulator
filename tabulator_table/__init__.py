import streamlit.components.v1 as components

_component_func = components.declare_component(
    "tabulator",
    path="./tabulator_table"
)

def tabulator(data,code,key):
    # spec = json.dumps(fig, cls=PlotlyJSONEncoder)
    spec = data
    key = key
    code=  code
    component_value = _component_func(spec = spec,key = key, code=code)
    return component_value


