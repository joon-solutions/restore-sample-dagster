from dagster_example.restore_flow.ops import nothing_input,check_params_and_defaults,mb_data_translate
from dagster import graph

@graph(ins=nothing_input)
def copy_db_schema(start):
    jobs = check_params_and_defaults(start)
    return jobs

@graph(
    ins=nothing_input
    )
def mb_translate_step(start):
    graphs = mb_data_translate(check_params_and_defaults(start))
    return graphs