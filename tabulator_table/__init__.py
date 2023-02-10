import streamlit.components.v1 as components

_component_func = components.declare_component(
    "tabulator",
    path="./tabulator_table"
)

def tabulator(data):
    # spec = json.dumps(fig, cls=PlotlyJSONEncoder)
    spec = data
    component_value = _component_func(spec = spec, default = None)
    return component_value