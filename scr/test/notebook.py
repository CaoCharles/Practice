# -*- coding: utf-8 -*-
import datetime

# 儲存下一個新筆記的編號
last_id = 0

class Note:
    '''代表筆記本中的一個筆記 ,可用字串搜尋並儲存標籤. '''
    
    def __init__(self, memo, tags = ''):
        ''' 以紀錄與選擇性的空白分隔標籤初始化筆記. 自動的設置筆記的建構日期與編號 .''' 
        
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
    
    def match(self, filter):
        # 判斷筆記是否與搜尋文字相符.若相符回傳True, 否則回傳 False #
        # 搜尋區分大小寫且同時尋找文字與標籤 #
        return filter in self.memo or filter in self.tags
        
class Notebook:
    # 代表一群可以被標記、修改與搜尋的筆記 #
    
    def __init__(self):
        # 以空清單初始化筆記本 #
        self.notes = []
    
    def new_note(self, memo, tags = ''):
        # 建構新的筆記並加入到清單中 #
        self.notes.append(Note(memo, tags))
        
#     def modify_memo(self, note_id, memo):
#         # 找出特定編號的筆記並改變其內容為指定值 #
#         for note in self.notes:
#             if note.id == note_id:
#                 note.memo = memo
#                 break
    def modify_tags(self, note_id, tags):
        # 找出特定編號的筆記並改變其標籤為指定值 #
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break
            
    def search(self, filter):
        # 找出所有與指定條件字串相符的筆記 #
        return [note for note in self.notes if
                note.match(filter)]
            
    def _find_note(self, note_id):
        # 找出有特定的id的筆記 #
        for note in self.notes:
            if note.id == note_id:
                return note
        return note
    
    def modify_memo(self, note_id, memo):
        # 找出特定編號的筆記並改變其內容為指定值 #
        self._find_note(note_id).memo = memo

    
        