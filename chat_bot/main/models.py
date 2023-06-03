from django.db import models

class Talk(models.Model):
    # メッセージ
    message = models.CharField(max_length=500)
    

    send_bot = models.BooleanField(default=False, help_text='ボットの時True')
    # 時刻
    # auto_now_add=True とすると、そのフィールドの値には、オブジェクトが生成されたときの時刻が保存されます。
    time = models.DateTimeField(auto_now_add=True)
    # send_bot = models.BooleanField()

    # def __str__(self):
    #     return "{} -> {}".format(self.sender, self.receiver)
    
class Q_A(models.Model):
    question_text = models.CharField(max_length=500)  
    answer_text = models.CharField(max_length=500)  


