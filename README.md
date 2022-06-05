1. Create environment variable to hold secrets. Create 2 environment variables with these name and value
MY_TEST_HOST=my_env_var_HOST
MY_TEST_PORT=my_env_var_PORT

2. Clone repo, cd into the folder and run this command in Terminal to create virtual environment, install requirements

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


3. Start dagit

dagit -f dagster_example/restore_flow/final_workflow.py

4. Go to Dagster UI
Open a web browser and go to localhost:3000

5. Run job
Go to Launchpad tab and input the sample config in file "dagster_example/restore_flow/sample_config.yaml"
Click Launch Run to start the job