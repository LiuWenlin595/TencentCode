#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import json
import requests
import time
import numpy as np

# https://iwiki.woa.com/pages/viewpage.action?pageId=1583794447
PROJECTNAME = "kaiwurl"
TOKEN = "1f7ff38fac25970544e622bad3bf3a22"
STAFFNAME = "tobeyzheng"
# URL = "http://openapi.zhiyan.oa.com/log/search/elasticsearch"
URL = "http://openapi.zhiyan.oa.com/log/v2/search/query"

# current_milli_time 获得当前本机unix毫秒时间戳
def current_milli_time():
  return round(time.time() * 1000)

class ZhiYanDB():
  def __init__(self, pn = PROJECTNAME, tk = TOKEN, sn = STAFFNAME):
    self.project_name = pn
    self.token = tk
    self.staff_name = sn
    self.header = {
      "X-API-Version": "v2",
      "Content-type": "application/json",
      "projectname": self.project_name,
      "token": self.token,
      "staffname": self.staff_name
    }
    self.api_url = URL

  def query(self, task_id, query_key, query_value, keys, start_time, end_time):
    query_params = {
      "startTime": start_time,
      "endTime": end_time,
      "dataflowName": "y1_public_br",
      "storageType": "elasticsearch",
      "filter": [
        {
          "key": "@task_id",
          "operator": "eq",
          "value": task_id
        },
        # {
        #   "key": "AvgMateDistanceInBattle",
        #   "operator": "lt",
        #   "value": 50
        # },
        # {
        #   "key": "AvgMateDistanceInSearch",
        #   "operator": "lt",
        #   "value": 50
        # },
        {
          "key": "AssitantNum",
          "operator": "gte",
          "value": 0
        }
        # {
        #   "type": "AND",
        #   "filters": [
        #     {
        #       "key": "KillNum",
        #       "operator": "gte",
        #       "value": 0
        #     }
        #   ]
        # }
        # {
        #   "key": f"{query_key}",
        #   "operator": "eq",
        #   "value": query_value
        #   # "value": f"{query_value}"
        # }
      ],
      "fields": keys.append("LadderLevel"),
      # "query": "@host: 106.53.106.243", #(与filter二选一，注意不支持storageType:clickhouse)
      "orderBy": "desc",
      "page": 1,
      "limit": 10000
    }
    print(query_params)
    res = requests.post(url = self.api_url, headers = self.header, json = query_params)
    res = json.loads(res.text)
    # 具体return code的报错可以查看 https://iwiki.woa.com/pages/viewpage.action?pageId=299491736
    if res['code'] != 0:
      print(res['msg'])
    # print(res)
    # return json.loads(res['data'])
    return res['data']

def reduce_mean(data, keys):
    ret = {k:[] for k in keys}
    for query in data:
        for k, v in query.items():
            if k in ret:
                ret[k].append(v)
    # return {k: np.mean(v) for k, v in ret.items()} "Cnt":len(v)}
    ret = {k: np.mean(v) for k, v in ret.items()}
    ret["Cnt"] = len(data)
    return ret

def reduce_mean_by_level(data, keys):
    ret = {}
    for query in data:
        level = int(query["LadderLevel"] / 10)
        if level not in ret:
            ret[level] = []
        ret[level].append(query)
    for k, v in ret.items():
        ret[k] = reduce_mean(v, keys)
    return ret 

def reduce_mean_by_kast(data, keys):
    ret = {}
    for query in data:
        level = int(query["AssitantNum"] * 10)
        if level not in ret:
            ret[level] = []
        ret[level].append(query)
    for k, v in ret.items():
        ret[k] = reduce_mean(v, keys)
    return ret 

def main():
    args = arg_parse()
    zhiYanDB = ZhiYanDB()
    keys = [
          "KillNum",
          "AssitantNum",
          "SurviveNum",
          "TradeNum",
          "AvgMateDistanceInBattle",
          "AvgMateDistanceInSearch"
    ]
    try_time = 3
    time_gap = args.secs * 1000.0 / 3.0
    start_time, end_time = current_milli_time() - args.secs * 1000, current_milli_time() 
    data = []
    for i in range(try_time):
        stime, etime = start_time + i * time_gap, start_time + (i+1)*time_gap
        d = zhiYanDB.query(args.task_id, args.key, args.value, keys, stime, etime)
        data.extend(d["list"])
    # print(data["list"])
    # if data != None:
    #   print(data["aggregations"])
    # print (keys)
    # print (reduce_mean(data["list"], keys))
    # print (reduce_mean_by_level(data["list"], keys))
    # ret = reduce_mean_by_level(data["list"], keys)
    ret = reduce_mean_by_kast(data, keys)
    # np.set_printoptions(precision=2)
    for level, val in sorted(ret.items()):
        print(level, {k:round(v, 2) for k, v in val.items()})
  

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task_id", type=str)
    parser.add_argument("--key", type=str)
    parser.add_argument("--value", type=int)
    parser.add_argument("--secs", type=int)
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    main()
