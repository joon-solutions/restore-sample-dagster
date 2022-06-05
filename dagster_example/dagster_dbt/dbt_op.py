from dagster_example.restore_flow.ops import nothing_input
from dagster_dbt import dbt_cli_resource,dbt_run_op,dbt_test_op
from dagster import op,job,graph

my_dbt_resource = dbt_cli_resource.configured(
    {
        "project_dir": "/home/toandm/research/04.dbt/mysql_dbt/test_mysql",
        "profiles_dir": "/home/toandm/.dbt",
    }
)

@graph(
    ins=nothing_input
)
def my_dbt_job(start):
    graph = dbt_test_op(start_after=dbt_run_op(start))
    return graph