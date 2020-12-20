from jichuex.gndyex import LwGndyExObj
from jichuex.gndyex import ListThread


class Factory:
    def __init__(self, name: str, win_name, pic_config, limit=False, limit_num=0, add_sum=15):
        self.work = LwGndyExObj(name, win_name, pic_config, add_sum=add_sum, limit_num=limit_num, limit=limit)
        self.equi = ListThread(limit, limit_num, name, add_sum)
