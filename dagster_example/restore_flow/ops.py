from dagster import op,In,Nothing,Field

TYPE_NOTHING = In(Nothing)
nothing_input = {"start":TYPE_NOTHING}

@op(
    required_resource_keys={"source_db","target_db"}
    ,ins=nothing_input
    ,config_schema={
        "use_db":Field(
            str
            ,default_value="source_db"
        )
    }
)
def check_params_and_defaults(context):
    db_type = context.op_config.get("use_db")
    db_data = getattr(context.resources,db_type)
    source_host,source_port = db_data.values()
    context.log.info(f"Source host is {source_host}, port is {source_port}")
    # context.log.info(f"DB_DATA is {db_data}")



@op(config_schema={
    "RUN_JOB":Field(
        bool
        ,default_value=False
        ,description="If false, reloads job only and nothing executed (default)."
        )
    }
)
def run_job(context):
    run_job_param = context.op_config.get("RUN_JOB")
    context.log.info(f"Param RUN_JOB value is {str(run_job_param)}")


@op(config_schema={
        "BRANCH_OR_TAG":Field(str,default_value="mygitbranch")
    }
    ,ins=nothing_input
)
def clone_gitlab(context):
    branch = context.op_config.get("BRANCH_OR_TAG")
    context.log.info(f"Cloning repo with branch {branch}")



@op(required_resource_keys={"target_db"}
    ,ins=nothing_input
)
def mb_data_translate(context):
    host,port = context.resources.target_db.values()
    context.log.info(f"{context.resources}, type is {type(context.resources)}")
    context.log.info(f"Performing mindbody translate on target host {host}, target port is {port}")