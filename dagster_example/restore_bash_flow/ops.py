from dagster_shell import create_shell_command_op
from dagster import op,In,Nothing,Field

TYPE_NOTHING = In(Nothing)
nothing_input = {"start":TYPE_NOTHING}

check_params_and_defaults = create_shell_command_op(
    'echo "Source host is $HOST, port is $PORT"'
    ,name="check_params_and_defaults"
)

run_job = create_shell_command_op(
    'echo "Param RUN_JOB value is $RUN_JOB"'
    ,name="run_job"
)

clone_gitlab = create_shell_command_op(
    'echo "Cloning repo with branch $BRANCH_OR_TAG"'
    ,name="clone_gitlab"
)

mb_data_translate = create_shell_command_op(
    'echo "Performing mindbody translate on target host $HOST, target port is $PORT"'
    ,name="mb_data_translate"
)