# -*- coding:utf-8 -*-
import redis


class RedisClient(object):
    def __init__(self, host, port, db, password):
        self.redis_conn = redis.StrictRedis(host=host, port=port,
                                            decode_responses=True, db=db,
                                            password=password)

    def get_keys(self):
        return self.redis_conn.keys()

    def delete(self, name):
        self.redis_conn.delete(name)

    def insert_cookies(self, cookies):
        self.redis_conn.set(cookies, '1')

    def delete_cookies(self, cookies):
        self.redis_conn.delete()

    def set_proxy_value(self, proxy, index):
        '''
        设置值这个方法只有在该代理IP对应的某个爬虫不可用的时候，才会调用，然后将对应位置的值1设置为0
        '''
        self.redis_conn.lset(proxy, index, 0)

    def insert_proxy(self, proxy):
        '''插入新的代理IP到IP池中去
                    1. 首先检测该ip是否在IP池中存在，如果存在，则不添加
                       如果不存在，则添加
                '''
        res = self.get_proxy_value(proxy)
        if not res:
            self.redis_conn.lpush(proxy, 0, 0, 0, 0, 1)

    def get_proxy_value(self, key):
        return self.redis_conn.lrange(key, 0, -1)


