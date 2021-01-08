#coding:utf-8
import datetime
import uuid
import pytest
import yaml
from jsonpath import jsonpath
from service.tag import Tag

#获取数据
def get_datas():
    with open('test_tag.yaml')as f:
        data=yaml.safe_load(f)
    updata_datas=data['update']['datas']
    updata_ids = data['update']['ids']
    add_datas=data['add']['datas']
    add_ids = data['add']['ids']
    delete_group_datas = data['delete_group']['datas']
    delete_tag_datas = data['delete_group']['datas']
    return [updata_datas,updata_ids,add_datas,add_ids,delete_group_datas,delete_tag_datas]

class TestTag:

    def setup(self):
        self.tag = Tag()

    #查询标签
    def test_list(self):
        r=self.tag.list()
        # print(r.json(),type(r.json()))
        assert r.json()['errcode']==0

    #更新标签
    @pytest.mark.parametrize("tag_id,tag_name",get_datas()[0],ids=get_datas()[1])
    def test_update_and_detect(self,tag_id,tag_name):
        tag_name = tag_name + str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        r = self.tag.update_and_detect(id=tag_id, tag_name=tag_name)
        assert r.json()['errcode'] == 0
        r=self.tag.list()
        print(r.json())
        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name

    #添加标签
    @pytest.mark.parametrize('group_name,tag',get_datas()[2],ids=get_datas()[3])
    def test_add_and_detect(self,group_name,tag):
        r=self.tag.add_and_detect(group_name=group_name,tag=tag)
        assert r

    #删除标签组
    @pytest.mark.parametrize('group_id',get_datas()[4])
    def test_delete_and_detect_group(self,group_id):
        r=self.tag.delete_and_detect_group(group_id)
        print(r.json(),type(r.json()))
        assert r.json()['errcode']==0

    #删除标签
    @pytest.mark.parametrize('tag_id',get_datas()[5])
    def test_delete_and_detect_tag(self,tag_id):
        r = self.tag.delete_and_detect_tag(tag_id)
        assert r.json()['errcode'] == 0