import pytest
import os
import pickle
from christmas_list import ChristmasList as cList

@pytest.fixture
def myList():
    fName = "cList.pkl"
    
    if os.path.isfile(fName):
        os.remove(fName)
    yield fName

    if os.path.isfile(fName):
        os.remove(fName)
    

def describe_Christmas_List():
    
    def it_init_is_empty_list(myList):
        testList = cList(myList)
        assert os.path.isfile(myList)
        assert testList.loadItems() == []

    def it_loads_saved_items(myList):
        items = [{"name":'book',"purchased": False},
        {"name":'car', "purchased": False},
        {"name":'ball', "purchased": False}]
        testList = cList(myList)
        testList.saveItems(items)
        assert testList.loadItems() == items

    def it_saves_new_items(myList):
        items = [{"name":'book',"purchased": False},
        {"name":'car', "purchased": False},
        {"name":'ball', "purchased": False}]
        testList = cList(myList)
        testList.saveItems(items)
        assert testList.loadItems() == items
        newItems = [{"name":'pistol',"purchased": False},
        {"name":'phone', "purchased": False},
        {"name":'computer', "purchased":False}]
        testList.saveItems(newItems)
        assert testList.loadItems() == newItems
    
    def it_adds_new_items_to_saved_list(myList):
        items = [{"name":'book',"purchased": False},
        {"name":'car', "purchased": False},
        {"name":'ball', "purchased":False}]
        testList = cList(myList)
        testList.saveItems(items)
        assert testList.loadItems() == items
        testItem = {"name": 'doll', "purchased": False}
        newItem = "doll"
        testList.add(newItem)
        assert testItem in testList.loadItems()
    
    def it_checks_item_to_true(myList):
        items = [{"name":'book',"purchased": False},
        {"name":'car', "purchased": False},
        {"name":'ball', "purchased":False}]
        testList = cList(myList)
        testList.saveItems(items)
        name = 'book'
        testList.check_off(name)
        tList = testList.loadItems()
        for item in tList:
            if item["name"] == name:
                assert item["purchased"] is True
    
    def it_removes_item_from_list(myList):
        items = [{"name":'book',"purchased": False},
        {"name":'car', "purchased": False},
        {"name":'ball', "purchased":False}]
        testList = cList(myList)
        testList.saveItems(items)
        name = 'book'
        testList.remove(name)
        tList = testList.loadItems()
        assert name not in tList

