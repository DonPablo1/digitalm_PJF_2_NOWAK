

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_product_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total_sales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='total_sales_amount',
            field=models.IntegerField(default=0),
        ),
    ]
