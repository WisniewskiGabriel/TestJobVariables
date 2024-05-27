from prefect import flow, task, get_run_logger, variables


@flow(name="Show args", log_prints=True)
def print_args():
    print("test")
    x = variables.get()


if __name__ == "__main__":
    print_args()
