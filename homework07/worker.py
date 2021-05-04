from jobs import q, update_job_status
import time

@q.worker
def do_work(jid):
    update_job_status(jid, 'in progress')
    time.sleep(15)
    update_job_status(jid, 'complete')

do_work()
