from prefect import flow, task, get_run_logger


@flow(name="Show Args")
def print_args():
    print("test")


if __name__ == "__main__":
    print_args()
