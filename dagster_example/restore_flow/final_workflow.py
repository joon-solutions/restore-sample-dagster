from dagster import job,config_mapping,make_values_resource,StringSource
from dagster_example.restore_flow.graphs import copy_db_schema,mb_translate_step
from dagster_example.restore_flow.ops import run_job,clone_gitlab,check_params_and_defaults
from dagster_example.dagster_dbt.dbt_op import my_dbt_job, my_dbt_resource

@job(
    resource_defs={
        "source_db":make_values_resource(host=StringSource,port=StringSource)
        ,"target_db":make_values_resource(host=StringSource,port=StringSource)
        ,"dbt":my_dbt_resource
        }
    )
def restore_flow():
    step1 = clone_gitlab(check_params_and_defaults(run_job()))
    step2_1 = copy_db_schema(step1)
    step2_2 = copy_db_schema(step1)
    step3 = mb_translate_step([step2_1,step2_2])
    # step4 = my_dbt_job(step3)
