import uuid
from hotqueue import HotQueue
import redis
import os
import requests
import json
import pandas as pd
from datetime import datetime

q = HotQueue("queue", host='10.178.131.244', port=6379, db=2)
rd_jobs = redis.StrictRedis(host='10.178.131.244', port=6379, db=0)
rd_data = redis.StrictRedis(host='10.178.131.244', port =6379, db=1)

# import the two sets of lists of places where to get pizza                                                              
location1 = pd.read_cvs('8358_1.csv').fillna(0)
location2 = pd.read_cvs('Datafiniti_Pizza_Restaurants_and_the_Pizza_They_Sell_Jun19.csv').fillna(0)

#merge the two sets of data                                                                                              
full_location = pd.merge(location1, location2, how='left', left_on= ['id', 'address', 'categories'], right_on = ['id', '\
address','categories']).fillna(0)

#sort by id, address, and categories                                                                                     
full_location = full_location.sort_values(by=['id','address','categories'])

def get_locations():
      return total_locations

def _generate_jid():
      return str(uuid.uuid4())

def _generate_job_key(jid):
      if type(jid) == bytes:
            jid = jid.decode('utf-8')
      return 'job.{}'.format(jid)
    
def _instantiate_job(jid, status, start, end):
      if type(jid) == str:
          return {'id': jid,
                  'status': status,
                  'start': start,
                  'end': end
          }
      return {'id': jid.decode('utf-8'),
              'status': status.decode('utf-8'),
              'start': start.decode('utf-8'),
              'end': end.decode('utf-8')
      }

def _save_job(job_key, job_dict):
      """Save a job object in the Redis database."""
    rd.hmset(job_key, job_dict)

def _queue_job(jid):
      """Add a job to the redis queue."""
      q.put(jid)

def add_job(start, end, status="submitted"):
      """Add a job to the redis queue."""
      jid = _generate_jid()
      job_dict = _instantiate_job(jid, status, start, end)
      _save_job(_generate_job_key(jid), job_dict))
      _queue_job(jid)
      return job_dict

def update_job_status(jid, new_status):
      """Update the status of job with job id `jid` to status `status`."""
      jid, status, start, end, = rd_jobs.hmget(_generate_job_key(jid), 'id', 'status', 'start', 'end')
      job = _instantiate_job(jid,status, start, end)

      if(new_status == 'in progress'):
            worker_ip = os.environ.get('WORKER_IP')
            print(worker_ip)
            rd_jobs.hset(_generate_job_key(jid), 'worker', worker_ip)

      if job:
            job['status'] = new_status
            _save_job(_generate_job_key(job['id']), job)
      else:
            raise Exception()



