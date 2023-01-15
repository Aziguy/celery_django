from celery import shared_task


@shared_task(bind=True)
def make_some_iteration(self):
    for i in range(10):
        print(i)
    return "Done"
