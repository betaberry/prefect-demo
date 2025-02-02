from prefect import flow, task

@task
def web_task():
    return "this is a web task"


@flow
def hello_web():
    s = web_task()
    print(s)

if __name__ == '__main__':
    hello_web()