from dagster_example.restore_bash_flow.ops import check_params_and_defaults,clone_gitlab,run_job
from dagster_example.restore_bash_flow.graphs import copy_db_schema,mb_translate_step
from dagster import job,config_mapping

@config_mapping(config_schema={
    "source_host": str
    ,"source_port": str
    ,"target_host": str
    ,"target_port": str
    })
def simplified_config(val):
    source_host,source_port,target_host,target_port = val.values()
    return {
        "ops": {
            "run_job":{
                "config":{
                    "env":{
                        "RUN_JOB":"FALSE"
                    }
                }
            },
            "check_params_and_defaults":{
                "config":{
                    "env":{
                        "HOST":source_host
                        ,"PORT":source_port
                    }
                }
            },
            "clone_gitlab":{
                "config":{
                    "env":{
                        "BRANCH_OR_TAG":"mybranch"
                    }
                }
            },
            "copy_db_schema":{
                "ops":{
                    "check_params_and_defaults":{
                        "config":{
                            "env":{
                                "HOST":source_host
                                ,"PORT":source_port
                            }
                        }
                    }
                }
            },
            "copy_db_schema_2":{
                "ops":{
                    "check_params_and_defaults":{
                        "config":{
                            "env":{
                                "HOST":source_host
                                ,"PORT":source_port
                            }
                        }
                    }
                }
            },
            "mb_translate_step":{
                "ops":{
                    "check_params_and_defaults":{
                        "config":{
                            "env":{
                                "HOST":source_host
                                ,"PORT":source_port
                            }
                        }
                    },
                    "mb_data_translate":{
                        "config":{
                            "env":{
                                "HOST":target_host
                                ,"PORT":target_port
                            }
                        }
                    }
                }
            }
        }
    }


@job(
    config=simplified_config
    )
def restore_flow():
    step1 = clone_gitlab(check_params_and_defaults(run_job()))
    step2_1 = copy_db_schema(step1)
    step2_2 = copy_db_schema(step1)
    mb_translate_step([step2_1,step2_2])
    