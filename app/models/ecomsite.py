from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import JSONField



class New_Product(models.Model):
	class Meta:
		db_table = 'products'
	created_on = models.DateTimeField(auto_now_add=True)

	p_img = models.CharField(null=True, max_length=50)
	p_upload_date = models.DateTimeField(default=datetime.now, blank=True, max_length=20)
	p_name = models.TextField()
	p_price = models.IntegerField()
	p_desc = models.TextField()
	p_rating = models.IntegerField(null=True)
	p_json = JSONField(null=True)